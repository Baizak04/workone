import telebot
from telebot import types


bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['swit'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    url = types.InlineKeyboardButton(text='URL', url='https://www.edx.org/')
    switch = types.InlineKeyboardButton(text='Swit', switch_inline_query='hello 👨🏻‍💻')
    callback = types.InlineKeyboardButton(text='Callback', callback_data='hello')
    markup.add(url, switch, callback)
    bot.send_message(message.chat.id, 'Сообщение 👨🏻‍💻', reply_markup=markup)

bot.polling()