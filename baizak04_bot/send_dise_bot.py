import telebot
from telebot import types
from telebot import util

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['sticer_football'])
def sticer(message):
    bot.send_dice(message.chat.id, '⚽️')


@bot.message_handler(commands=['sticer_basketball'])
def sticer_basketball(message):
    bot.send_dice(message.chat.id, '🏀')

@bot.message_handler(commands=['sticer_2'])
def sticer_2(message):
    bot.send_dice(message.chat.id, '🎯')
    
@bot.message_handler(commands=['sticer_bowling'])
def sticer_bowling(message):
    bot.send_dice(message.chat.id, '🎳')
    
@bot.message_handler(commands=['sticer_casino'])
def sticer_casino(message):
    bot.send_dice(message.chat.id, '🎰')


bot.polling()