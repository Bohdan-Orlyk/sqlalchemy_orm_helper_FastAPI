from pydantic_settings import BaseSettings


class DatabaseConfig(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///practise.db.sqlite3"


database_config = DatabaseConfig()
