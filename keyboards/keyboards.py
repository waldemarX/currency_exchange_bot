from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder
from lexicon.lexicon import LEXICON_RU
from services.sevices import available_currency


def buttons():
    currency_keyboard: list[KeyboardButton] = [
        KeyboardButton(text=str(i)) for i in available_currency
    ]

    builder = ReplyKeyboardBuilder()

    builder.row(*currency_keyboard, width=4)

    currency_keyboard: ReplyKeyboardMarkup = builder.as_markup(
        resize_keyboard=True
    )
    return currency_keyboard


def create_inline_kb(width: int,
                     *args: str,
                     last_btn: str | None = None,
                     **kwargs: str) -> InlineKeyboardMarkup:

    kb_builder = InlineKeyboardBuilder()

    buttons: list[InlineKeyboardButton] = []

    if args:
        for button in args:
            buttons.append(InlineKeyboardButton(
                text=LEXICON_RU[button] if button in LEXICON_RU else button,
                callback_data=button))
    if kwargs:
        for button, text in kwargs.items():
            buttons.append(InlineKeyboardButton(
                text=text,
                callback_data=button))

    kb_builder.row(*buttons, width=width)

    if last_btn:
        kb_builder.row(InlineKeyboardButton(
            text=last_btn,
            callback_data='last_btn'
        ))

    return kb_builder.as_markup()
