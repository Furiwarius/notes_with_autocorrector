from sqlalchemy import String, Integer, ForeignKey, Text
from sqlalchemy import Column, DateTime
from app.database.tables.base import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class NotesTable(Base):
    '''
    Модель таблицы notes
    '''
    __tablename__ = "notes"

    name = Column(String(20), nullable=False)
    text = Column(Text, nullable=False)
    start_date = Column(DateTime, default=func.now(), server_default=func.now(), nullable=False)
    update_date = Column(DateTime, default=func.now(), server_default=func.now(), onupdate=func.now())
    account_id = Column(Integer, ForeignKey("accounts.id"))
    
    account = relationship("AccountsTable", back_populates="notes")



class AccountsTable(Base):
    '''
    Модель таблицы accounts
    '''
    __tablename__ = "accounts"

    login = Column(String(65), nullable=False, unique=True)
    password = Column(String(65), nullable=False)
    notes = relationship("NotesTable", back_populates="account", lazy="joined")