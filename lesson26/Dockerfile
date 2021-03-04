FROM python:3.6

# Установка базовой рабочей директории внутри контейнера
WORKDIR /app

# Копирование зависимостей
COPY requirements.txt .

# Установка зависимостей
RUN pip install -U pip && pip install -r requirements.txt

# Копирование остальных файлов проекта не добавленных в dockerignore
COPY . .

# Предустановка команды pytest и папки allure-отчёта
ENTRYPOINT ["pytest", "--alluredir", "allure-report"]

# Запуск с необходимыми параметрами
CMD ["--browser", "chrome"]


