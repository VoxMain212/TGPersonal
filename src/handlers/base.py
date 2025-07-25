from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message
from src.db.users import check_user, reg_user
from src.keyboards.Inline_keyboards import base_kb


router = Router()


@router.message(CommandStart())
async def start(msg: Message):
    if await check_user(msg.from_user.id):
        await msg.answer("Добро пожаловать!\n\nЧто хотите?", reply_markup=base_kb)
    else:
        await reg_user(msg.from_user.id)
        await msg.answer("Добро пожаловать!\n\nЧто хотите?", reply_markup=base_kb)
