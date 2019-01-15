#/usr/bin/python

import sys
import json
from telegram.ext import Updater
import threading
import logging
logging.basicConfig(format='%(asctime)s - %(name)s -%(levelname)s - %(message)s',level=logging.INFO)
updater = Updater(token='732629412:AAGozAsOtKqhdK5nTs7_9GKv6rQ-0L754os')
from telegram.ext import CommandHandler


count = {"total": 0}
path = sys.path[0]
dispatcher = updater.dispatcher

def start(bot, update):     
        try:
            loadedCount = open("data.json","r")
            global count
            count = json.load(loadedCount)
            print count
        except IOError:
            print "json.data wasnt found"
        bot.send_message(chat_id=update.message.chat_id, text="I am a bot, please talk to me!")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

def shutdown():
	updater.stop()
	updater.is_idle = False

def stop(bot, update):
        jsonarray = json.dumps(count)
        print jsonarray
        with open('data.json', 'w') as outfile:
            json.dump(count, outfile)
        threading.Thread(target=shutdown).start()

stop_handler = CommandHandler('stop', stop)
dispatcher.add_handler(stop_handler)



def add(bot, update, args):
        user = update.message.from_user
        if user.id in count:
            count[user.id] = int(count[user.id]) + int(args[0])
        else:
            count[user.id] = args[0]
        count["total"] = int(count["total"]) + int(args[0])
        bot.send_message(chat_id=update.message.chat_id, text=("added " + args[0]) + " Mate to " + user.first_name)


add_handler = CommandHandler('add', add, pass_args=True)
dispatcher.add_handler(add_handler)

updater.start_polling()

