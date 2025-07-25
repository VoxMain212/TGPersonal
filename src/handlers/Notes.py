from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.filters import StateFilter
from src.db.notes import db_get_notes, db_add_note
from src.keyboards.Inline_keyboards import create_note_kb, note_manage_kb, note_confirm_kb
from src.states.Notes import NoteState


router = Router()


@router.callback_query(F.data == "notes")
async def handle_notes(call: CallbackQuery):
    await call.message.edit_text("Управление заметками", reply_markup=note_manage_kb)

@router.callback_query(F.data == "note_list")
async def note_list(call: CallbackQuery):
    await call.answer()
    notes = (await db_get_notes(call.from_user.id)).fetchall()
    if len(notes) != 0:
        message = "Список заметок:\n\n"
        note_enum = enumerate(notes, start=1)
        keyboard = create_note_kb(note_enum)
        for pos, note in enumerate(notes, start=1):
            message += f"{pos}. {note.title}\n"
        await call.message.edit_text(message, reply_markup=keyboard)
    else:
        await call.message.answer("Список заметок пуст", reply_markup=None)

@router.callback_query(F.data == "note_add")
async def add_note(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Заголовок заметки:")
    await state.set_state(NoteState.title)
    await call.answer()

@router.message(StateFilter(NoteState.title))
async def get_note_title(msg: Message, state: FSMContext):
    await state.update_data(title=msg.text)
    await msg.answer("Описание заметки:")
    await state.set_state(NoteState.discription)

@router.message(StateFilter(NoteState.discription))
async def get_note_discription(msg: Message, state: FSMContext):
    await state.update_data(discription=msg.text)
    message = f"""
{(await state.get_data())['title']}

{msg.text}

Подтвердить заметку?
"""
    await state.set_state(NoteState.confirm)
    await msg.answer(message, reply_markup=note_confirm_kb)

@router.callback_query(StateFilter(NoteState.confirm), F.data=="note_confirm")
async def confirm_note(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    data.setdefault("user_id", call.from_user.id)
    print(data)
    await state.clear()
    await db_add_note(data)
    await call.message.edit_text("Заметка добавлена")

@router.callback_query(StateFilter(NoteState.confirm), F.data=="note_cancel")
async def cancel_note(call: CallbackQuery, state: FSMContext):
    await call.message.edit_text("Заметка отменена")
    await state.clear()
