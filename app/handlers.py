from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет!')
    await message.reply('Как дела?')


@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Вы нажали на кнопку помощи')


@router.message(F.text == 'У меня всё хорощо')
async def nice(message: Message):
    await message.answer('Я очень рад')
