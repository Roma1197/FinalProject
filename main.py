import requests
from bs4 import BeautifulSoup
from multiprocessing import Pool
import logging
from aiogram import Bot, Dispatcher, executor, types
from typing import List
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup, \
    InlineKeyboardButton


tuple1 = []
tuple2 = []
tuple3 = []
tuple4 = []
link1 = 'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/kiev/q-%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0/?currency=UAH&page' \
        '={0}'
link2 = 'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/kharkov/q-%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0/?currency=UAH' \
        '&page={0}'
link3 = 'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/lvov/q-%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0/?currency=UAH&page' \
        '={0}'
link4 = 'https://www.olx.ua/d/uk/nedvizhimost/kvartiry/odessa/q-%D0%BE%D1%80%D0%B5%D0%BD%D0%B4%D0%B0/?currency=UAH' \
        '&page={0}'


def rent(list):
    return list


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        for page in range(1, 3):
            url = link1.format(str(page))
            headers = {
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                               + 'AppleWebKit/537.36 (KHTML, like Gecko) '
                               + 'Chrome/109.0.0.0 Safari/537.36')
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                vacancies = soup.find_all('div', class_='css-1sw7q4x')
                for vacancy in vacancies:
                    date = vacancy.find('div', class_='css-u2ayx9')
                    if date is not None:
                        tuple1.append(date.text)
                    continue
            else:
                print('Cannot fetch the data')

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        for page in range(1, 3):
            url = link2.format(str(page))
            headers = {
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                               + 'AppleWebKit/537.36 (KHTML, like Gecko) '
                               + 'Chrome/109.0.0.0 Safari/537.36')
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                vacancies = soup.find_all('div', class_='css-1sw7q4x')
                for vacancy in vacancies:
                    date = vacancy.find('div', class_='css-u2ayx9')
                    if date is not None:
                        tuple2.append(date.text)
                    continue
            else:
                print('Cannot fetch the data')

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        for page in range(1, 3):
            url = link3.format(str(page))
            headers = {
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                               + 'AppleWebKit/537.36 (KHTML, like Gecko) '
                               + 'Chrome/109.0.0.0 Safari/537.36')
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                vacancies = soup.find_all('div', class_='css-1sw7q4x')
                for vacancy in vacancies:
                    date = vacancy.find('div', class_='css-u2ayx9')
                    if date is not None:
                        tuple3.append(date.text)
                    continue
            else:
                print('Cannot fetch the data')

if __name__ == '__main__':
    with Pool(processes=4) as pool:
        for page in range(1, 3):
            url = link4.format(str(page))
            headers = {
                'user-agent': ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                               + 'AppleWebKit/537.36 (KHTML, like Gecko) '
                               + 'Chrome/109.0.0.0 Safari/537.36')
            }
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                vacancies = soup.find_all('div', class_='css-1sw7q4x')
                for vacancy in vacancies:
                    date = vacancy.find('div', class_='css-u2ayx9')
                    if date is not None:
                        tuple4.append(date.text)
                    continue
            else:
                print('Cannot fetch the data')

API_TOKEN = '5867489731:AAEo7MEbMxgKgq0Jt6SErvbdCTpQatR76fk'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def process_command_1(message: types.Message):
    await message.reply("Виберіть місто", reply_markup=inline_kb_full)


# keyboards.py
inline_btn_1 = InlineKeyboardButton('Київ', callback_data='button1')
inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1)
inline_kb_full = InlineKeyboardMarkup(row_width=1).add(inline_btn_1)
inline_kb_full.add(InlineKeyboardButton('Харків', callback_data='btn2'))
inline_btn_3 = InlineKeyboardButton('Львів', callback_data='btn3')
inline_btn_4 = InlineKeyboardButton('Одеса', callback_data='btn4')
inline_kb_full.add(inline_btn_3, inline_btn_4)


@dp.callback_query_handler(lambda c: c.data == 'button1')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '\n\n'.join(tuple1))


@dp.callback_query_handler(lambda c: c.data == 'btn2')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '\n\n'.join(tuple2))


@dp.callback_query_handler(lambda c: c.data == 'btn3')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '\n\n'.join(tuple3))


@dp.callback_query_handler(lambda c: c.data == 'btn4')
async def process_callback_button1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, '\n\n'.join(tuple4))


@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
