from app.entities import Note
from app.database.tables.essence import NotesTable, UserNotesTable
from app.utilities import convertertation
from app.database import Database



class NotesCRUD():
    '''
    Класс для работы с заметками пользователей в БД
    '''


    @convertertation
    def add(self, acc_id:int, note:Note) -> Note:
        '''
        Добавить заметку для аккаунта
        '''
        with Database() as db:

            db.add(note)     # добавляем в бд
            db.commit()     # сохраняем изменения
            
            new_user_note = UserNotesTable(account_id=acc_id,
                                           note_id=note.id)
            
            db.add(new_user_note)
            db.commit()

            result = db.query(NotesTable).order_by(NotesTable.id.desc()).first()

        return result
    


    @convertertation
    def get_notes(self, acc_id:int) -> None|list:
        '''
        Получить заметки аккаунта
        '''
        with Database() as db:
            notes = db.query(UserNotesTable).filter(UserNotesTable.account_id==acc_id).all()

            if notes: 
                    return [db.get(NotesTable, user_note.note_id) for user_note in notes]