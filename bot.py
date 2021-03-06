import config
import telebot
import time
import random
import re
import sys, traceback
import quotes

from pikabu import get_pikabu_post_link

bot = telebot.TeleBot(config.token)

YOBA_CONFUSED = "CAADAgAD0gMAAgwWHwL2Lqda-jMVBAI"
YOBA_GLAD = "CAADAgAD6AMAAgwWHwIOqWgUfLdNNQI"


@bot.message_handler(commands=['help'])
def handle_start_help(message):
    bot.send_message(message.chat.id, "Дароу, я Илья. \n Мои команды: \n /pikabu")
    
@bot.message_handler(commands=['quote'])
def handle_start_help(message):
    bot.send_message(message.chat.id, random.choice(quotes.list))


@bot.message_handler(commands=['pikabu'])
def handle_start_help(message):
    try:
        bot.send_message(message.chat.id, "Конечно, брат, держи")
        bot.send_message(message.chat.id, get_pikabu_post_link())
        bot.send_sticker(message.chat.id, YOBA_GLAD)

    except:
        print("Pikabu exception occurred with following stacktrace:")
        traceback.print_exc(file=sys.stdout)
        bot.send_message(message.chat.id, "Бля, чёт поломалось, не будет истории(")


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    try:
        time.sleep(1)
        processed_msg = message.text.lower()
        if "илья" in processed_msg and "гей" in processed_msg:
            bot.send_sticker(message.chat.id, YOBA_CONFUSED)
        if re.search(r'м+и+я+г+и+', processed_msg):
            bot.send_message(message.chat.id, "мияяяяяги")

    except:
        traceback.print_exc(file=sys.stdout)


if __name__ == '__main__':
    bot.polling(none_stop=True)
