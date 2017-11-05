import config
import telebot
import time
import random
import re

bot = telebot.TeleBot(config.token)


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    time.sleep(1)
    processed_msg = message.text.lower()
    if "пис" in processed_msg:
        bot.send_message(message.chat.id, random.choice(['пись', 'пись)', 'пись))', 'пись))00)0']))
    if "илья" in processed_msg and "гей" in message.text.lower():
        bot.send_sticker(message.chat.id, "CAADAgAD0gMAAgwWHwL2Lqda-jMVBAI")
    if re.search(r'м+и+я+г+и+', processed_msg):
        bot.send_message(message.chat.id, "мияяяяяги")
    if re.search(r'\*илья как дела\*', processed_msg):
        bot.send_message(message.chat.id, )


if __name__ == '__main__':
    bot.polling(none_stop=True)
