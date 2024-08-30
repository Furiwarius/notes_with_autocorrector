from app.database.cruds import AccountCRUD
from app.utilities import to_hash
from app.entities import Account
from app.errors.service_exc import LoginExist, IncorrectUserData



class AccountManager():
    '''
    Сервисный слой для аккаунтов
    Вызывает исключения в случае нарушений
    '''


    acc_crud = AccountCRUD()


    def new_user(self, login:str, password:str) -> Account:
        '''
        Добавление нового пользователя

        Возвращает класс Account с id 
        при удачном внесении в бд.
        '''

        acc = Account(login=to_hash(login),
                      password=to_hash(password))

        acc_in_db = self.acc_crud.get_by_login(login=acc.login)
        if acc_in_db:
            raise LoginExist
        
        acc = self.acc_crud.add(acc)

        return acc



    def exist_user(self, login:str, password:str) -> Account:
        '''
        Попытка входа за существующего пользователя
        '''

        acc = Account(login=to_hash(login),
                      password=to_hash(password))
        
        acc_in_db = self.acc_crud.get_by_login(login=acc.login)

        if acc_in_db is None or acc.password != acc_in_db.password:
            raise IncorrectUserData

        return acc_in_db