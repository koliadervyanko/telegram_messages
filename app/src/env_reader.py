import os
from pathlib import Path

from dotenv import load_dotenv

from .dto.env_data_dto import EnvDataDto


class EnvReader:
    def __init__(self, path: str):
        self.path = path

    def get_env_data(self) -> EnvDataDto:
        self.load_env_file()
        hash = os.getenv("HASH")
        id = os.getenv("ID")
        return EnvDataDto(hash, int(id))

    def load_env_file(self):
        dotenv_path = Path(self.path)
        load_dotenv(dotenv_path=dotenv_path)
