import telebot
from telebot import types
from telebot import util
import random
from time import sleep

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')


STICKER_ID = 'CAACAgIAAxkBAAEJNdFkfOimFqVgJp0FK5C-DNdVrUUprAACDR8AAhrkOUp-mJM1072QEC8E'
STICKER_ID_ONE = 'CAACAgIAAxkBAAEJOZlkft26O4uEZaBFPOtq6zfXDRxKUAACWxoAAmqfMUpmtfP_ZUtlji8E'




@bot.message_handler(content_types=['text'])
def text_two(message):
    if 'Байзак' in message.text:
        sleep(2)
        bot.reply_to(message, 'Мой хозяин всегда на связи 👨🏻‍💻')
        return
    
@bot.message_handler(content_types=['sticker'])
def sticker_handler(message):
    bot.send_sticker(message.chat.id, random.choice([STICKER_ID, STICKER_ID_ONE]))


bot.polling(none_stop=True)