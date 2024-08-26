from app.database import Database
from app.database.tables.essence import AccountsTable
from app.entities.account import Account
from app.utilities import Converter



class AccountCRUD():
    '''
    Класс для работы с аккаунтами пользователей в БД
    '''

    converter = Converter()


    def add(self, new_acc:Account) -> Account:
        '''
        Добавить аккаунт
        '''

        acc = self.converter.conversion_to_table(new_acc)
        with Database() as db:

            db.add(acc)     # добавляем в бд
            db.commit()     # сохраняем изменения
            
            result = db.query(AccountsTable).order_by(AccountsTable.id.desc()).first()

        return self.converter.conversion_to_data(result)
    
    

    def get_by_login(self, login:str) -> None|Account:
        '''
        Получить аккаунт по логину
        '''
        with Database() as db:
            account = db.query(AccountsTable).filter(AccountsTable.login==login).all()

        if account:
            return self.converter.conversion_to_data(account[0])