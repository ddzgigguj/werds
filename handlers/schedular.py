from aiogram import Router, types
from aiogram.filters import Command
from bot import scheduler, bot
from datetime import datetime
from db.shopdb import select_users

scheduler_router = Router()

@scheduler_router.message()
async def remind_me():
    scheduler.add_job(
        send_reminder,
        "interval",
        seconds=4,
    )

async def send_reminder():
    users = select_users()
    for user in users:
        await bot.send_message(user, "Привет")