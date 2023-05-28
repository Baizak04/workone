import telebot

# Установите токен вашего бота
# TOKEN = 'YOUR_BOT_TOKEN'

# Создайте экземпляр объекта бота
bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

# Обработчик команды /pdf
@bot.message_handler(commands=['pdf'])
def send_pdf(message):
    # Укажите путь к PDF-файлу
    pdf_path = 'api_bot/python.pdf'
    
    # Отправка PDF-файла
    with open(pdf_path, 'rb') as file:
        bot.send_document(message.chat.id, file)

# Запуск бота
bot.polling()