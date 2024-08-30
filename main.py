from app import app
import uvicorn

# Запуск uvicorn main:app --reload

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, log_level="info")