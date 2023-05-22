import telebot
from telebot import types


bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['switch'])
def switch(message):
    kb = types.InlineKeyboardMarkup()
    switch = types.InlineKeyboardButton(text='Выбрат чат', switch_inline_query='Тур эй сасыбай 😂😂😂')
    kb.add(switch)
    bot.send_message(message.chat.id, 'Сообщение', reply_markup=kb)

bot.polling()