import telebot
from telebot import types


bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['callback'])
def callback(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton(text='Салам', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='Ваалейкум', callback_data='btn2')
    kb.add(btn, btn1)
    bot.send_message(message.chat.id, 'выбери что-то из них', reply_markup=kb)
    
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton(text='алейкум', callback_data='btn2')
        btn1 = types.InlineKeyboardButton(text='салам', callback_data='btn1')
        kb.add(btn, btn1)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='хихих 😂 \n Предупреждения!!! дальше ничего не нажимай', reply_markup=kb)    



bot.polling()