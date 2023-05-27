import telebot



bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')


@bot.message_handler(commands=['startthree'])
def start(message):
    chat_id = message.chat_id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f'Привет чем могу помочь {first_name} !')


bot.polling() 