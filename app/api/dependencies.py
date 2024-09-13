from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from app.api.models.models import User
from fastapi.templating import Jinja2Templates
from jwt.exceptions import InvalidTokenError
import jwt
from datetime import datetime, timezone
from app.settings import jwt_settings



oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
templates = Jinja2Templates(directory="app/templates")



async def create_jwt_token(data: dict) -> str:
    '''
    Создание токена из словаря данных
    '''
    # Время жизни токена
    expiration:datetime = datetime.now(timezone.utc) + jwt_settings.EXPIRATION_TIME
    # Добавляем в тело токена время жизни
    data.update({"exp": expiration})

    token:str = jwt.encode(data, jwt_settings.JWT_KEY, algorithm=jwt_settings.ALGORITHM)
    
    return token



async def verify_jwt_token(token: str) -> User:
    '''
    Расшифровка токена
    '''
    try:
        decoded_data:dict = jwt.decode(token, 
                                  jwt_settings.JWT_KEY, 
                                  algorithms=[jwt_settings.ALGORITHM])
        
        return User(user_id=decoded_data["user_id"])
    
    except jwt.PyJWTError:
        raise HTTPException(status_code=419, detail="Invalid token")



async def getting_data(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    '''
    Получение данных из токена
    '''
    
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        user:User = await verify_jwt_token(token)
    except InvalidTokenError:
        raise credentials_exception
    
    return user



async def get_current_user(current_user: Annotated[User, Depends(getting_data)]) -> User:
    '''
    Получение пользователя по токену
    '''
    
    return current_user