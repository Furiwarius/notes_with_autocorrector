from dataclasses import dataclass


@dataclass
class Note():
    '''
    Заметка 
    '''

    id: int = None
    # название заметки
    name: str = None
    # содержание заметки
    text: str = None