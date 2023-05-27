import telebot
from telebot import types

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['button_two'])
def button_two(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item = types.InlineKeyboardButton('Как дела бот?', callback_data='question_one')
    item_two = types.InlineKeyboardButton('Пока бот', callback_data='goodbye')
    markup.add(item, item_two)
    bot.send_message(message.chat.id, 'hello', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback_two(call):
    if call.message:
        if call.data == 'question_one':
            bot.send_message(call.message.chat.id, 'хорошо 😁')
        if call.data == 'goodbye':
            bot.send_message(call.message.chat.id, 'удачи тебе 👋')


bot.polling()