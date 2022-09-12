import logging
from aiogram import Dispatcher, Bot, executor, types

from config import TOKEN
from translate_func import translater

logging.basicConfig(level=logging.INFO,
                    filename='bot.log',
                    format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S')

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен!')

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Привет, {message.from_user.first_name}!')
    await bot.send_message(message.from_id, 'Это телеграм-бот, который переводит из кириллицы в латиницу.\n\nНапример, введите ФИО:')

@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await message.answer(f'Перевод:\n{translater(message.text)}')
    await bot.send_message(message.from_id, 'Введите сообщение:')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
