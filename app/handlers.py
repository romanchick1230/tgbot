from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
import re
from datetime import datetime

import app.keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    text = State()
    count = State()
    data = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Благодорим за использование нашего бота.', reply_markup=kb.main)


@router.message(F.text == 'Поддержка')
async def support(message: Message):
    await message.answer('Для поддержки пишите админестратору бота - @Pronyakin_roman',
                         reply_markup=kb.main)


@router.message(F.text == 'Создать розыгрыш')
async def create(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer('Введте название розыгрыша.')


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.text)
    await message.answer('Введите текст в котором вы опишите условия розыгрыша,\n дату окончяния и кол-во победителей.')


@router.message(Register.text)
async def register_text(message: Message, state: FSMContext):
    await state.update_data(text=message.text)
    await state.set_state(Register.count)
    await message.answer('Выберите кол-во победителей.', reply_markup=kb.count)


@router.callback_query(Register.count, F.data == '1')
async def register_1(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count=1)
    await state.set_state(Register.data)
    await callback.message.answer('Введите Дату окончания розыгрыша.')

@router.callback_query(Register.count, F.data == '2')
async def register_2(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count=2)
    await state.set_state(Register.data)
    await callback.message.answer('Введите Дату окончания розыгрыша.')

@router.callback_query(Register.count, F.data == '3')
async def register_3(callback: CallbackQuery, state: FSMContext):
    await state.update_data(count=3)
    await state.set_state(Register.data)
    await callback.message.answer('Введите дату окончания розыгрыша в формате YYYY-MM-DD.')


@router.message(Register.data, F.text)
async def register_data(message: Message, state: FSMContext):
    date_string = message.text
    try:
        if not re.match(r'\d{4}-\d{2}-\d{2}', date_string):
            raise ValueError("Неверный формат даты. Используйте формат YYYY-MM-DD")

        date_object = datetime.strptime(date_string, '%Y-%m-%d')
        await state.update_data(date=date_object)
        data = await state.get_data()
        await message.answer(f"Розыгрыш создан:\nНазвание: {data['name']}\nТекст: {data['text']}\nПобедителей: {data['count']}\nДата окончания: {date_object.strftime('%Y-%m-%d')}\nВыберите канал для публикации в разделе 'Мои розыгрыши'.")
        await state.clear()
    except ValueError as e:
        await message.answer(f"Ошибка: {e}. Пожалуйста, введите корректную дату в формате YYYY-MM-DD.")
    except Exception as e:
        await message.answer(f"Произошла неизвестная ошибка: {e}")


@router.message(F.text == 'Мои розыгрыши')
async def catalog(message: Message):
    await message.answer('Выберите розыгрыш', reply_markup=kb.myRG)


@router.message(F.text == 'Добавить канал')
async def catalog(message: Message):
    await message.answer('Добавьте бота в качевстве админестратора канала')

@router.callback_query(F.data == 'RGname')
async def RGname(callback: CallbackQuery):
    await callback.answer('Вы выбрали', show_alert=True)
    await callback.message.answer('Вы выбрали', reply_markup=kb.SRG)
