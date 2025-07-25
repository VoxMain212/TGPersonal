from src.db.models import Note, async_session
from sqlalchemy import select


async def db_get_notes(user_id: int):
    async with async_session() as session:
        notes = await session.scalars(select(Note).where(Note.user_id==user_id))
        return notes
    
async def db_add_note(data):
    async with async_session() as session:
        note = Note(**data)
        session.add(note)
        await session.commit()
