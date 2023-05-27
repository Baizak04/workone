import telebot
from telebot import types

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['links'])
def button_one(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_one = types.InlineKeyboardButton(text='ссылка на гитхаб', url='https://github.com/Baizak04')
    btn_two = types.InlineKeyboardButton(text='ссылка на instagram', url='https://www.instagram.com/nadurbekov_144/')
    kb.add(btn_one, btn_two)
    bot.send_message(message.chat.id, 'ссылки 🤭', reply_markup=kb)

bot.polling()