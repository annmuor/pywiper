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


def wipe(client, _id, days):
    till = int(time()) - (3600 * 24 * days)
    for message in client.iter_history(_id):
        if message.date < till:
            break
        message.delete()


def list(client):
    outcome = [('ID', 'DIALOG')]
    for dialog in client.iter_dialogs():
        if dialog.chat.type == "group" or dialog.chat.type == "supergroup":
            outcome.append((dialog.chat.id, dialog.chat.title))
    return outcome


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("id", help='id', type=int)
    parser.add_argument("hash", help='hash')
    parser.add_argument("-l", "--list", help="list", action="store_true")
    parser.add_argument("-w", "--wipe", help="wipe <id> <days>", nargs='+', )
    args = parser.parse_args()
    with Client("my_account", args.id, args.hash) as client:
        if args.list:
            pprint.pprint(list(client))
        if args.wipe:
            wipe(client, args.wipe[0], args.wipe[1])
