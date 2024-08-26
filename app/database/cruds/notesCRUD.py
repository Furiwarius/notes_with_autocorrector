from app.entities import Note
from app.database.tables.essence import NotesTable, UserNotesTable
from app.utilities import Converter
from app.database import Database



class NotesCRUD():
    '''
    Класс для работы с заметками пользователей в БД
    '''

    converter = Converter()


    def add(self, acc_id:int, note:Note) -> Note:
        '''
        Добавить заметку для аккаунта
        '''
        note = self.converter.conversion_to_table(note)
        with Database() as db:

            db.add(note)     # добавляем в бд
            db.commit()     # сохраняем изменения
            
            new_user_note = UserNotesTable(account_id=acc_id,
                                           note_id=note.id)
            
            db.add(new_user_note)
            db.commit()

            result = db.query(NotesTable).order_by(NotesTable.id.desc()).first()

        return self.converter.conversion_to_data(result)




    def get_notes(self, acc_id:int) -> None|list:
        '''
        Получить заметки аккаунта
        '''
        with Database() as db:
            notes = db.query(UserNotesTable).filter(UserNotesTable.account_id==acc_id).all()

            if notes: 
                    return [self.converter.conversion_to_data(db.get(NotesTable, user_note.id)) for user_note in notes]