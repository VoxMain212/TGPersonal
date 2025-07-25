from sqlalchemy.orm import DeclarativeBase, mapped_column, Mapped
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy import BigInteger, Integer, String, Text, DateTime, Date
from datetime import datetime, date


engine = create_async_engine("sqlite+aiosqlite:///db.sqlite")
async_session = async_sessionmaker(engine)


class Base(DeclarativeBase, AsyncAttrs):
    pass


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(BigInteger(), primary_key=True)


class Note(Base):
    __tablename__ = "notes"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    user_id: Mapped[int] = mapped_column(BigInteger())
    title: Mapped[str] = mapped_column(String(length=150))
    discription: Mapped[str] = mapped_column(Text())


class Todo(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)
    title: Mapped[str] = mapped_column(String(length=150))
    discription: Mapped[str] = mapped_column(Text())
    date_of_do: Mapped[date] = mapped_column(Date(), default=datetime.now().date())


class Remind(Base):
    __tablename__ = "reminds"

    id: Mapped[int] = mapped_column(Integer(), primary_key=True)

    title: Mapped[str] = mapped_column(String(length=150))
    discription: Mapped[str] = mapped_column(Text())
    date_use: Mapped[datetime] = mapped_column(DateTime())
    user_id: Mapped[int] = mapped_column(BigInteger())


async def start_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)