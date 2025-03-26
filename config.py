import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent

load_dotenv(dotenv_path=BASE_DIR / ".env")


class Config:
    DEBUG: bool = False
    TESTING: bool = False
    #SQLALCHEMY_DATABASE_URI: str = os.getenv("URL_HW_5")
    SQLALCHEMY_DATABASE_URI: str = "sqlite:///my_hw_5_database.db"


class DevelopmentConfig(Config):
    DEBUG: bool = True



class ProductionConfig(Config):
    ...
