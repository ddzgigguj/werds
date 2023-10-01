from aiogram import types, Router
from aiogram.filters import Command
import random


picture_router = Router()


@picture_router.message(Command("picture"))
async def send_random_photo(message: types.Message):
    file = types.FSInputFile("images/richard.jpg")
    file2 = types.FSInputFile("images/emamen.jpg")
    file3 = types.FSInputFile("images/hm.jpg")
    file4 = types.FSInputFile("images/medic.jpg")
    file5 = types.FSInputFile("images/obamna.jpg")
    file6 = types.FSInputFile("images/papich.jpg")
    file7 = types.FSInputFile("images/rock.jpg")
    file8 = types.FSInputFile("images/skuf.jpg")
    file9 = file, file2, file3, file4, file5, file6, file7, file8
    random_photo = random.choice(file9)
    await message.answer_photo(random_photo)