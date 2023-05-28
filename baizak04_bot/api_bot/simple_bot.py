import telebot
from telebot import types

token = '6226915086:AAEN1Sr9j2RJnfrZrGXZKBkdEQwPQ7LoOEY'
bot = telebot.TeleBot(token)
photo_url = 'https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.wallpaperflare.com%2Fblack-haired-girl-anime-wallpaper-twintails-monochrome-black-hair-wallpaper-avg&psig=AOvVaw0PwbWNOOywrp0ziow8mLLB&ust=1685345258556000&source=images&cd=vfe&ved=0CBEQjRxqFwoTCMDnj76-l_8CFQAAAAAdAAAAABAE'
@bot.message_handler(commands=['starttwo'])
def hello(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
    keyboard.add(types.KeyboardButton('Отправить картинку'), types.KeyboardButton('Отправить файл'))
    keyboard.add(types.KeyboardButton('Ответить на вопрос'))
    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name}!', reply_markup=keyboard)
    
@bot.message_handler(content_types=['text'])
def main_menu(message):
    # if message.text == 'Отправить картинку':
    #     bot.send_photo(message.chat.id, photo=photo_url, caption='Аниме девочка')
    if message.text == 'Отправить файл':
        f = open('api_bot/txt/new.txt', 'rb')
        bot.send_document(message.chat.id, document=f, caption='Очень фажный файл про любовь \n читай')
    elif message.text == 'Ответить на вопрос':
        inlinekeyboard = types.InlineKeyboardMarkup()
        inlinekeyboard.add(types.InlineKeyboardButton('2', callback_data=2))
        inlinekeyboard.add(types.InlineKeyboardButton('4', callback_data=4))
        inlinekeyboard.add(types.InlineKeyboardButton('5', callback_data=5))
        bot.send_message(message.chat.id, '2+2=?', reply_markup=inlinekeyboard)
        


@bot.callback_query_handler(func=lambda call: True)
def get_answer(call):
    if call.data == '4':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.id, text='вы ответили верно!')
    else:
        bot.send_message(call.message.chat.id, "Ответ неверный, попоробуйте снова")

bot.polling(none_stop=True)