from sys import argv
from time import time
try:
    from pyrogram import Client
except ImportError:
    print("Please run: pip install --user pyrogram tgcrypto")
    exit(1)
print("**** TELEGRAM GROUPS WIPER ****")
print("* Idea: @annmuor")
print("* First python release: @stenopolz")
print("** Stay Safe! **")

if len(argv) < 3:
    print("Usage: {} <id:hash> <list|wipe id [days]>".format(argv[0]))
    exit(1)

if argv[2] == "wipe" and len(argv) < 4:
    print("Usage: {} <id:hash> <list|wipe id [days]>".format(argv[0]))
    exit(1)

x = argv[1].split(":")
api_id = x[0]
api_hash = x[1]

with Client("my_account", api_id, api_hash) as app:
    if argv[2] == "list":
        print("ID".ljust(20),"DIALOG")
        for dialog in app.iter_dialogs():
            if dialog.chat.type == "group" or dialog.chat.type == "supergroup":
                print("{}".format(dialog.chat.id).ljust(20),dialog.chat.title)
        exit(0)
    if argv[2] == "wipe":
        id = int(argv[3])
        days = 1
        if len(argv) > 4:
            days = int(argv[4])

    till = int(time()) - (3600*24*days)
    for message in app.iter_history(id):
        if message.date > till:
            message.delete()
        else:
            exit(0)
