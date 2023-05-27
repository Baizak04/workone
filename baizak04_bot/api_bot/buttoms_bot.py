import telebot
from telebot import types


bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['button'])
def button(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1 )
    btn1 = types.KeyboardButton(text='кнопка1')
    btn2 = types.KeyboardButton(text='кнопка2')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'кнопки', reply_markup=kb)

bot.polling()