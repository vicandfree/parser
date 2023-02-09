# laptop_parser

## Первый запуск

1) Сформируй виртуальное Python-окружение
2) Установи зависимости `pip install -r requirements.txt`
3) В качестве БД используется PostgreSQL. Запустить можно через Docker.
4) Необходимо создать БД и указать в переменной `postgres_url` по адресу `config/__init__.py`
5) Накатить схему БД (миграции) `alembic upgrade head`
6) Запустить приложение `python main.py`