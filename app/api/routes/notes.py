from fastapi import APIRouter, HTTPException, Depends, Request
from app.api.models.models import Note, User
from app.database.cruds import NotesCRUD
from app.service.note.note_service import NoteManager
from app.errors.service_exc import LoginExist
from typing import Annotated
from app.api.dependencies import get_current_user, templates
from fastapi.responses import HTMLResponse, JSONResponse



notes = APIRouter()


@notes.get("/notes", response_class=HTMLResponse)
async def get_notes(request:Request,
                   user: Annotated[User, Depends(get_current_user)], 
                   notes_crud: NotesCRUD = Depends(NotesCRUD)):
    '''
    Получение списка заметок
    '''
    notes = await notes_crud.get_notes(user.user_id)
    
    return templates.TemplateResponse(request, "notes.html", {"notes":notes})



@notes.get("/new_note",  response_class=HTMLResponse)
async def new_note(request:Request,
                   user: Annotated[User, Depends(get_current_user)]):
    '''
    Получение страницы для добавления новой заметки
    '''
    
    return templates.TemplateResponse(request, "new_note.html")



@notes.post("/new_note", response_class=JSONResponse)
async def add_note(note:Note,
                   user: Annotated[User, Depends(get_current_user)],
                   note_manager: NoteManager = Depends(NoteManager)):
    '''
    Добавление новой заметки
    '''
    

    await note_manager.new_note(account_id=user.user_id, 
                          note_name=note.name,
                          note_text=note.text)

    return {"message": "Note added!"}