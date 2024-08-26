from app.database.cruds import AccountCRUD, NotesCRUD
from app.entities import Account, Note
import pytest


class TestDatabase():
    '''
    Класс для тестирования работы крудов
    '''


    def test_add_account(self,  account:Account, acc_crud:AccountCRUD):
        '''
        Тестирование метода по добавлению аккаунта
        '''
        acc:Account = acc_crud.add(account)
        assert acc.id
    


    def test_get_account_by_login(self, account:Account, acc_crud:AccountCRUD):
        '''
        Тестирование метода по получения аккаунта по логину
        '''
        acc:Account = acc_crud.add(account)
        assert acc.id
        
        acc_in_db:Account = acc_crud.get_by_login(acc.login)
        assert acc_in_db.id==acc.id
    


    def test_add_note(self, account_id:int, note:Note, note_crud:NotesCRUD):
        '''
        Тестирование метода по добавлению заметки
        '''
        new_note = note_crud.add(note=note, 
                                 acc_id=account_id)
        assert new_note.id



    def test_get_notes(self, account_id:int, note:Note, note_crud:NotesCRUD):
        '''
        Тестирование метода по получению всех заметок пользователя
        '''
        new_note = note_crud.add(note=note, 
                                 acc_id=account_id)
        assert new_note.id

        notes = note_crud.get_notes(acc_id=account_id)
        assert notes