from app.database.cruds import AccountCRUD, NotesCRUD
from app.entities import Account, Note
import pytest


class TestDatabase():
    '''
    Класс для тестирования работы крудов
    '''

    @pytest.mark.asyncio
    async def test_add_account(self,  account:Account, acc_crud:AccountCRUD):
        '''
        Тестирование метода по добавлению аккаунта
        '''
        acc:Account = await acc_crud.add(account)
        assert acc.id
    

    @pytest.mark.asyncio
    async def test_get_account_by_login(self, account:Account, acc_crud:AccountCRUD):
        '''
        Тестирование метода по получения аккаунта по логину
        '''
        acc:Account = await acc_crud.add(account)
        assert acc.id
        
        acc_in_db:Account = await acc_crud.get_by_login(acc.login)
        assert acc_in_db.id==acc.id
    

    @pytest.mark.asyncio
    async def test_add_note(self, note:Note, note_crud:NotesCRUD):
        '''
        Тестирование метода по добавлению заметки
        '''
        new_note:Note = await note_crud.add(note)
        assert new_note.id


    @pytest.mark.asyncio
    async def test_get_notes(self, account_id:int, note:Note, note_crud:NotesCRUD):
        '''
        Тестирование метода по получению всех заметок пользователя
        '''
        new_note:Note = await note_crud.add(note)
        assert new_note.id

        notes = await note_crud.get_notes(acc_id=account_id)
        assert notes