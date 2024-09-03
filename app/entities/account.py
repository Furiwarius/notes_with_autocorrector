from dataclasses import dataclass, field


@dataclass
class Account():
    '''
    Аккаунт 
    '''

    id: int = None
    # логин
    login: str = None
    # хешированный пароль
    password: str = None
    # Заметки
    notes: list[int] = field(default_factory=list)