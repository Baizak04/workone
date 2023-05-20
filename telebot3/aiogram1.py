# Itspace_kg Telegram Bot



from aiogram import Bot, Dispatcher, executor, types

bot = Bot('6287454351:AAE4VdG2Fp0Pj0P8u4HIPegkldIi9T0_G8Q')

dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Салам')
    await message.answer('Салам я ваш персональный бот')


@dp.message_handler(commands=['привет', 'салам'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Салам')
    await message.answer('привет оуу жаным угуп жатам 😂')


@dp.message_handler(commands=['жестко'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Салам')
    await message.answer('еще жестче 😂')


@dp.message_handler(commands=['дану'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Салам')
    await message.answer('койшей')


@dp.message_handler(content_types=['photo'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Салам')
    await message.answer('Какая красивая фотка 😍')


# @dp.message_handler(content_types=['text'])
# async def start(message: types.Message):
#     # await bot.send_message(message.chat.id, 'Салам')
#     # await message.answer('На данный момент мой хозяин занят')
#     await message.reply('На данный момент мой хозяин занят')
#     # await message.answer_document('Спасибо данные')

@dp.message_handler(content_types=['document'])
async def start(message: types.Message):
    # await bot.send_message(message.chat.id, 'Салам')
    await message.answer('Спасибо за информация')
#


@dp.message_handler(commands=['info'])
async def info(message: types.Message):
    markup = types.InlineKeyboardMarkup(row_width=3)
    markup.add(types.InlineKeyboardButton('Site', url='https://www.linkedin.com/in/baizak-nadurbekov/'))
    markup.add(types.InlineKeyboardButton('Git cheetshet', url='https://habr.com/ru/companies/ruvds/articles/599929/'))
    markup.add(types.InlineKeyboardButton('umar', callback_data='umar'))
    await message.reply('Салам', reply_markup=markup)



@dp.callback_query_handler()
async def callback(call):
    await call.message.answer(call.data)

@dp.message_handler(commands=['reply'])
async def reply(message: types.Message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
    markup.add(types.KeyboardButton('Site'))   
    markup.add(types.KeyboardButton('Website'))  
    await message.answer('Салам хихи', reply_markup=markup)
 

executor.start_polling(dp)