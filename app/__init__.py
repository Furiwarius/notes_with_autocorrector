from app.api import app
from fastapi.staticfiles import StaticFiles

app.mount("/static", StaticFiles(directory="app/templates/static"))