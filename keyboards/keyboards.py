from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import requests


data = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()

# Создаем список списков с кнопками
currency_keyboard: list[KeyboardButton] = [
    KeyboardButton(text=str(i)) for i in data['Valute']
]

# Инициализируем билдер
builder = ReplyKeyboardBuilder()

# Добавляем кнопки в билдер
builder.row(*currency_keyboard, width=3)

# Создаем объект клавиатуры, добавляя в него кнопки
currency_keyboard: ReplyKeyboardMarkup = builder.as_markup(resize_keyboard=True)
