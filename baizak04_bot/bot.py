import telebot
from telebot import types
bot = telebot.TeleBot('6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY')

@bot.message_handler(commands=['starttwo'])
def starttwo(message):
    bot.send_message(message.chat.id,  'Привет Я ваш персональный бот 😊 Чем могу помочь')
    
@bot.message_handler(commands=['id'])
def starttwo(message):
    bot.send_message(message.chat.id, message.chat.id)
    
    
@bot.message_handler(commands=['Псевдоним'])
def starttwo(message):
    bot.send_message(message.chat.id, str(message.from_user.username))
     

    
@bot.message_handler(commands=['Имя'])
def starttwo(message):
    bot.send_message(message.chat.id, str(message.from_user.first_name))
     
def salam(message):
    return message.text == "Салам алейкум"

@bot.message_handler(func=salam)
def start(message):
    bot.reply_to(message, 'Ваалейкум салам. Мой хозяин занят на данный момент')

def hwo_baizak(message):
    return message.text == "Кто твой создатель?"

@bot.message_handler(func=hwo_baizak)
def hwo(message):
    bot.reply_to(message, 'Мой создатель <strong>Байзак </strong> 😎', parse_mode='html')

def salam(message):
    return message.text == "Привет"

@bot.message_handler(func=salam)
def start(message):
    bot.reply_to(message, 'Привет дорогуша')

def jan(message):
    return message.text == "Жан"

@bot.message_handler(func=jan)
def jan(message):
    bot.reply_to(message, 'оуу жаным угуп жатам 😊')
    
def good_morning(message):
    return message.text == "Доброе утро жан"

@bot.message_handler(func=good_morning)
def good_morning(message):
    bot.reply_to(message, 'Доброе ❤️')
    

def what(message):
    return message.text == "Чем ты занимаешься?"

@bot.message_handler(func=what)
def what(message):
    bot.reply_to(message, 'Лежу \n думаю что-то сделать с тобой ')
    
    
def hwo(message):
    return message.text == "Кто ты?"

@bot.message_handler(func=hwo)
def hwo(message):
    bot.reply_to(message, 'Я помощьник хозяина Байзака ')
    
    
def hwo(message):
    return message.text == "Ты моё солнце?"

@bot.message_handler(func=hwo)
def hwo(message):
    bot.reply_to(message, '<strong>Нет</strong>', parse_mode='html')
    
def hwo_two(message):
    return message.text == "Как дела?"

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

# @bot.message_handler(regexp=r'[0-9]+')
# def sum_one(message):
    # bot.send_message(message.chat.id, 'Ты что шитать не умеешь \n Научис шитать')

@bot.message_handler(commands=['itspace'])
def itspace(message):
    bot.send_message(message.chat.id, '<i>itspace</i>',parse_mode='html')
     
     
@bot.message_handler(commands=['button'])
def button(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 = types.KeyboardButton(text='кнопка один')
    btn2 = types.KeyboardButton(text='кнопка два')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'кнопки пока не работает', reply_markup=kb)


@bot.message_handler(commands=['links'])
def button_one(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn_one = types.InlineKeyboardButton(text='ссылка на гитхаб', url='https://github.com/Baizak04')
    btn_two = types.InlineKeyboardButton(text='ссылка на instagram', url='https://www.instagram.com/nadurbekov_144/')
    kb.add(btn_one, btn_two)
    bot.send_message(message.chat.id, 'ссылки 🤭', reply_markup=kb)

@bot.message_handler(commands=['photo1'])
def photo1(message):
    file = open('photo1.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Фото для ноутбука')

@bot.message_handler(commands=['photo2'])
def photo2(message):
    file = open('photo2.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, 'второе фото для ноутбука')

@bot.message_handler(commands=['photo3'])
def photo3(message):
    file = open('photo3.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'третое фото для ноутбука')

@bot.message_handler(commands=['photo_anime'])
def photo_anime1(message):
    file = open('photo_anime1.jpeg', 'rb')
    bot.send_photo(message.chat.id, file, 'Фото для аниме')


@bot.message_handler(commands=['switch'])
def switch(message):
    kb = types.InlineKeyboardMarkup()
    switch = types.InlineKeyboardButton(text='Выбрат чат', switch_inline_query='Тур эй сасыбай 😂😂😂')
    kb.add(switch)
    bot.send_message(message.chat.id, 'Сообщение', reply_markup=kb)

@bot.message_handler(commands=['callback'])
def callback(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    btn = types.InlineKeyboardButton(text='Салам', callback_data='btn1')
    btn1 = types.InlineKeyboardButton(text='Ваалейкум', callback_data='btn2')
    kb.add(btn, btn1)
    bot.send_message(message.chat.id, 'выбери что-то из них', reply_markup=kb)
    
@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        kb = types.InlineKeyboardMarkup(row_width=1)
        btn = types.InlineKeyboardButton(text='алейкум', callback_data='btn2')
        btn1 = types.InlineKeyboardButton(text='салам', callback_data='btn1')
        kb.add(btn, btn1)
        bot.edit_message_text(chat_id=callback.message.chat.id, message_id=callback.message.id, text='хихих 😂 \n Предупреждения!!! дальше ничего не нажимай', reply_markup=kb)    

@bot.message_handler(commands=['swit'])
def switch(message):
    markup = types.InlineKeyboardMarkup()
    url = types.InlineKeyboardButton(text='URL', url='https://www.edx.org/')
    switch = types.InlineKeyboardButton(text='Swit', switch_inline_query='hello 👨🏻‍💻')
    callback = types.InlineKeyboardButton(text='Callback', callback_data='hello')
    markup.add(url, switch, callback)
    bot.send_message(message.chat.id, 'Сообщение 👨🏻‍💻', reply_markup=markup)

bot.polling()


bot.polling()

bot.polling()