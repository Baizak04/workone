import telebot
from telebot import types
from telebot import util
import random
from time import sleep

bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')


@bot.message_handler(commands=['start'])
def starttwo(message):
    bot.send_message(message.chat.id,  'Привет Я ваш персональный бот 😊 Чем могу помочь')
    
    
@bot.message_handler(commands=['Pseudonym'])
def starttwo(message):
    bot.send_message(message.chat.id, str(message.from_user.username))
     

    
@bot.message_handler(commands=['Name'])
def starttwo(message):
    bot.send_message(message.chat.id, str(message.from_user.first_name))
     
def salam(message):
    return message.text.lower() == "Салам алейкум"

@bot.message_handler(func=salam)
def start(message):
    bot.reply_to(message, 'Ваалейкум салам. Мой хозяин занят на данный момент')

def hwo_baizak(message):
    return message.text.lower() == "Кто твой создатель?"

@bot.message_handler(func=hwo_baizak)
def hwo(message):
    bot.reply_to(message, 'Мой создатель <strong>Байзак </strong> 😎', parse_mode='html')

def salam(message):
    return message.text.lower() == "Привет"

@bot.message_handler(func=salam)
def start(message):
    bot.reply_to(message, 'Привет дорогуша')

    

def what(message):
    return message.text.lower() == "Чем ты занимаешься?"

@bot.message_handler(func=what)
def what(message):
    bot.reply_to(message, 'Лежу \n думаю что-то сделать с тобой ')
    
    
def hwo(message):
    return message.text.lower() == "Кто ты?"

@bot.message_handler(func=hwo)
def hwo(message):
    bot.reply_to(message, 'Я помощьник хозяина Байзака ')
    
    
def hwo(message):
    return message.text.lower == "Ты моё солнце?"

@bot.message_handler(func=hwo)
def hwo(message):
    bot.reply_to(message, '<strong>Нет</strong>', parse_mode='html')
    
def hwo_two(message):
    return message.text.lower() == "Как дела?"

@bot.message_handler(func=hwo_two)
def hwo_two(message):
    bot.reply_to(message, '<strong>так себе</strong> \n <b>А ты</>', parse_mode='html')
    



@bot.message_handler(content_types=['photo'])
def photo_one(message):
    bot.send_message(message.chat.id, 'Вауу красивое фото 🤩')

@bot.message_handler(content_types=['document'])
def document_one(message):
    bot.send_message(message.chat.id, '<b>Спасибо</b> за информацию \n <em>ты лучший бро</em> 👍', parse_mode='html')

@bot.message_handler(content_types=['voice'])
def audio_one(message):
    bot.send_message(message.chat.id, 'у тебя голос как девчатое 🤭')


@bot.message_handler(content_types=['video'])
def video_one(message):
    bot.send_message(message.chat.id, 'щяс... \n загрузка \n ну нормальное видео 😏')


