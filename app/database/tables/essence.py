from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy import Column, DateTime
from app.database.tables.base import Base
from sqlalchemy.sql import func



class AccountsTable(Base):
    '''
    Модель таблицы accounts
    '''
    __tablename__ = "accounts"

    login = Column(String(65), nullable=False, unique=True)
    password = Column(String(65), nullable=False)



class NotesTable(Base):
    '''
    Модель таблицы notes
    '''
    __tablename__ = "notes"

    name = Column(String(20), nullable=False)
    text = Column(String(100), nullable=False)
    start_date = Column(DateTime, default=func.now(), server_default=func.now(), nullable=False)
    update_date = Column(DateTime, default=func.now(), server_default=func.now(), onupdate=func.now())


class UserNotesTable(Base):
    '''
    Модель таблицы users_notes
    '''
    __tablename__ = "users_notes"

    account_id = Column(Integer, ForeignKey("accounts.id"), nullable=False)
    note_id = Column(Integer, ForeignKey("notes.id"), nullable=False)