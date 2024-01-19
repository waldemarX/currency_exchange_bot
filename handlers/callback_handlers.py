from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import create_inline_kb
from services.sevices import get_currency, available_currency

router = Router()


@router.message(Command(commands='currency'))
async def get_currency_list(message: Message):
    await message.answer(
        text=LEXICON_RU['valute'],
        reply_markup=create_inline_kb(3, *available_currency)
    )


@router.callback_query(F.data == 'else')
async def button_another_press(callback: CallbackQuery):
    await callback.message.edit_text(
        text=LEXICON_RU['choose_else'],
        reply_markup=create_inline_kb(3, *available_currency)
    )


@router.callback_query(F.data.in_(available_currency))
async def button_currency_press(callback: CallbackQuery):
    currency, price = get_currency(callback.data)
    await callback.message.edit_text(
        text=f'{LEXICON_RU["exchange"]} {currency} --> {price} рублей',
        reply_markup=create_inline_kb(1, 'else')
    )
