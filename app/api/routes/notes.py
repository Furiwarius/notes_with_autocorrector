from fastapi import APIRouter, HTTPException, Depends, Request
from app.api.models.models import Note, User
from app.database.cruds import NotesCRUD
from app.service.note.note_service import NoteManager
from app.errors.service_exc import LoginExist
from fastapi.templating import Jinja2Templates
from typing import Annotated
from fastapi.security import OAuth2PasswordBearer
from app.utilities import verify_jwt_token


notes = APIRouter()
templates = Jinja2Templates(directory="app/templates")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    user = verify_jwt_token(token)
    return user


@notes.get("/notes")
async def get_notes(request:Request,
                   user: Annotated[User, Depends(get_current_user)], 
                   notes_crud: NotesCRUD = Depends(NotesCRUD)):
    '''
    Получение списка заметок
    '''
    notes = notes_crud.get_notes(user["user_id"])
    
    return templates.TemplateResponse(request, "notes.html", {"notes":notes})



@notes.get("/new_note")
async def new_note(request:Request,
                   user: Annotated[User, Depends(get_current_user)]):
    '''
    Получение страницы для добавления новой заметки
    '''
    
    return templates.TemplateResponse(request, "new_note.html")



@notes.post("/new_note")
async def add_note(note:Note,
                   user: Annotated[User, Depends(get_current_user)],
                   note_manager: NoteManager = Depends(NoteManager)):
    '''
    Добавление новой заметки
    '''
    

    note_manager.new_note(account_id=user["user_id"], 
                          note_name=note.name,
                          note_text=note.text)

    return {"message": "Note added!"}