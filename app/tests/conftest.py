from app.database.cruds import AccountCRUD, NotesCRUD
from app.entities import Account, Note
from faker import Faker
import pytest_asyncio
from random import randrange


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
def note(fake:Faker) -> Note:
    '''
    Генератор заметки
    '''

    new_note = Note(name=fake.word(),
                    text=fake.paragraph())

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