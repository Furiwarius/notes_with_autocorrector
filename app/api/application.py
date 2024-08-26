from fastapi import FastAPI


class Application():
    '''
    Приложение
    '''

    def create_app(self) -> FastAPI:
        '''
        Создание приложения
        '''
        self.app = FastAPI()

        return self.app