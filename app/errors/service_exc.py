from app.errors.base_exc import BaseApplicationException


class LoginExist(BaseApplicationException):
    '''
    Исключение, которое вызывается при
    попытке создать новый аккаунт с уже 
    существующим логином
    '''



class LoginNotExist(BaseApplicationException):
    '''
    Исключение, которое вызывается,
    если аккаунта не существует
    '''


class IncorrectPassword(BaseApplicationException):
    '''
    Исплючение, которое вызывается, если пароль
    не совпадает с сохраненным в бд
    '''