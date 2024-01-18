from aiogram import F, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import my_keyboard, data

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='currency'))
async def process_valute(message: Message):
    await message.answer(
        text=LEXICON_RU['valute'],
        reply_markup=my_keyboard
    )


@router.message(F.text.in_(data['Valute']))
async def process_cost(message: Message):
    currency = data["Valute"][message.text]["Name"]
    price = str(data["Valute"][message.text]["Value"])
    await message.answer(
        text=f'{LEXICON_RU["exchange"]} {currency} --> {price} рублей',
        reply_markup=ReplyKeyboardRemove()
    )
