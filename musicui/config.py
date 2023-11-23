from confz import BaseConfig, FileSource, EnvSource, CLArgSource
from pydantic import SecretStr
from typing import ClassVar, Literal
from pathlib import Path


class WebConfig(BaseConfig):
    enabled: bool = False
    host: str = None
    port: int = None


class SpotifyConfig(BaseConfig):
    client_id: SecretStr
    client_secret: SecretStr
    redirect_uri: str


class Config(BaseConfig):
    config_folder_path: ClassVar[Path] = Path.home() / ".musicui"

    log_level: Literal[
        "NOTSET", "DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"
    ] = "INFO"
    web: WebConfig
    spotify: SpotifyConfig

    CONFIG_SOURCES = [
        FileSource(file=config_folder_path / "config.toml"),
        FileSource(file=config_folder_path / "secrets.toml"),
        EnvSource(allow_all=True, prefix="MUSICUI_"),
        CLArgSource(),
    ]
