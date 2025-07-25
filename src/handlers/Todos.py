from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from src.keyboards.Inline_keyboards import todos_manage_kb

router = Router()


@router.callback_query(F.data == "todos")
async def handle_todos(call: CallbackQuery):
    await call.answer()
    await call.message.edit_text("Управление списком дел", reply_markup=todos_manage_kb)

@router.callback_query(F.data == "todos_add")
async def add_todos(call: CallbackQuery):
    pass

@router.callback_query(F.data == "todos_list")
async def show_todos(call: CallbackQuery):
    pass
