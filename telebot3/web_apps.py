# Itspace_kg Telegram Bot

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6287454351:AAE4VdG2Fp0Pj0P8u4HIPegkldIi9T0_G8Q')
dp = Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб сайт', web_app=WebAppInfo(url='https://itproger.com/')))
    await message.answer('Привет, кто-то', reply_markup=markup)



executor.start_polling(dp)