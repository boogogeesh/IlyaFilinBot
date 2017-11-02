import config
import telebot
import time
import random

bot = telebot.TeleBot(config.token)
@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    time.sleep(1)
    if "пис" in message.text.lower():
        bot.send_message(message.chat.id, random.choice(['пись', 'пись)', 'пись))','пись))00)0']))
    if "илья" in message.text.lower() and "гей" in message.text.lower():
        bot.send_message(message.chat.id, "нет ты(")

if __name__ == '__main__':
    bot.polling(none_stop=True)
