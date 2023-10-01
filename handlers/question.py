from aiogram import types, Router, F
from aiogram.filters import  Command
from aiogram.types import(
    Message,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    KeyboardButton,

)
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


questions_router = Router()


class UserData(StatesGroup):
    name = State()
    sex = State()
    old = State()


@questions_router.message(F.text == "Отмена")
@questions_router.message(Command("cancel"))
async def cancel_questions(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Отменено", reply_markup=ReplyKeyboardRemove())


@questions_router.message(Command("ask"))
async def start_questions(message: Message, state: FSMContext):
    await state.set_state(UserData.name)
    kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="Отмена")]])
    await message.answer(
        "Для того чтобы задать вопрос, введите свои данные. Если хотите прекратить, нажмите кнопку 'Отмена'"
    )
    await message.answer("Введите ваше имя", reply_markup=kb)



@questions_router.message(F.text, UserData.name)
async def procces_sex(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(UserData.sex)
    kb = InlineKeyboardMarkup(
    inline_keyboard=[
    [
    IButton(text="Жен", callback_data="F"),
    IButton(text="Муж", callback_data="M"),
    ],
    ]
    )
    await message.answer("Выберите, и напишите ваш пол", reply_markup=kb)

    @questions_router.callback_query(F.data == "F")
    async def about(callback: types.CallbackQuery):
        await callback.answer()

        await callback.message.answer("")

    @questions_router.callback_query(F.data == "M")
    async def about(callback: types.CallbackQuery):
        await callback.answer()

        await callback.message.answer("")


@questions_router.message(F.text, UserData.sex)
async def process_email(message: Message, state: FSMContext):
    if message.text not in ['Муж', 'Жен']:

        await message.answer("Вы ввели неправильный пол")
    else:
        await state.update_data(sex=message.text)
        await state.set_state(UserData.old)
        await message.answer("Напишите ваш возраст")


@questions_router.message(F.text, UserData.old)
async def process_email(message: Message, state: FSMContext):
    n = int(message.text)
    if n > 100 or n < 1:
        await message.answer('Вы ввели неправильный возраст')
    else:
        await state.update_data(old=message.text)


    data = await state.get_data()

    await message.answer(
        "Спасибо. Вот ваши ответы:"
        f"Имя: {data['name']}, пол: {data['sex']}, ваш возраст: {data['old']}",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()