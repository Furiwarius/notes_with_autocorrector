from app.errors.base_exc import BaseApplicationException


class LoginExist(BaseApplicationException):
    '''
    Исключение, которое вызывается при
    попытке создать новый аккаунт с уже 
    существующим логином
    '''



class IncorrectUserData(BaseApplicationException):
    '''
    Исключение, которое вызывается,
    если введены переданы неверные данные при авторизации
    '''