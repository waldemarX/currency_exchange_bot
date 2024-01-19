from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from services.sevices import available_currency

currency_keyboard: list[KeyboardButton] = [
    KeyboardButton(text=str(i)) for i in available_currency
]

builder = ReplyKeyboardBuilder()

builder.row(*currency_keyboard, width=3)

currency_keyboard: ReplyKeyboardMarkup = builder.as_markup(
    resize_keyboard=True
)
