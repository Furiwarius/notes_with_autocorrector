from app.entities import Note
from app.database.cruds import NotesCRUD


class NoteManager():
    '''
    Сервисный слой для заметок
    '''

    note_crud = NotesCRUD()


    def new_note(self, account_id:int, note_name:str, note_text:str) -> None:
        '''
        Добавляет новую заметку
        '''

        note = Note(name=note_name,
                    text=note_text,
                    account_id=account_id)
        
        self.note_crud.add(note)