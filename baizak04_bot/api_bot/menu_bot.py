import telebot
from telebot import types, util
import random
TOKEN = '6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎲 Рандомное число')
    item2 = types.KeyboardButton('👨🏻‍💻 Программирование')
    item3 = types.KeyboardButton('💁 Информация') 
    item4 = types.KeyboardButton('➡️ Другое')
    
    markup.add(item1, item2, item3, item4)
    
    bot.send_message(message.chat.id, 'Это меню, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число ' + str(random.randint(0, 100)))
        elif message.text == '👨🏻‍💻 Программирование':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('ссылка')
            item2 = types.KeyboardButton('👨🏻‍💻 Программирование')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, back)
            
            bot.send_message(message.chat.id,'👨🏻‍💻 Программирование', reply_markup=markup)

        elif message.text == '💁 Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🤖 о боте')
            item2 = types.KeyboardButton('🐍 Что такое Python?')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, back)
            
            bot.send_message(message.chat.id,'💁 Информация', reply_markup=markup)

        elif message.text == '➡️ Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🛠 Настройка')
            item2 = types.KeyboardButton('📨 Подписка')
            item3 = types.KeyboardButton('😈 Стикер')

            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, back)
            
            bot.send_message(message.chat.id,'➡️ Другое', reply_markup=markup)


        elif message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🎲 Рандомное число')
            item2 = types.KeyboardButton('👨🏻‍💻 Программирование')
            item3 = types.KeyboardButton('💁 Информация') 
            item4 = types.KeyboardButton('➡️ Другое')
            
            markup.add(item1, item2, item3, item4)
            
            bot.send_message(message.chat.id, '⬅️ Назад', reply_markup=markup)
    
        elif message.text == '😈 Стикер':
            stick = open('sticer/sticerslon.png', 'rb')
            bot.send_sticker(message.chat.id, stick)
            
        elif message.text == '🐍 Что такое Python?':
           text = open('txt/python.txt', 'r', encoding="utf8").read()
           for mess in util.smart_split(text, 3000):
                bot.send_message(message.chat.id, mess)

bot.polling()