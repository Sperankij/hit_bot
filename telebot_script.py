import logging
import os
from random import choice
from dotenv import load_dotenv
import telebot
from telebot import types

from config import chopolakh_type

load_dotenv()  # Start reading data from .env file.
logging.basicConfig(level=logging.INFO)  # Start logging.

bot = telebot.TeleBot(os.getenv('TELEGRAM_BOT_API_KEY'))  # Bot api token init.


# Handler for /start command.
@bot.message_handler(commands=['start'])
def cmd_start(message: types.Message):
    answer = 'Для работы бота добавте его в группу как администратора с правами на удаления сообщений.\nПользуйтесь командой /hit'
    bot.send_message(message.chat.id, answer)


# Handler for /hit command.
@bot.message_handler(commands=['hit'])
def hit(message: types.Message):
    command_parts = message.text.split(maxsplit=1)
    hited_user = command_parts[1] if len(command_parts) > 1 else None
    user_id = message.from_user.id
    user = bot.get_chat_member(message.chat.id, user_id)
    if hited_user is not None:
        # Deletes the message to which the handler reacted
        bot.delete_message(message.chat.id, message.message_id)

        answer = f'{user.user.full_name} прописал {choice(chopolakh_type)}чеполах {hited_user}'
        bot.send_message(message.chat.id, answer)
    else:
        answer = 'Аргумент не указан.\nПринимаются сообщения такого типа:\n/hit <Имя> (лучше указывать в дательном падеже)'
        bot.send_message(message.chat.id, answer)


# Start polling
if __name__ == '__main__':
    bot.polling()
