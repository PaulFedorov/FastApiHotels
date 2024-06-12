from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from config import settings

engine = create_async_engine(settings.DATABASE_URL)  # движок для передачи url

async_session_maker = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)

from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
