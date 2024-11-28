from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Создать розыгрыш'),
                                      KeyboardButton(text='Мои розыгрыши')],
                                     [KeyboardButton(text='Добавить канал'),
                                      KeyboardButton(text='Поддержка')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пунк меню...')

# from app.handlers import lotteries as g
from app.handlers import lotteries_router
dp = Dispatcher(bot, storage=MemoryStorage())
dp.include_router(lotteries_router)

def create_lottery_keyboard(lotteries):  # lotteries is now an argument
    """Creates an inline keyboard with buttons for each lottery."""
    keyboard = []
    for lottery in lotteries:
        keyboard.append([InlineKeyboardButton(text=lottery['name'], callback_data=f"lottery_{lottery['id']}")])
    return InlineKeyboardMarkup(inline_keyboard=keyboard)


count = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='1'),
     InlineKeyboardButton(text='2', callback_data='2'),
     InlineKeyboardButton(text='3', callback_data='3')]])


myRG = create_lottery_keyboard(lotteries_router)


SRG = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Завершить', callback_data='finish')],
    [InlineKeyboardButton(text='Удалить', callback_data='delete')]])
