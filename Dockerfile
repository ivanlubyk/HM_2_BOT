# Docker-команда FROM вказує базовий образ контейнера
# Наш базовий образ - це Linux з попередньо встановленим python-3.10
FROM python:3.11

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію усередині контейнера
WORKDIR $APP_HOME
COPY pyproject.toml $APP_HOME/pyproject.toml
COPY poetry.lock $APP_HOME/poetry.lock


# Встановимо залежності усередині контейнера
RUN pip install poetry
RUN poetry config virtualenvs.create false && poetry install


# Скопіюємо інші файли до робочої директорії контейнера
COPY . .


# Позначимо порт де працює програма всередині контейнера
EXPOSE 5000

# Запустимо нашу програму всередині контейнера
ENTRYPOINT ["python", "bot_folder/start_bot.py"]
# запуск для взаємодії - docker run -it my_home_web_2.1
