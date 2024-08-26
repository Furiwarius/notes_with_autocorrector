from dataclasses import dataclass


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