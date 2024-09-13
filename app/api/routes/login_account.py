from fastapi import APIRouter, HTTPException, Depends, Request
from app.api.models.models import UserData, Token
from app.service import AccountManager
from app.errors.service_exc import LoginExist, IncorrectUserData
from app.entities import Account
from app.api.dependencies import create_jwt_token, templates
from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.responses import JSONResponse, HTMLResponse


login_account = APIRouter()


@login_account.get("/", response_class=HTMLResponse)
async def index_page(request:Request):
    '''
    Главная страница
    '''
    return templates.TemplateResponse(request, "index.html")



@login_account.get("/registr",  response_class=HTMLResponse)
async def registr_page(request:Request):
    '''
    Страница регистрации
    '''
    return templates.TemplateResponse(request, "registr.html")



@login_account.post("/registr", response_class=JSONResponse)
async def new_user(new_user: Annotated[OAuth2PasswordRequestForm, Depends()], 
                   account_manager: AccountManager = Depends(AccountManager)):
    '''
    Регистрация пользователя
    '''
    try:
        await account_manager.new_user(login=new_user.username, password=new_user.password)
    
    except LoginExist as err:
        raise HTTPException(status_code=422, detail="This login is already in use") from err
    
    return {"message": "Accaunt created"}



@login_account.post("/token", response_model=Token)
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                account_manager: AccountManager = Depends(AccountManager)) -> Token:
    '''
    Получение токена для пользователя
    '''
    try:
        acc: Account = await account_manager.exist_user(login=form_data.username, 
                                         password=form_data.password)
    except IncorrectUserData as err:
        raise HTTPException(status_code=401, detail="Wrong login/password") from err
    
    token: str = await create_jwt_token({"user_id": acc.id})

    return Token(access_token=token, token_type="bearer")


