FROM python:3.12 as builder

# Метаданные
LABEL author="VasiliyTrunov" 
LABEL version="0.0"

# Создаем папку app
WORKDIR /app
# Копируем файл зависимостей
COPY ./requirements.txt .
# Скачиваем все модули из файла
RUN pip install -r ./requirements.txt
# Копируем в папку наш проект
COPY . .

ENTRYPOINT bash -c "uvicorn main:app --host 127.0.0.1 --port 8000 --reload"