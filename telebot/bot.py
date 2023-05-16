import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram import types
from aiogram.filters import Command
from aiogram.filters import CommandObject
from aiogram import html
from datetime import datetime




# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6286824253:AAEx9FvYCexXauX71zhXjJGIbnt6Y3UAT7k", parse_mode="HTML")
# Диспетчер
dp = Dispatcher()

@dp.message(F.text)
async def echo_with_time(message: types.Message):
    # Получаем текущее время в часовом поясе ПК
    time_now = datetime.now().strftime('%H:%M')
    # Создаём подчёркнутый текст
    added_text = html.underline(f"Создано в {time_now}")
    # Отправляем новое сообщение с добавленным текстом
    await message.answer(f"{message.text}\n\n{added_text}", parse_mode="HTML")
    
@dp.message(Command("pop"))
async def any_message(message: types.Message):
    await message.answer("Сообщение <u>Привет</u>")
    await message.answer("Сообщение без <s>какой-либо разметки</s>", parse_mode=None)

@dp.message(Command("name"))
async def cmd_name(message: types.Message, command: CommandObject):
    # await message.answer(f"Привет, {html.bold(html.quote(command.args))}", parse_mode="HTML")

    if command.args:
        await message.answer(f"Привет, <b>{command.args}</b>")
    else:
        await message.answer("Пожалуйста, укажи своё имя после команды /name!")
        
# Хэндлер на команду /start
@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Добро пожаловать")
    
@dp.message(Command("Umar"))
async def cmd_test1(message: types.Message):
    await message.reply("Умар уялбайсынбы")

@dp.message(Command("answer"))
async def cmd_answer(message: types.Message):
    await message.answer("Это простой ответ")


@dp.message(Command("reply"))
async def cmd_reply(message: types.Message):
    await message.reply('Это ответ с "ответом"')
    
@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(-5371931544, emoji=DiceEmoji.DICE)



# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
    
