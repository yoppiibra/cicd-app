"""
This module sets up the ML model configuration.

It utilizes Pydantic's BaseSettings for configuration management,
allowing settings to be read from environments variable and a .env file.
"""

from pydantic import DirectoryPath
from pydantic_settings import BaseSettings, SettingsConfigDict


class ModelSettings(BaseSettings):
    """
    ML model configuration settings for application,

    Attribute:
    model_config (SettingsConfigDict): Model config, loaded from .env file.
    model_path (str): Filesystem path to the model.
    model_name (str): Name of the model.
    """
    model_config = SettingsConfigDict(
        env_file='config/.env',
        env_file_encoding='utf-8',
        extra='ignore',
    )

    model_path: DirectoryPath
    model_name: str


model_settings = ModelSettings()
