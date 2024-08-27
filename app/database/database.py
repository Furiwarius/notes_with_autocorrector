from sqlalchemy import create_engine, Engine
from app.settings import db_setting
from app.database.tables.base import Base
from sqlalchemy.orm import Session



class Database():
    '''
    База данных

    Имеет всего 1 экземпляр на все приложение
    '''
    # Переменная с именем БД
    database_name = db_setting.DATABASE_NAME


    _instance = None  # Приватное поле для хранения единственного экземпляра


    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance._new_engine()
            cls._instance._create_table()
        return cls._instance
    


    def __enter__(self) -> Session:
        self.__new__(self)
        with Session(autoflush=False, bind=self.engine) as db:
            self.session = db
            return self.session


    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if self.session:
            self.session.close()


    def _new_engine(self) -> Engine:
        '''
        Создание движка SQLalchemy
        '''
        # строка подключения
        mysql_database = f"postgresql+psycopg2://{db_setting.DATABASE_USER}:{db_setting.DATABASE_PASSWORD}@{db_setting.HOST}/{db_setting.DATABASE_NAME}"
        # создаем движок SqlAlchemy
        self.engine = create_engine(mysql_database, echo=False)



    def _create_table(self) -> None:
        '''
        Создание таблиц
        '''
        # создаем таблицы
        Base.metadata.create_all(bind=self.engine)