"""
This module sets up Database configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environments variable and a .env file.
"""

from sqlalchemy import create_engine
from pydantic_settings import BaseSettings, SettingsConfigDict


class DbSettings(BaseSettings):
    """
    Database configuration settings for application,

    Attribute:
    db_conn_str (str): Database connection string.
    """
    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    db_conn_str: str
    rent_apart_table_name: str


db_settings = DbSettings()

engine = create_engine(db_settings.db_conn_str)
