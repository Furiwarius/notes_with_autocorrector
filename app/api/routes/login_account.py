from fastapi import APIRouter, HTTPException, Depends, Request
from fastapi.responses import FileResponse
from app.api.models.models import UserData 
from app.service import AccountManager
from app.errors.service_exc import LoginExist, IncorrectUserData
from app.entities import Account
from app.utilities import create_jwt_token
from fastapi.templating import Jinja2Templates


login_account = APIRouter()
templates = Jinja2Templates(directory="app/templates")



@login_account.get("/")
async def index_page(request:Request):
    '''
    Главная страница
    '''
    return templates.TemplateResponse(request, "index.html")



@login_account.get("/registr")
async def registr_page(request:Request):
    '''
    Страница регистрации
    '''
    return templates.TemplateResponse(request, "registr.html")



@login_account.post("/registr")
async def new_user(new_user: UserData, 
                   account_manager: AccountManager = Depends(AccountManager)):
    '''
    Регистрация пользователя
    '''
    try:
        account_manager.new_user(login=new_user.login, password=new_user.password)
    
    except LoginExist as err:
        raise HTTPException(status_code=422, detail="This login is already in use") from err
    
    return {"message": "Accaunt created"}



@login_account.post("/login")
async def login(user: UserData,
                account_manager: AccountManager = Depends(AccountManager)):
    '''
    Вход
    '''
    try:
        acc: Account = account_manager.exist_user(login=user.login, 
                                         password=user.password)
    except IncorrectUserData as err:
        raise HTTPException(status_code=401, detail="Wrong login/password") from err
    
    token = create_jwt_token({"user_id": acc.id})
    return {"token": token}



