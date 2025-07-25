from aiogram.fsm.state import State, StatesGroup


class NoteState(StatesGroup):
    title = State()
    discription = State()
    confirm = State()