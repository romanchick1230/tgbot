from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardMarkup, InlineKeyboardButton)

main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Создать розыгрыш'),
                                      KeyboardButton(text='Мои розыгрыши')],
                                     [KeyboardButton(text='Добавить канал'),
                                      KeyboardButton(text='Поддержка')]],
                           resize_keyboard=True,
                           input_field_placeholder='Выберите пунк меню...')


count = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='1', callback_data='1'),
     InlineKeyboardButton(text='2', callback_data='2'),
     InlineKeyboardButton(text='3', callback_data='3')]])


myRG = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Розыгрыш', callback_data='RGname')]])


SRG = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text='Завершить', callback_data='finish')]])