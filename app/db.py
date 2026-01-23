from sqlalchemy import Column, String, Text, DateTime, Uuid, func
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
import uuid
import datetime
from typing import AsyncGenerator
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from fastapi import Depends

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db?timeout=10")


class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTableUUID, Base):
   posts =  relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Uuid, primary_key=True, default=uuid.uuid4)
    caption = Column(Text)
    url = Column(String, nullable=False)
    file_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    file_id = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.utcnow)
    user_id = Column(Uuid, ForeignKey("user.id"),nullable=False)
    user = relationship("User", back_populates="posts")

engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)
