from pydantic import Field
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DB_URL: str = Field(default='postgresql+asyncpg://workout1:workout1@localhost/workout1')


settings = Settings()