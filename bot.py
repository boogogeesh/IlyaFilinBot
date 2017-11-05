import config
import telebot
import time
import random
import re

from pikabu import get_pikabu_post_link

bot = telebot.TeleBot(config.token)

YOBA_CONFUSED = "CAADAgAD0gMAAgwWHwL2Lqda-jMVBAI"
YOBA_GLAD = "CAADAgAD6AMAAgwWHwIOqWgUfLdNNQI"


@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    time.sleep(1)
    processed_msg = message.text.lower()
    if "пис" in processed_msg:
        bot.send_message(message.chat.id, random.choice(['пись', 'пись)', 'пись))', 'пись))00)0']))
    if "илья" in processed_msg and "гей" in message.text.lower():
        bot.send_sticker(message.chat.id, YOBA_CONFUSED)
    if re.search(r'м+и+я+г+и+', processed_msg):
        bot.send_message(message.chat.id, "мияяяяяги")
    if "как дела" in processed_msg:
        bot.send_message(message.chat.id, "Хорошо")
        bot.send_message(message.chat.id, "А у тебя?")
        bot.send_message(message.chat.id, get_pikabu_post_link())
        bot.send_sticker(message.chat.id, YOBA_GLAD)


if __name__ == '__main__':
    bot.polling(none_stop=True)
