from src.db.models import User, async_session
from sqlalchemy import select


async def check_user(user_id: int) -> bool:
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.id==user_id))
        if user:
            return True
        return False
    
async def reg_user(user_id: int):
    async with async_session() as session:
        user = User(id=user_id)
        session.add(user)
        await session.commit()
