import asyncio

from config import postgres_url
from db import create_async_engine, get_session_maker
from parsers import parse_dns, parse_mvideo


async def parse():
    async_engine = create_async_engine(postgres_url)
    session_maker = get_session_maker(async_engine)
    await parse_mvideo(session_maker)
    await parse_dns(session_maker)

if __name__ == '__main__':
    asyncio.run(parse())
