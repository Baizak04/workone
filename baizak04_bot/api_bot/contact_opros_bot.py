import telebot


bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')


@bot.message_handler(commands=['location'])
def location(message):
    bot.send_location(message.chat.id, 42.000012,74.000017)

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_contact(message.chat.id, phone_number=+996501751998, first_name='Baizak', last_name='Nadurbekov')

@bot.message_handler(commands=['contact_alt'])
def contact(message):
    bot.send_contact(message.chat.id, phone_number=+996708153711, first_name='A', last_name='')



@bot.message_handler(commands=['polls'])
def polls(message):
    bot.send_poll(message.chat.id, question='сколько вам лет?', options=['14', '55', 'не скажу'], allows_multiple_answers=False, is_anonymous=True)




bot.polling()