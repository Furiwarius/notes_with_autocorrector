from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from app.api.models.models import UserData 
from app.service import AccountManager
from app.errors.service_exc import LoginExist, LoginNotExist, IncorrectPassword
from app.entities import Account
from app.utilities import create_jwt_token


login_account = APIRouter()


@login_account.get("/")
async def index():
    '''
    Главная страница
    '''
    return FileResponse("index.html")



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
    except LoginNotExist as err:
        raise HTTPException(status_code=401, detail="Wrong login") from err
    except IncorrectPassword as err:
        raise HTTPException(status_code=401, detail="Wrong password") from err
    
    token = create_jwt_token({"user_id": acc.id})
    return {"token": token}



