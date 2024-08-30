FROM python:3.12 AS builder

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

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]