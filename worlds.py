# class Register(StatesGroup):
#     name = State()
#     age = State()
#     number = State()


# @router.message(CommandStart())
# async def cmd_start(message: Message):
#     await message.answer('Привет!', reply_markup=kb.main)
#     await message.reply('Как дела?')


# @router.message(Command('help'))
# async def cmd_help(message: Message):
#     await message.answer('Вы нажали на кнопку помощи')


# @router.message(F.text == 'Каталог')
# async def catalog(message: Message):
#     await message.answer('Выберите категорию товара', reply_markup=kb.catalog)


# @router.callback_query(F.data == 't-shirt')
# async def t_shirt(callback: CallbackQuery):
#     await callback.answer('Вы выбрали категорию', show_alert=True)
#     await callback.message.answer('Вы выбрали категорию футболки.')


# @router.message(Command('register'))
# async def register(message: Message, state: FSMContext):
#     await state.set_state(Register.name)
#     await message.answer('Введите ваше имя')


# @router.message(Register.name)
# async def register_name(message: Message, state: FSMContext):
#     await state.update_data(name=message.text)
#     await state.set_state(Register.age)
#     await message.answer('Введите ваш возраст')


# @router.message(Register.age)
# async def register_age(message: Message, state: FSMContext):
#     await state.update_data(age=message.text)
#     await state.set_state(Register.number)
#     await message.answer('Отправьте ваш номер телефона', reply_markup=kb.get_number)


# @router.message(Register.number, F.contact)
# async def register_number(message: Message, state: FSMContext):
#     await state.update_data(number=message.contact.phone_number)
#     data = await state.get_data()
#     await message.answer(f'Ваше имя: {data["name"]}\nВаш возраст: {data["age"]}\nНомер: {data["number"]}')
#     await state.clear()




# main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Каталог')],
#                                      [KeyboardButton(text='Корзина')],
#                                      [KeyboardButton(text='Контакты'),
#                                       KeyboardButton(text='О нас')]],
#                            resize_keyboard=True,
#                            input_field_placeholder='Выберите пунк меню...')


# catalog = InlineKeyboardMarkup(inline_keyboard=[
#     [InlineKeyboardButton(text='Футболки', callback_data='t-shirt')],
#     [InlineKeyboardButton(text='Красовки', callback_data='sneakers')],
#     [InlineKeyboardButton(text='Кепки', callback_data='cap')]])


# get_number = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Отправить номер',
#                                                            request_contact=True)]],
#                                  resize_keyboard=True)