from app.errors.base_exc import BaseException


class LoginExist(BaseException):
    '''
    Исключение, которое вызывается при
    попытке создать новый аккаунт с уже 
    существующим логином
    '''



class LoginNotExist(BaseException):
    '''
    Исключение, которое вызывается,
    если аккаунта не существует
    '''


class IncorrectPassword(BaseException):
    '''
    Исплючение, которое вызывается, если пароль
    не совпадает с сохраненным в бд
    '''