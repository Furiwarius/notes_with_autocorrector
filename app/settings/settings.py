import dotenv
import os
from functools import lru_cache


class DatabaseSetting():
    '''
    Настройки для базы данных
    '''

    @lru_cache
    def __init__(self) -> None:
        
        # имя пользователя БД
        self.DATABASE_USER = os.getenv("DATABASE_USER")
        # Имя тестовой БД
        self.DATABASE_SERVER = os.getenv("DATABASE_SERVER")
        # Имя рабочей бд
        self.DATABASE_NAME = os.getenv("DATABASE_NAME")
        # Пароль для доступа к бд
        self.DATABASE_PASSWORD = os.getenv("DATABASE_PASSWORD")
        # Хост на котором находится бд
        self.HOST = os.getenv("HOST")