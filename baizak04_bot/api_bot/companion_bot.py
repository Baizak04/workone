import telebot
from telebot import types
from time import sleep

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')


@bot.message_handler(content_types=['text'])
def text_two(message):
    if message.text == "Как поживаешь?":
        sleep(3)
        bot.send_message(message.chat.id, 'Спасибо, что спросили 🥺. Я - компьютерная программа и не могу иметь состояния или чувств, но я всегда готов помочь вам решить любые задачи.')
    elif message.text == "Чем занимаешься?":
        sleep(5)
        bot.send_message(message.chat.id, 'Я создан, чтобы помочь в решении различных задач. Моя функциональность может быть различной в зависимости от того, какую задачу вы мне поставите. Я могу отвечать на вопросы, предоставлять информацию и многое другое. Таким образом, моя деятельность напрямую связана с теми задачами, которые мне поставляют.')
  
bot.polling()