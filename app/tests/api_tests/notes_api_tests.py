from app.entities import Note
from httpx import AsyncClient
from fastapi import status
import pytest



class TestNotesRoutes():
    '''
    Класс для тестирования ручек модуля notes
    '''


    @pytest.mark.asyncio
    async def test_get_notes(self, token:str, async_client:AsyncClient):
        '''
        Тестирование метода по получению страницы
        со списком заметок пользователя 
        '''
        
        response = await async_client.get("/notes", 
                                          headers={"Authorization": f"Bearer {token}"})
        
        assert response.status_code == status.HTTP_200_OK




    @pytest.mark.asyncio
    async def test_get_new_note_page(self, token:str, async_client:AsyncClient):
        '''
        Тестирование метода по получению страницы
        для добавления новой заметки
        '''
        response = await async_client.get("/new_note", 
                                          headers={"Authorization": f"Bearer {token}"})
        
        assert response.status_code == status.HTTP_200_OK




    @pytest.mark.asyncio
    async def test_add_note(self, note:Note, token:str, async_client:AsyncClient):
        '''
        Тестирование метода по добавлению
        новой заметки
        '''
        response = await async_client.post("/new_note", 
                                          headers={"Authorization": f"Bearer {token}"},
                                          json={"name": note.name, "text": note.text})
        
        assert response.status_code == status.HTTP_200_OK