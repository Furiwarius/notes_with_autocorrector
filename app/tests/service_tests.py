from app.service import AccountManager
from app.entities.account import Account
import pytest
from app.errors.service_exc import LoginExist, LoginNotExist



class TestService():
    '''
    Тестирование классов бизнес-логики
    '''


    def test_new_user(self, account:Account, account_manager:AccountManager):
        '''
        Тестирование метода по добавлению
        нового аккаунта 
        AccountManager.new_user()
        '''
        acc:Account = account_manager.new_user(login=account.login,
                                               password=account.password)
        assert acc.id



    def test_new_user_with_LoginExist(self, 
                                      exist_account:Account, 
                                      account_manager:AccountManager):
        '''
        Тестирование метода по добавлению в бд
        с вызовом исключения LoginExist
        '''

        with pytest.raises(LoginExist):
            account_manager.new_user(login=exist_account.login,
                                     password=exist_account.password)



    def test_exist_user(self, exist_account:Account, account_manager:AccountManager):
        '''
        Тестирование метода по получению
        данных существующего аккаунта 
        AccountManager.exist_user()
        '''

        acc:Account = account_manager.exist_user(login=exist_account.login,
                                         password=exist_account.password)
        
        assert acc.id

    

    def test_exist_user_with_LoginNotExist(self, account:Account, account_manager:AccountManager):
        '''
        Тестирование метода по получению
        данных существующего аккаунта 
        AccountManager.exist_user() c вызовом
        исключения LoginNotExist
        '''
        with pytest.raises(LoginNotExist):
            account_manager.exist_user(login=account.login,
                                         password=account.password)