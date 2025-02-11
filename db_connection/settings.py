from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import  URL
from sqlalchemy import create_engine
from os import getenv
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.url = URL.create(drivername="postgresql",
                              username=getenv("POSTGRES_USER"),
                              host=getenv("POSTGRES_HOST"),
                              port=getenv("POSTGRES_PORT"),
                              database=getenv("POSTGRES_DB"),
                              password=getenv("POSTGRES_PASSWORD"))
    
settings = Settings()
