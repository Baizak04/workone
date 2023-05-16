import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6286824253:AAEx9FvYCexXauX71zhXjJGIbnt6Y3UAT7k")
# Диспетчер
dp = Dispatcher()

# Хэндлер на команду /start
# @dp.message(Command("start"))
# async def cmd_start(message: types.Message):
#     await message.answer("Добро пожаловать")
    
# @dp.message(Command("Umar"))
# async def cmd_test1(message: types.Message):
#     await message.reply("Умар уялбайсынбы")

# @dp.message(Command("answer"))
# async def cmd_answer(message: types.Message):
#     await message.answer("Это простой ответ")


# @dp.message(Command("reply"))
# async def cmd_reply(message: types.Message):
#     await message.reply('Это ответ с "ответом"')
    
# @dp.message(Command("dice"))
# async def cmd_dice(message: types.Message, bot: Bot):
#     await bot.send_dice(-1001608650143, emoji=DiceEmoji.DICE)


@dp.message(Command("add_to_list"))
async def cmd_add_to_list(message: types.Message, mylist: list[int]):
    mylist.append(7)
    await message.answer("Добавлено число 7")


@dp.message(Command("show_list"))
async def cmd_show_list(message: types.Message, mylist: list[int]):
    await message.answer(f"Ваш список: {mylist}")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
