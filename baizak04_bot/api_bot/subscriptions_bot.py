import telebot
from telebot import types

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['subscription'])
def subscription(message):
    channel_link = "https://t.me/+-6Nt9nY9T7s1OWMy"
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.KeyboardButton(text='Подтвердить ✅')
    markup.add(keyboard)
    chat_id = message.chat.id
    user = message.chat.first_name
    bot.send_message(chat_id, f'Привет {user} Чтобы пользоваться ботом подпишис на канал\n'
                     f'{channel_link}', reply_markup=markup)
    
@bot.message_handler(content_types=['text'])
def subscription_two(message):
    user = message.chat.first_name
    if message.chat.type == 'private':
        if message.text == 'Подтвердить ✅':
            status = ['creator', 'administrator', 'member']
            for stat in status:
                if stat ==bot.get_chat_member(chat_id='@+-6Nt9nY9T7s1OWMy', user_id=message.from_user.id).status:
                    bot.send_message(message.chat.id, f'Доступ открыт {user}')
                    break
                
            else:
                bot.send_message(message.chat.id, f'{user}Не пытайтесь работа с ботом для вас закрыт')
    
bot.polling()
    
    
    