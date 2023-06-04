import random
import telebot

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

smiles = [
    '❤️',
    '😂',
    '😜',
    '😊',
    '😎',
]

bot.message_handler(func=lambda message: True)
def smile(message):
    bot.reply_to(message, random.choice(smiles))
    
bot.polling()
