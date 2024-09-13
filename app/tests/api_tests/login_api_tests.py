from fastapi import status
import pytest
from httpx import AsyncClient
from random import randrange
from copy import copy
from app.entities import Account
from app.api.dependencies import verify_jwt_token
from app.api.models.models import User



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
                                    data={"username": account.login,
                                          "password": account.password},
                                    headers={"Content-Type": "application/x-www-form-urlencoded"})
        assert response.status_code == status.HTTP_200_OK    



    @pytest.mark.asyncio
    async def test_new_user_exception(self, exist_account:Account, async_client:AsyncClient):
        '''
        Тестирование вызова исключений при использовании
        метода по созданию нового пользователя
        '''

        data={"username": exist_account.login,
              "password": exist_account.password}
        
        response = await async_client.post("/registr", data=data,
                                           headers={"Content-Type": "application/x-www-form-urlencoded"})
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY  



    @pytest.mark.asyncio
    async def test_login(self, exist_account:Account, async_client:AsyncClient):
        '''
        Тестирование метода по авторизации пользователя
        '''

        response = await async_client.post("/token",
                                    data={"username": exist_account.login,
                                          "password": exist_account.password},
                                    headers={"Content-Type": "application/x-www-form-urlencoded"})
        
        assert response.status_code == status.HTTP_200_OK

        jwt_data = response.json()
        assert jwt_data["access_token"]

        user: User = await verify_jwt_token(token=jwt_data["access_token"])

        assert exist_account.id==int(user.user_id)
    


    @pytest.mark.asyncio
    async def test_login_exception(self, exist_account:Account, async_client:AsyncClient):
        '''
        Тестирование метода по авторизации с получением исключений
        '''

        data = {"username": exist_account.login, "password": exist_account.password}

        # Меняем логин, меняем пароль и пытаемся пройти авторизацию
        for item in data:
            copy_data = copy(data)
            copy_data[item]+=str(randrange(10))

            response = await async_client.post("/token", data=copy_data,
                                               headers={"Content-Type": "application/x-www-form-urlencoded"})
            
            assert response.status_code == status.HTTP_401_UNAUTHORIZED