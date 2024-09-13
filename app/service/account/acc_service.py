from app.database.cruds import AccountCRUD
from app.utilities import to_hash
from app.entities import Account
from app.errors.service_exc import LoginExist, IncorrectUserData



class AccountManager():
    '''
    Сервисный слой для аккаунтов
    Вызывает исключения в случае нарушений
    '''


    acc_crud:AccountCRUD = AccountCRUD()


    async def new_user(self, login:str, password:str) -> Account:
        '''
        Добавление нового пользователя

        Возвращает класс Account с id 
        при удачном внесении в бд.
        '''

        acc:Account = Account(login=await to_hash(login),
                      password=await to_hash(password))

        acc_in_db:Account = await self.acc_crud.get_by_login(login=acc.login)
        if acc_in_db:
            raise LoginExist
        
        acc:Account = await self.acc_crud.add(acc)

        return acc



    async def exist_user(self, login:str, password:str) -> Account:
        '''
        Попытка входа за существующего пользователя
        '''

        acc:Account = Account(login=await to_hash(login),
                      password=await to_hash(password))
        
        acc_in_db:Account = await self.acc_crud.get_by_login(login=acc.login)

        if acc_in_db is None or acc.password != acc_in_db.password:
            raise IncorrectUserData

        return acc_in_db