import telebot
import sqlite3
from telebot import types
bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')
name = None



@bot.message_handler(commands=['registration'])
def sql(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()
    
    bot.send_message(message.chat.id, 'Привет это регистрация! Введите ваше имя')
    bot.register_next_step_handler(message, user_name)
    
def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, 'Введите пароль')
    bot.register_next_step_handler(message, user_pass)
    
    
def user_pass(message):
    password = message.text.strip()
    
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    
    cur.execute("INSERT INTO users (name, pass) VALUES (?, ?)", (name, password))
    conn.commit()
    cur.close()
    conn.close()
    
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован!', reply_markup=markup)
    
@bot.callback_query_handler(func=lambda call: True)
def callback_two(call):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    
    cur.execute('SELECT * FROM users')
    users = cur.fetchall()
    
    info = ''
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'
        
    
    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)
    
    
bot.polling(none_stop=True)