import telebot
import webbrowser


bot = telebot.TeleBot('6287454351:AAE4VdG2Fp0Pj0P8u4HIPegkldIi9T0_G8Q')

@bot.message_handler(commands=['site', 'website', 'itspace_kg'])
def site(message):
    webbrowser.open('https://www.w3schools.com/python/')

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, f"Здраствуйте, {message.from_user.first_name}")
    
@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, "<b>Справочная</b> <em><u>информация</u></em>", parse_mode='html')
    
@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

    
bot.polling(none_stop=True)