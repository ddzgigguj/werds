from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from text1 import START_TEXT
from text2 import BUTTON_TEXT
from db.queries import save_question

start_router = Router()

@start_router.message(Command("start"))
async def hello(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
               IButton(text="Контакты", callback_data="contacts"),
               IButton(text="О нас", callback_data="about"),
               IButton(text="Наш сайт", url="https://google.com"),
               IButton(text="Подписаться", callback_data="podpis"),
            ],
       ]
    )
    await message.answer(START_TEXT, reply_markup=kb)


@start_router.callback_query(F.data == "podpis")
async def podpis(callback: types.CallbackQuery):
    save_question(callback.message.from_user.id)
    await callback.answer("Сохраненно")


@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(BUTTON_TEXT)


@start_router.callback_query(F.data == "contacts")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("911")