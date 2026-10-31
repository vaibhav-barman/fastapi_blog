from pathlib import Path

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from .config import settings

# 1. Dynamically calculate the absolute path to the project root folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 2. Create the database engine instance directly using the settings URL
engine = create_async_engine(settings.DATABASE_URL)

# 3. Configure the asynchronous session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 4. Keep the declarative base instance intact for your database models
class Base(DeclarativeBase):
    pass

# 5. Database context session dependency runner
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
