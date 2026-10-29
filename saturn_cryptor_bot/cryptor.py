#!/usr/bin/env python3
import os
import io
import telebot
from telebot import apihelper
from telebot.types import Message

TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN', '') #your token from BotFather

if not TOKEN:
    raise ValueError('Error: TELEGRAM_BOT_TOKEN environment variable is not set!')

bot = telebot.TeleBot(TOKEN)

#you can use cloudflare proxy if telegram is banned in your country
PROXY_URL = os.environ.get('TELEGRAM_PROXY_URL', '')
PROXY_FILE_URL = os.environ.get('TELEGRAM_PROXY_FILE_URL', '')

if PROXY_URL: apihelper.API_URL = PROXY_URL
if PROXY_FILE_URL: apihelper.FILE_URL = PROXY_FILE_URL

USER_KEYS = {}

def encrypt_text(text: str, key: str) -> str:
    crypted_chars = []
    key_lenth = len(key)
    if text.startswith('G# '):
        strings = text[3:].split()
        numbers = [int(string) for string in strings]
        for index, number in enumerate(numbers):
            key_char = key[index % key_lenth]
            crypted_char = chr(number ^ ord(key_char))
            crypted_chars.append(crypted_char)
            index += 1
        crypted_message = ''.join(crypted_chars)
    else:
        for index, char in enumerate(text):
            key_char = key[index % key_lenth]
            crypted_char = str(ord(char) ^ ord(key_char))
            crypted_chars.append(crypted_char)
            index += 1
        crypted_message = 'G# ' + ' '.join(crypted_chars)
    return crypted_message

def encrypt_file(file: io.BytesIO, key: str) -> io.BytesIO:
    file.seek(0)

    key_bytes = key.encode('utf-8')
    data = file.read()

    processed_data = bytearray()
    key_lenth = len(key_bytes)
    for index, byte in enumerate(data):
        key_byte = key_bytes[index % key_lenth]
        crypted_byte = byte ^ key_byte
        processed_data.append(crypted_byte)
    crypted_file = io.BytesIO(processed_data)

    crypted_file.seek(0)

    return crypted_file

@bot.message_handler(commands=['start', 'help'])
def main(message: Message):
    bot.send_message(message.chat.id, 'Hello! I am Saturn Cryptor. Set the master-key using "/key [master-key]" and send me any text or file and I will encrypt it via your master-key.')

@bot.message_handler(commands=['key'])
def key(message):
    if message.text is None:
        return

    parts = message.text.split(' ', 1)

    if len(parts) > 1:
        extracted_key = parts[1].strip()
        USER_KEYS[message.chat.id] = extracted_key
        bot.reply_to(message, 'Master-key set.')
    else:
        bot.reply_to(message, 'You should also write the master-key! As example: "/key qwerty123"')

@bot.message_handler(content_types=['text'])
def handle_text(message: Message):
    if message.text is not None:
        master_key = USER_KEYS.get(message.chat.id)
        if master_key:
            ciphered_text = encrypt_text(message.text, master_key)
            bot.reply_to(message, ciphered_text)
        else:
            bot.send_message(message.chat.id, 'Master-key not set. Set the master-key using "/key [master-key]".')

@bot.message_handler(content_types=['document'])
def handle_file(message: Message):
    if message.document is not None:
        master_key = USER_KEYS.get(message.chat.id)
        if master_key:
            status_message = bot.reply_to(message, 'Downloading and encrypting your file...')
            try:
                file_info = bot.get_file(message.document.file_id)
                downloaded_bytes = bot.download_file(file_info.file_path) #type: ignore

                input_file = io.BytesIO(downloaded_bytes)

                encrypted_file = encrypt_file(input_file, master_key)
                encrypted_file.name = message.document.file_name or 'encrypted_file'

                bot.send_document(message.chat.id, encrypted_file, reply_to_message_id=message.message_id, caption='Your encrypted file:')
                bot.delete_message(message.chat.id, status_message.message_id)
            except Exception as e:
                bot.reply_to(message, f'An error occured during encryption: {e}')
        else:
            bot.send_message(message.chat.id, 'Master-key not set. Set the master-key using "/key [master-key]".')

if __name__ == '__main__':
    print('Bot is running...')
    bot.infinity_polling()