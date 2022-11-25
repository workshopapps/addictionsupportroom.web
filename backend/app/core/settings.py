from pathlib import Path
from sys import modules

from pydantic import BaseSettings

BASE_DIR = Path(__file__).parent.resolve()
from aioredis import (
    from_url,
)


class Settings(BaseSettings):
    """Application settings."""

    ENV: str = "dev"
    HOST: str = "0.0.0.0"
    PORT: int = 8000
    BASE_URL_: str = f"https://{HOST}:{PORT}"
    # quantity of workers for uvicorn
    WORKERS_COUNT: int = 1
    # Enable uvicorn reloading
    RELOAD: bool = True
    # Database settings
    DB_HOST: str = "localhost"
    DB_PORT: int = 3306
    DB_USER: str = "root"
    DB_PASS: str = "admin123!"
    DB_BASE: str = "addictionsupportroom"
    DB_ECHO: bool = False
    REDIS_HOST: str = "redis-18482.c232.us-east-1-2.ec2.cloud.redislabs.com"  # os.getenv("REDIS_HOST")
    REDIS_PORT: str = 18482  # os.getenv("REDIS_PORT")
    REDIS_USERNAME: str = "default"  # os.getenv("REDIS_USERNAME")
    REDIS_PASSWORD: str = (
        "sEovbKUESFKny4fvg4IgzOIcdLwpZ6EZ"  # os.getenv("REDIS_PASSWORD")
    )

    #   import redis

    # r = redis.Redis(
    #   host='redis-18482.c232.us-east-1-2.ec2.cloud.redislabs.com',
    #   port=18482,
    #   password='sEovbKUESFKny4fvg4IgzOIcdLwpZ6EZ')

    "mysql+asyncmy://root:admin123!@localhost:3306/addictionsupportroom"

    @property
    def BASE_URL(self) -> str:
        return self.BASE_URL_ if self.BASE_URL_.endswith("/") else f"{self.BASE_URL_}/"

    @property
    def DB_URL(self) -> str:
        """
        Assemble Database URL from settings.

        :return: Database URL.
        """

        # return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_BASE}"
        return f"mysql+asyncmy://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_BASE}"

    class Config:
        env_file = f"{BASE_DIR}/.env"
        env_file_encoding = "utf-8"
        fields = {
            "BASE_URL_": {
                "env": "BASE_URL",
            },
        }

    async def redis_conn(self) -> str:
        """
        Assemble Redis URL from self.

        Args:
            self ( _obj_ ) : object reference.

        Returns:
            str: The assembled Redis host URL.
        """

        return await from_url(
            "redis://"
            + self.REDIS_USERNAME
            + ":"
            + self.REDIS_PASSWORD
            + "@"
            + self.REDIS_HOST
            + ":"
            + self.REDIS_PORT
            + "/"
            "0",
            decode_responses=True,
        )


class TestSettings(Settings):
    @property
    def DB_BASE(self):
        return f"{self.DB_BASE}_test"


if "pytest" in modules:
    settings = TestSettings()
else:
    settings = Settings()
