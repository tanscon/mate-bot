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
dispatcher = updater.dispatcher

def start(bot, update):     
        try:
            with open('data.json','r') as fp:
                loadedCount = json.load(fp)
            global count
            count = loadedCount
            print count
        except IOError:
            print "json.data wasnt found"
        bot.send_message(chat_id=update.message.chat_id, text="I will now start to count")


def shutdown():
	updater.stop()
	updater.is_idle = False

def stop(bot, update):
        jsonarray = json.dumps(count)
        print jsonarray
        with open('data.json', 'w') as outfile:
            json.dump(count, outfile)
        threading.Thread(target=shutdown).start()

def printOutMate(bot, update):
        user = update.message.from_user
        if str(user.id) in count:
            content = user.first_name + " got " + str(count[str(user.id)]) + " mate already."
            bot.send_message(chat_id=update.message.chat_id, text=content)
        else:
            bot.send_message(chat_id=update.message.chat_id, text="Drink more mate!")

def add(bot, update, args):
        print count
        user = update.message.from_user
        userId = str(user.id)
        if userId in count:
            print "old"
            count[userId] = int(count[userId]) + int(args[0])
        else:
            print "new"
            count[userId] = args[0]
        count["total"] = int(count["total"]) + int(args[0])
        bot.send_message(chat_id=update.message.chat_id, text=("added " + args[0]) + " Mate to " + user.first_name)

#Add all handler to the dispatcher 
print_handler = CommandHandler("mate", printOutMate)
start_handler = CommandHandler('start', start)
stop_handler = CommandHandler('stop', stop)
add_handler = CommandHandler('add', add, pass_args=True)

dispatcher.add_handler(print_handler)
dispatcher.add_handler(start_handler)
dispatcher.add_handler(stop_handler)
dispatcher.add_handler(add_handler)

updater.start_polling()

