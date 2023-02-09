from sqlalchemy.engine import URL

postgres_url = URL.create(
    "postgresql+asyncpg",
    username='postgres',
    host='localhost',
    database='laptop_parser',
    port=5432,
    password='postgres'
)