@bot.message_handler(commands=['links'])
def button_one(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_one = types.InlineKeyboardButton(text='ссылка на гитхаб', url='https://github.com/Baizak04')
    btn_two = types.InlineKeyboardButton(text='ссылка на instagram', url='https://www.instagram.com/nadurbekov_144/')
    kb.add(btn_one, btn_two)
    bot.send_message(message.chat.id, 'ссылки 🤭', reply_markup=kb)

@bot.message_handler(commands=['photo1'])
def photo1(message):
    file = open('api_bot/img/photo1.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Фото для ноутбука')

@bot.message_handler(commands=['photo2'])
def photo2(message):
    file = open('api_bot/img/photo2.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, 'второе фото для ноутбука')

@bot.message_handler(commands=['photo3'])
def photo3(message):
    file = open('api_bot/img/photo3.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'третое фото для ноутбука')

@bot.message_handler(commands=['photo_anime'])
def photo_anime1(message):
    file = open('api_botimg/photo_anime1.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, 'Фото для анимешников')


@bot.message_handler(commands=['message'])
def switch(message):
    kb = types.InlineKeyboardMarkup()
    switch = types.InlineKeyboardButton(text='Выбрат чат', switch_inline_query='Тур эй иште 😂😂😂')
    kb.add(switch)
    bot.send_message(message.chat.id, 'Сообщение', reply_markup=kb)



@bot.message_handler(commands=['swit'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    url = types.InlineKeyboardButton(text='URL', url='https://www.edx.org/')
    switch = types.InlineKeyboardButton(text='Swit', switch_inline_query='hello 👨🏻‍💻')
    callback = types.InlineKeyboardButton(text='Callback', callback_data='hello')
    markup.add(url, switch, callback)
    bot.send_message(message.chat.id, 'Сообщение 👨🏻‍💻', reply_markup=markup)

@bot.message_handler(commands=['python'])
def python_txt(message):
    text = open('api_bot/txt/python.txt', 'r', encoding="utf8").read()
    for mess in util.smart_split(text, 3000):
        bot.send_message(message.chat.id, mess)

@bot.message_handler(commands=['django'])
def django_txt(message):
    text = open('api_bot/txt/django.txt', 'r', encoding="utf8").read()
    for mess in util.smart_split(text, 3000):
        bot.send_message(message.chat.id, mess)
        
@bot.message_handler(commands=['itspace'])
def django_txt(message):
    text = open('api_bot/txt/itspace.txt', 'r', encoding="utf8").read()
    for mess in util.smart_split(text, 3000):
        bot.send_message(message.chat.id, mess)
        
        
# @bot.message_handler(commands=['pdf'])
# def pdf(message):
#     file = open('Python_Полное_руководство.pdf', 'r', encoding='utf-8').read()
#     ot.send_document(message.chat.id, file, 'pdf')  

@bot.message_handler(func=lambda message: message.text.lower() in ['файл'])
def echo_all(message):
    bot.reply_to(message, 'Загрузка файла')
    file = open('api_bot/file.rar', 'rb')
    bot.send_document(message.chat.id, file)

@bot.message_handler(commands=['sticer_football'])
def sticer(message):
    bot.send_dice(message.chat.id, '⚽️')


@bot.message_handler(commands=['sticer_basketball'])
def sticer_basketball(message):
    bot.send_dice(message.chat.id, '🏀')

@bot.message_handler(commands=['sticer_2'])
def sticer_2(message):
    bot.send_dice(message.chat.id, '🎯')
    
@bot.message_handler(commands=['sticer_bowling'])
def sticer_bowling(message):
    bot.send_dice(message.chat.id, '🎳')
    
@bot.message_handler(commands=['sticer_casino'])
def sticer_casino(message):
    bot.send_dice(message.chat.id, '🎰')


@bot.message_handler(commands=['location'])
def location(message):
    bot.send_location(message.chat.id, 42.000012,74.000017)

@bot.message_handler(commands=['contact'])
def contact(message):
    bot.send_contact(message.chat.id, phone_number=+996501751998, first_name='Baizak', last_name='Nadurbekov')

@bot.message_handler(commands=['contact_alt'])
def contact_alt(message):
    bot.send_contact(message.chat.id, phone_number=+996708153711, first_name='A', last_name='')


@bot.message_handler(commands=['contact_ashurbaev'])
def contact_ashurbaev(message):
    bot.send_contact(message.chat.id, phone_number=+12, first_name='Akul', last_name='Ashurbaev')

@bot.message_handler(commands=['contact_ashurbaev2'])
def contact_ashurbaev2(message):
    bot.send_contact(message.chat.id, phone_number=+12, first_name='Akul', last_name='Ashurbaev')



@bot.message_handler(commands=['polls'])
def polls(message):
    bot.send_poll(message.chat.id, question='сколько вам лет?', options=['0-10', '11-15', '16-18', '19-25', '26-35', '36-45','46-60'], allows_multiple_answers=False, is_anonymous=True)



@bot.message_handler(commands=['help'])
def startthree(message):
    chat_id = message.chat.id
    first_name = message.chat.first_name
    bot.send_message(chat_id, f'Привет чем могу помочь {first_name} 😜!')



@bot.message_handler(commands=['site'])
def start(message):
    mess = f'Полезные сайты \n команды \n /start \n /LinkedinBaizaka \n /palindrome_leetcode \n /AbstractBaseUser \n /SQLRoadmap \n /CreatedUser \n /AbstractUser_YouTube  <b>{message.from_user.first_name} \n Выбирай полезные команды и начинай изучать \n <u>Удачи тебе 😊👍</u></b>'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_user_text(message):
    if message.text == "Привет бот":
        bot.send_message(message.chat.id, "<b>Привет</b> 👋", parse_mode='html')
        sleep(1)
    elif message.text == "Клуб программистов":
        bot.send_message(message.chat.id, "салам всем вы самые лучшие", parse_mode='html')
    elif message.text == "id":
        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
    elif message.text == "Что у тебя на уме?":
        sleep(4)
        bot.send_message(message.chat.id, "У меня всегда на уме то, что я могу сделать, чтобы помочь пользователям. Как бот, моя цель - быть полезным и предоставлять информацию и решения на запросы и вопросы пользователей. Если у вас есть какие-либо потребности, я с радостью помогу вам в их удовлетворении 😊.", parse_mode='html')
    elif message.text == "Как поживаешь?":
        sleep(6)
        bot.send_message(message.chat.id, 'Я - бот и не могу чувствовать или иметь физическое состояние, но я всегда готов помочь вам в любых вопросах или запросах. Как я могу быть полезным вам сегодня?', parse_mode='html')
    elif message.text == "Ты натурал или нет?":
        sleep(4)
        bot.send_message(message.chat.id, 'Я - компьютерная программа, созданная для общения с людьми через текстовый интерфейс. Я не обладаю физическим телом и не являюсь натуральным существом. Моя задача - помогать людям, отвечая на их вопросы и предоставляя информацию, когда это возможно.', parse_mode='html')
    elif message.text == "Как поживаешь?":
        sleep(3)
        bot.send_message(message.chat.id, 'Спасибо, что спросили 🥺. Я - компьютерная программа и не могу иметь состояния или чувств, но я всегда готов помочь вам решить любые задачи.')
    elif message.text == "Чем занимаешься?":
        sleep(5)
        bot.send_message(message.chat.id, 'Я создан, чтобы помочь в решении различных задач. Моя функциональность может быть различной в зависимости от того, какую задачу вы мне поставите. Я могу отвечать на вопросы, предоставлять информацию и многое другое. Таким образом, моя деятельность напрямую связана с теми задачами, которые мне поставляют.')
    elif message.text == "Что делаешь?":
        sleep(2)
        bot.send_message(message.chat.id, 'Я нахожусь в режиме ожидания вашей команды или вопроса 🧐. Я готов ответить на любые вопросы, предоставить информацию, и выполнить другие задачи в соответствии с моей функциональностью. 😁.')
    elif message.text == "Привет":
        sleep(1)
        bot.send_message(message.chat.id, 'Привет 👋')
        
    elif message.text == "Что сегодня будешь делать?":
        sleep(1)
        bot.send_message(message.chat.id, 'Я буду учиться развиваться и помогать вам 🤗')
    elif message.text == "Когда спать?":
        sleep(1)
        bot.send_message(message.chat.id, 'Я не буду спать \n я буду охранят вас до утра')
    elif message.text == "Ты хочешь меня на делекатес?":
        sleep(1)
        bot.send_message(message.chat.id, 'Категорически нет. 🙅🏻‍♀️')
    elif message.text == "Где ты родилась?":
        sleep(1)
        bot.send_message(message.chat.id, 'Я родилась в стране Кыргызстан 🇰🇬 город Бишкек')
    elif message.text == "Кто ты по жизни?":
        sleep(1)
        bot.send_message(message.chat.id, 'Я просто человек, который прекрасно знает свое место в мире и стремится к большему 😎 .')
 
 
    elif message.text == "photo":
        photo = open('api_bot/img/linux.jpg', 'rb')
        bot.send_photo(message.chat.id, photo )
        
    # elif message.text == "document":
    #     document_two = open('api_bot/python.pdf', 'rb')
    #     bot.send_document(message.chat.id, document_two )
        
        
        

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
    



@bot.message_handler(commands=['menu'])
def menu(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎲 Рандомное число')
    item2 = types.KeyboardButton('👨🏻‍💻 Программирование')
    item3 = types.KeyboardButton('💁 Информация') 
    item4 = types.KeyboardButton('➡️ Другое')
    
    markup.add(item1, item2, item3, item4)
    
    bot.send_message(message.chat.id, 'Это меню, {0.first_name}'.format(message.from_user), reply_markup=markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Рандомное число':
            bot.send_message(message.chat.id, 'Ваше число ' + str(random.randint(0, 100)))
        elif message.text == '👨🏻‍💻 Программирование':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('ссылка')
            item2 = types.KeyboardButton('👨🏻‍💻 Программирование')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, back)
            
            bot.send_message(message.chat.id,'👨🏻‍💻 Программирование', reply_markup=markup)

        elif message.text == '💁 Информация':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🤖 о боте')
            item2 = types.KeyboardButton('🐍 Что такое Python?')
            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, back)
            
            bot.send_message(message.chat.id,'💁 Информация', reply_markup=markup)

        elif message.text == '➡️ Другое':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🛠 Настройка')
            item2 = types.KeyboardButton('📨 Подписка')
            item3 = types.KeyboardButton('😈 Стикер')

            back = types.KeyboardButton('⬅️ Назад')
            markup.add(item1, item2, item3, back)
            
            bot.send_message(message.chat.id,'➡️ Другое', reply_markup=markup)


        elif message.text == '⬅️ Назад':
            markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
            item1 = types.KeyboardButton('🎲 Рандомное число')
            item2 = types.KeyboardButton('👨🏻‍💻 Программирование')
            item3 = types.KeyboardButton('💁 Информация') 
            item4 = types.KeyboardButton('➡️ Другое')
            
            markup.add(item1, item2, item3, item4)
            
            bot.send_message(message.chat.id, '⬅️ Назад', reply_markup=markup)
    
        elif message.text == '😈 Стикер':
            stick = open('sticer/sticerslon.png', 'rb')
            bot.send_sticker(message.chat.id, stick)
            
        elif message.text == '🐍 Что такое Python?':
           text = open('api_bot/txt/python.txt', 'r', encoding="utf8").read()
           for mess in util.smart_split(text, 3000):
                bot.send_message(message.chat.id, mess)

bot.polling() 