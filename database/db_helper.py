from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession

from database.db_config import database_config
from database.base_model import Base


class DatabaseHelper:
    def __init__(self):
        self.engine = create_async_engine(
            url=database_config.db_url,
            echo=True
        )

        self.session_maker = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )

    async def get_session(self) -> AsyncSession:
        async with self.session_maker() as session:
            yield session
            await session.close()

    async def create_tables(self):
        async with self.engine.begin() as conn:
            # await conn.run_sync(Base.metadata.drop_all)
            await conn.run_sync(Base.metadata.create_all)


database_helper = DatabaseHelper()
