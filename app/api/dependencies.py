from app.utilities import verify_jwt_token
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from app.api.models.models import User
from fastapi.templating import Jinja2Templates


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
templates = Jinja2Templates(directory="app/templates")



async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]) -> User:
    user = verify_jwt_token(token)
    return User(user_id=user["user_id"])