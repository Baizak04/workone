import telebot
from telebot import util

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')


@bot.message_handler(commands=['python'])
def python_txt(message):
    text = open('python.txt', 'r', encoding="utf8").read()
    for mess in util.smart_split(text, 3000):
        bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['django'])
def django_txt(message):
    text = open('django.txt', 'r', encoding="utf8").read()
    for mess in util.smart_split(text, 3000):
        bot.send_message(message.chat.id, mess)

bot.polling()