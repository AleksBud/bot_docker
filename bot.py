import os
import logging
from aiogram import Dispatcher, Bot, executor, types

from translate_func import translater

logging.basicConfig(level=logging.INFO,
                    filename='logfile.log',
                    format='%(asctime)s: %(message)s',
                    datefmt='%H:%M:%S')

TOKEN = os.getenv('TOKEN')
# TOKEN='5706169432:AAENLIvrxYFBNV798j3b6roajYfIT_bYZMw'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

async def on_startup(_):
    print('Бот запущен!')

@dp.message_handler(commands=['start'])
async def starter(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await bot.send_message(message.from_id, f'Привет, {message.from_user.first_name}!')
    await bot.send_message(message.from_id, 'Это телеграм-бот, который переводит из кириллицы в латиницу.')
    await bot.send_message(message.chat.id, 'Перевод осуществляется в соответствии с [Приказом МИД по транслитерации](http://www.consultant.ru/document/cons_doc_LAW_360580/9eb761ae644ec1e283b3a50ef232330b924577cb/)', parse_mode='Markdown')
    await bot.send_message(message.from_id, 'Например, введите ФИО:')

@dp.message_handler()
async def echo(message: types.Message):
    logging.info(f'{message.from_user.full_name}: {message.text}')
    await message.answer(f'Перевод:\n{translater(message.text)}')
    await bot.send_message(message.from_id, 'Введите сообщение:')

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
