import telebot
from telebot import types

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['site'])
def start(message):
    mess = f'Привет,Я ваш персональный бот \n команды \n /start, /LinkedinBaizaka, /palindrome_leetcode, /AbstractBaseUser, /SQLRoadmap, /CreatedUser, /AbstractUser_YouTube  <b>{message.from_user.first_name} \n Выбирай полезные команды и начинай изучать \n <u>Удачи тебе 😊👍</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет":
        bot.send_message(message.chat.id, "И тебе привет", parse_mode='html')
    elif message.text.lower() == "Клуб программистов":
        bot.send_message(message.chat.id, "салам всем вы самые лучшие", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "photo":
        photo = open('img/linux.jpg', 'rb')
        bot.send_photo(message.chat.id, photo )
    # else:
    #     bot.send_message(message.chat.id, "Я тебя не понял", parse_mode='html')


@bot.message_handler(content_types=['photo'])
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау крутое фото 😍')
    



    

@bot.message_handler(commands=['LinkedinBaizaka'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить мой linkedin сайт", url="https://www.linkedin.com/in/baizak-nadurbekov/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)
    
@bot.message_handler(commands=['palindrome_leetcode'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт palindrome leetcode", url="https://leetcode.com/problems/longest-palindrome/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт чтобы выпольнить задачку', reply_markup=markup)
    
@bot.message_handler(commands=['AbstractBaseUser'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт django AbstractBaseUser", url="https://tproger.ru/translations/extending-django-user-model/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт учить Django AbstractBaseUser', reply_markup=markup)


@bot.message_handler(commands=['SQLRoadmap'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Роадмап по SQL ", url="https://habr.com/ru/articles/725414/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт посмотреть на roadmap sql', reply_markup=markup)

@bot.message_handler(commands=['CreatedUser'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посетить сайт django Created User", url="https://django.fun/ru/articles/tips/sozdanie-polzovatelskoj-modeli-user-v-django/"))
    bot.send_message(message.chat.id, 'Перейдите на сайт учить Django Created User', reply_markup=markup)




@bot.message_handler(commands=['AbstractUser_YouTube'])
def website(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton("Посмотреть YouTube видео", url="https://www.youtube.com/watch?v=sjJV0Ru1q0U&ab_channel=Denis"))
    bot.send_message(message.chat.id, 'Перейдите на YouTube канал', reply_markup=markup)
    

@bot.message_handler(commands=['help'])
def website(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    website = types.KeyboardButton('веб сайт')
    start = types.KeyboardButton('Start')
    markup.add(website, start)    
    bot.send_message(message.chat.id, 'Перейдите на сайт', reply_markup=markup)


bot.polling(none_stop=True)