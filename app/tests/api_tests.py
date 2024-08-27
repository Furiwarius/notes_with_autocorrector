from fastapi import status
import pytest
from httpx import AsyncClient
from random import randrange
from copy import copy
from app.entities import Account
from app.utilities import verify_jwt_token



class TestLoginAccountRoutes():
    '''
    Класс для тестирования ручек модуля login_account
    '''


    @pytest.mark.asyncio
    async def test_index(self, async_client:AsyncClient):
        '''
        Тестирование метода по получению индекскной страницы
        '''
        response = await async_client.get("/")
        assert response.status_code == status.HTTP_200_OK
  


    @pytest.mark.asyncio
    async def test_new_user(self, account:Account, async_client:AsyncClient):
        '''
        Тестирование метода по созданию нового пользователя
        '''

        response = await async_client.post("/registr",
                                    json={"login": account.login,
                                          "password": account.password})
        
        assert response.status_code == status.HTTP_200_OK    



    @pytest.mark.asyncio
    async def test_new_user_exception(self, exist_account:Account, async_client:AsyncClient):
        '''
        Тестирование вызова исключений при использовании
        метода по созданию нового пользователя
        '''

        json={"login": exist_account.login,
              "password": exist_account.password}
        
        response = await async_client.post("/registr", json=json)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY  



    @pytest.mark.asyncio
    async def test_login(self, exist_account:Account, async_client:AsyncClient):
        '''
        Тестирование метода по авторизации пользователя
        '''

        response = await async_client.post("/login",
                                    json={"login": exist_account.login,
                                          "password": exist_account.password})
        
        assert response.status_code == status.HTTP_200_OK

        jwt_data = response.json()
        assert jwt_data["token"]

        data = verify_jwt_token(token=jwt_data["token"])
        print(exist_account.id)
        print(int(data["user_id"]))
        assert exist_account.id==int(data["user_id"])
    


    @pytest.mark.asyncio
    async def test_login_exception(self, exist_account:Account, async_client:AsyncClient):
        '''
        Тестирование метода по авторизации с получением исключений
        '''

        json = {"login": exist_account.login, "password": exist_account.password}

        # Меняем логин, меняем пароль и пытаемся пройти авторизацию
        for item in json:
            copy_json = copy(json)
            copy_json[item]+=str(randrange(10))

            response = await async_client.post("/login", json=copy_json)
            
            assert response.status_code == status.HTTP_401_UNAUTHORIZED