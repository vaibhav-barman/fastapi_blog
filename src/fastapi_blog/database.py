from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase
import os
from pathlib import Path

# 1. Dynamically calculate the absolute path to the project root folder
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# 2. Build the database connection URL string pointing to the root workspace
SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{BASE_DIR / 'blog.db'}"

# 3. Create the database engine instance
engine = create_async_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}, # Specific to SQLite; allows multi-thread connection sharing.
)

# 4. Configure the asynchronous session factory
AsyncSessionLocal = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

# 5. Keep the declarative base instance intact for your database models
class Base(DeclarativeBase):
    pass

# 6. Database context session dependency runner
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
