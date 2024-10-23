from pydantic_settings import BaseSettings, SettingsConfigDict


class Config(BaseSettings):
    model_config = SettingsConfigDict(
        validate_assignment=True, env_prefix="", env_ignore_empty=True
    )

    DATABASE_URL: str = "sqlite+aiosqlite:///:memory:"


config = Config()

__all__ = ("config",)
