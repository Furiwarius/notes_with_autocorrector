from app.database.cruds import AccountCRUD, NotesCRUD
from app.entities import Account, Note
from faker import Faker
import pytest_asyncio


# набор уникальных цифр
numbers = set([number for number in range(1000)])



@pytest_asyncio.fixture(scope="session")
def fake() -> Faker:
    return Faker(locale="ru")



@pytest_asyncio.fixture(scope="function")
def account(fake:Faker, generate_number:int) -> Account:
    '''
    Генератор данных аккаунта
    '''

    new_account = Account(login=f"{fake.first_name}{generate_number}",
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
