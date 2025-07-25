from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from src.handlers import Notes, base, Todos
from src.db.models import start_main
from config import TOKEN
import logging
import asyncio


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(storage=MemoryStorage())


async def main():
    await start_main()
    dp.include_routers(base.router, Notes.router, Todos.router)
    try:
        await dp.start_polling(bot)
    except:
        await bot.session.close()


if __name__ == "__main__":
    asyncio.run(main())
