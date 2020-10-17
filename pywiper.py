#!/usr/bin/env python3

import argparse
import pprint
from time import time

import pip

try:
    from pyrogram import Client
except ImportError:
    if hasattr(pip, 'main'):
        pip.main(['install', 'pyrogram'])
        pip.main(['install', 'tgcrypto'])
    else:
        pip._internal.main(['install', 'pyrogram'])
        pip._internal.main(['install', 'tgcrypto'])


def _wipe(client, _id, till_days=1, since_days=0, *args):
    till_ts = int(time() - (3600 * 24 * int(till_days)))
    since_ts = int(time() - (3600 * 24 * int(since_days)))

    for message in client.iter_history(_id):
        if message.date < till_ts:
            break
        if message.date > since_ts:
            continue
        message.delete()

def _erase(client, _id, *args):
    for message in client.iter_history(_id):
        if message.outgoing:
            print("Delete: >", message.text)
            message.delete()

def _list(client):
    outcome = [['ID', 'DIALOG']]
    for dialog in client.iter_dialogs():
        if dialog.chat.type == "group" or dialog.chat.type == "supergroup":
            outcome.append([dialog.chat.id, dialog.chat.title])
    return outcome


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--id", type=int, help="my.telegram.org/apps API ID", required=True)
    parser.add_argument("-s", "--secret", help="my.telegram.org/apps API Secret", required=True)
    parser.add_argument("-l", "--list", help="list chats", action="store_true")
    parser.add_argument("-w", "--wipe", help="wipe <id> [until days [since days]]", nargs='+', )
    parser.add_argument("-e", "--erase", help="erase <id>", nargs='+', )
    args = parser.parse_args()

    with Client("my_account", args.id, args.secret) as client:
        if args.list:
            for chat in _list(client):
                print("{0:20} {1}".format(*chat))
        if args.wipe:
            _wipe(client, *args.wipe)
        if args.erase:
            _erase(client, *args.erase)

