# Використовуємо офіційний образ Python як базовий
FROM python:3.11-slim

# Встановимо робочу директорію всередині контейнера
WORKDIR /app

# Скопіюємо файл залежностей у контейнер
COPY requirements.txt .

# Встановимо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Скопіюємо решту проекту в контейнер
COPY . .

# Встановимо змінні оточення для запуску
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT production

# Відкриємо порт для програми
EXPOSE 8000
# Команда для запуску
CMD ["python", "fastapi-application/run_main.py"]
