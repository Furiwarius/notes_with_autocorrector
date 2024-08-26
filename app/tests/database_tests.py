from app.database.cruds import AccountCRUD, NotesCRUD
from app.entities import Account, Note
import pytest


class TestDatabase():
    '''
    Класс для тестирования работы крудов
    '''


    @pytest.mark.asyncio
    def test_add_account(self,  account:Account, acc_crud:AccountCRUD):
        '''
        Тестирование метода по добавлению аккаунта
        '''
    


    @pytest.mark.asyncio
    def test_get_account_by_login(self, account:Account, acc_crud:AccountCRUD):
        '''
        Тестирование метода по получения аккаунта по логину
        '''
    


    @pytest.mark.asyncio
    def test_add_note(self, note:Note, note_crud:NotesCRUD):
        '''
        Тестирование метода по добавлению заметки
        '''
    


    @pytest.mark.asyncio
    def test_get_notes(self, account_id:int, note_crud:NotesCRUD):
        '''
        Тестирование метода по получению всех заметок пользователя
        '''
