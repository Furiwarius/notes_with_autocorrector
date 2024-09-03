from app.entities import Note
from app.database.tables.essence import NotesTable, AccountsTable
from app.utilities import convertertation
from app.database import Database



class NotesCRUD():
    '''
    Класс для работы с заметками пользователей в БД
    '''


    @convertertation
    def add(self, note:Note) -> Note:
        '''
        Добавить заметку для аккаунта
        '''
        with Database() as db:

            db.add(note)     # добавляем в бд
            db.commit()     # сохраняем изменения

            result = db.query(NotesTable).order_by(NotesTable.id.desc()).first()

        return result
    


    @convertertation
    def get_notes(self, acc_id:int) -> None|list:
        '''
        Получить заметки аккаунта
        '''
        with Database() as db:
            acc = db.query(AccountsTable).filter(AccountsTable.id==acc_id).one_or_none()

            if acc.notes: 
                    return acc.notes