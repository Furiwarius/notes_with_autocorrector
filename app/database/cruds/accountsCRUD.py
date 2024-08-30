from app.database import Database
from app.database.tables.essence import AccountsTable
from app.entities.account import Account
from app.utilities import convertertation



class AccountCRUD():
    '''
    Класс для работы с аккаунтами пользователей в БД
    '''


    @convertertation
    def add(self, new_acc:Account) -> Account:
        '''
        Добавить аккаунт
        '''

        with Database() as db:

            db.add(new_acc)     # добавляем в бд
            db.commit()     # сохраняем изменения
            
            result = db.query(AccountsTable).order_by(AccountsTable.id.desc()).first()

        return result
    
    
    @convertertation
    def get_by_login(self, login:str) -> None|Account:
        '''
        Получить аккаунт по логину
        '''
        with Database() as db:
            return db.query(AccountsTable).filter(AccountsTable.login==login).one_or_none()