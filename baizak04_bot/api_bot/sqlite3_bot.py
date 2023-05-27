import telebot
import sqlite3

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['sql'])
def sql(message):
    conn = sqlite3.connect('bot.sql')
    cur = conn.cursor()
    
    cur.execute('CREATE TABLE IF NOT EXISRS users (id)')