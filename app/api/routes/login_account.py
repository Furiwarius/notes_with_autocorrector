from fastapi import APIRouter, HTTPException, Depends
from fastapi.responses import FileResponse
from app.api.models.models import UserData 




login_account = APIRouter()


@login_account.get("/")
async def index():
    '''
    Главная страница
    '''
    return FileResponse("index.html")



@login_account.post("/registr")
async def new_user(new_user: UserData):
    '''
    Регистрация пользователя
    '''
    try:
        account_manager = AccountManager(Account(login=new_user.login,
                                                password=new_user.password,
                                                email=new_user.email,
                                                timezone=new_user.timezone), new=True)
    
    except EmailExists as err:
        raise HTTPException(status_code=422, detail="This email is already in use") from err
    except LoginExists as err:
        raise HTTPException(status_code=422, detail="This login is already taken") from err
    
    return {"message": "Accaunt created"}



@login_account.post("/login")
async def login(user: User):
    '''
    Вход
    '''
    try:
        account_manager = AccountManager(Account(login=user.login,
                                                password=user.password))
    except IncorrectPassword as err:
        raise HTTPException(status_code=401, detail="Wrong password") from err
    except IncorrectLogin as err:
        raise HTTPException(status_code=401, detail="Wrong login") from err
    
    token = create_jwt_token({"user_id": account_manager.account.id})
    return {"token": token}



