import telebot
import webbrowser


bot = telebot.TeleBot('6287454351:AAE4VdG2Fp0Pj0P8u4HIPegkldIi9T0_G8Q')
API ='8b78cb6da2d98c5f2540773af280dca0'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет, рад тебя видеть. Напиши название города')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()



bot.polling(none_stop=True)