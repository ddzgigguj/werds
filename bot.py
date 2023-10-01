from dotenv import load_dotenv
from os import getenv
from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler



load_dotenv()
token = getenv("TOKEN")
bot = Bot(token=token)

dp = Dispatcher()
scheduler = AsyncIOScheduler()

