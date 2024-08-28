from fastapi import FastAPI
from app.api.routes.login_account import login_account
from app.api.routes.notes import notes


class Application():
    '''
    Приложение
    '''


    @classmethod
    def create_app(self) -> FastAPI:
        '''
        Создание приложения
        '''
        app = FastAPI()
        app.include_router(login_account)
        app.include_router(notes)
        
        return app