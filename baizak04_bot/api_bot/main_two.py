import telebot
from telebot import types


bot = telebot.TeleBot('6287454351:AAE4VdG2Fp0Pj0P8u4HIPegkldIi9T0_G8Q')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup()
    but1 = types.KeyboardButton('Перейти на сайт')
    markup.row(but1)
    but2 = types.KeyboardButton('Удалить фото')
    but3 = types.KeyboardButton('изменить фото')
    markup.row(but2, but3)
    file = open('./photo.jpg', 'rb')
    bot.send_photo(message.chat.id, file, reply_markup=markup)
    # bot.send_message(message.chat.id, 'Привет', reply_markup=markup)
    bot.register_next_step_handler(message, on_click)

def on_click(message):
    if message.text == "Перейти на сайт":
        bot.send_message(message.chat.id, 'Открыт сайт')
    elif message.text == 'Удалить фото':
        bot.send_message(message.chat.id, 'Удалить фото')






# @bot.message_handler(content_types=['photo'])
# def get_photo(message):
#     bot.reply_to(message, 'Какое красивое фото 😍')
    

@bot.message_handler(content_types=['photo'])
def get_photo_two(message):
    markup = types.InlineKeyboardMarkup()
    but1 = types.InlineKeyboardButton('перейти на сайт', url='https://www.linkedin.com/in/baizak-nadurbekov/')
    markup.row(but1)
    but2 = types.InlineKeyboardButton('удалить фото', callback_data='delete')
    but3 = types.InlineKeyboardButton('изменить фото', callback_data='edit')
    markup.row(but2, but3)
    bot.reply_to(message, 'Какое красивое фото 😍', reply_markup=markup)
    
    
@bot.callback_query_handler(func=lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

bot.polling(none_stop=True)