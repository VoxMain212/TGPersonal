from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder
from src.db.models import Note


base_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Заметки", callback_data="notes"),
        InlineKeyboardButton(text="Задачи", callback_data="todos")
    ]
])

note_manage_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Список заметок", callback_data="note_list")],
    [
        InlineKeyboardButton(text="Добавить заметку", callback_data="note_add")
    ]
])

note_confirm_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Подтвердить", callback_data="note_confirm"),
        InlineKeyboardButton(text="Отклонить", callback_data="note_cancel")
    ]
])

def create_note_kb(note_enum: enumerate[Note]):
    kb = InlineKeyboardBuilder()
    for pos, note in note_enum:
        text = f"{pos}. {note.title}"
        if len(text) > 30:
            text = text[:27]+"..."
        kb.button(text=text, callback_data=f"note_{note.id}")
    return kb.as_markup()


todos_manage_kb = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Добавить задачу", callback_data="todos_add"),
        InlineKeyboardButton(text="Список задач", callback_data="todos_list")
    ]
])