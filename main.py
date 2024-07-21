import asyncio
import logging
import os
from random import choice

from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command, CommandObject
from dotenv import load_dotenv

from config import chopolakh_type

load_dotenv()   # Start reading data from .env file.
logging.basicConfig(level=logging.INFO)    # Start logging.

bot = Bot(token=os.getenv('TELEGRAM_BOT_API_KEY'))    # Bot api token init.
dp = Dispatcher()


# Handler for /start command.
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('hit_bot is work')


# Handler for /hit command.
@dp.message(Command('hit'))
async def hit(message: types.Message, command: CommandObject):
    hited_user = command.args
    user_id = message.from_user.id
    user = await bot.get_chat_member(chat_id=message.chat.id, user_id=user_id)
    if hited_user is not None:
        # Deletes the message to which the handler reacted
        await bot.delete_message(chat_id=message.chat.id,
            message_id=message.message_id)

        answer = f'{user.user.full_name} прописал {choice(chopolakh_type)}чеполах {hited_user}'
        await message.answer(answer)
    else:
        answer = 'Аргумент не указан.\nПринимаются сообщения такого типа:\n/hit <Имя> (лучше указывать в дательном падеже)'
        await message.answer(answer)


# Start new updates polling process.
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
