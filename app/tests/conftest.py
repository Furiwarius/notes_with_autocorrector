from app.database.cruds import AccountCRUD, NotesCRUD
from app.service import AccountManager
from app.entities import Account, Note
from faker import Faker
import pytest_asyncio
from random import randrange
from app.utilities import to_hash
from copy import copy
from app.api import app
from fastapi.testclient import TestClient
from httpx import ASGITransport, AsyncClient
from typing import AsyncGenerator, Generator
from app.api.dependencies import create_jwt_token


# набор уникальных цифр
numbers = set([number for number in range(1000)])



@pytest_asyncio.fixture(scope="session")
def fake() -> Faker:
    return Faker(locale="ru")



@pytest_asyncio.fixture(scope="function")
def generate_number() -> int:
        '''
        Генерация уникальной цифры
        '''
        value = tuple(numbers)[randrange(0, len(numbers)-1)]
        numbers.discard(value)

        return value



@pytest_asyncio.fixture(scope="function")
def account(fake:Faker, generate_number:int) -> Account:
    '''
    Генератор данных аккаунта
    '''

    new_account = Account(login=f"{fake.first_name()}{generate_number}",
                              password=f"password{generate_number}")

    return new_account



@pytest_asyncio.fixture(scope="function")
def note(account_id:int, fake:Faker) -> Note:
    '''
    Генератор заметки
    '''

    new_note = Note(name=fake.word(),
                    text=fake.paragraph(),
                    account_id=account_id)

    return new_note



@pytest_asyncio.fixture(scope="session")
def note_crud() -> NotesCRUD:
     
    return NotesCRUD()



@pytest_asyncio.fixture(scope="session")
def acc_crud() -> AccountCRUD:
     
    return AccountCRUD()



@pytest_asyncio.fixture(scope="function")
def account_id(fake:Faker, generate_number:int, acc_crud:AccountCRUD) -> int:
    
    new_acc = Account(login=f"{fake.first_name()}{generate_number}",
                              password=f"password{generate_number}")
    acc = acc_crud.add(new_acc)
    return acc.id



@pytest_asyncio.fixture(scope="function")
def exist_account(account:Account, acc_crud:AccountCRUD) -> Account:
    '''
    Генерация аккаунта с добавлением его в бд
    '''
    new_acc = copy(account)
    new_acc.login = to_hash(new_acc.login)
    new_acc.password = to_hash(new_acc.password)
    
    result:Account = acc_crud.add(new_acc)
    account.id = result.id
    return account



@pytest_asyncio.fixture(scope="session")
def account_manager() -> AccountManager:
    
    return AccountManager()



@pytest_asyncio.fixture(scope="session")
def anyio_backend():
    return "asyncio"



@pytest_asyncio.fixture(scope="session")
def client() -> Generator:
    yield TestClient(app)



@pytest_asyncio.fixture(scope="session", autouse=True)
async def async_client(client:TestClient) -> AsyncGenerator:
    async with AsyncClient(transport=ASGITransport(app=app), base_url=client.base_url) as ac:
        yield ac



@pytest_asyncio.fixture(scope="function")
def token(exist_account:Account) -> str:
    '''
    Генерация аккаунта с добавлением его в бд и возвращением токена
    '''

    return create_jwt_token({"user_id": exist_account.id})