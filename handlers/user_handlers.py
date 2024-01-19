from aiogram import F, Bot, Router
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.filters import Command, CommandStart
from lexicon.lexicon import LEXICON_RU
from keyboards.keyboards import currency_keyboard, data
from services.sevices import get_currency

router = Router()


@router.message(CommandStart())
async def process_start_command(message: Message):
    await message.answer(text=LEXICON_RU['/start'])


@router.message(Command(commands='help'))
async def process_help_command(message: Message):
    await message.answer(text=LEXICON_RU['/help'])


@router.message(Command(commands='currency'))
async def get_currency_list(message: Message):
    await message.answer(
        text=LEXICON_RU['valute'],
        reply_markup=currency_keyboard
    )


@router.message(F.text.in_(data['Valute']))
async def get_currency_cost(message: Message):
    currency, price = get_currency(message.text)
    await message.answer(
        text=f'{LEXICON_RU["exchange"]} {currency} --> {price} рублей',
        reply_markup=ReplyKeyboardRemove()
    )


@router.message(Command(commands='delmenu'))
async def del_main_menu(message: Message, bot: Bot):
    await bot.delete_my_commands()
    await message.answer(text='Кнопка "Menu" удалена')
