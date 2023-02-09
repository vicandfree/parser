from sqlalchemy.exc import ProgrammingError
from sqlalchemy.orm import sessionmaker

from db import Computer


async def create_computer(url: str, name: str, cpu_hhz: float, ram_gb: int, ssd_gb: int, price: int,
                          session_maker: sessionmaker) -> None:
    async with session_maker() as session:
        async with session.begin():
            computer = Computer(
                url=url,
                name=name,
                cpu_hhz=cpu_hhz,
                ram_gb=ram_gb,
                ssd_gb=ssd_gb,
                price_rub=price,
                rank=cpu_hhz * 2 + ram_gb * 4 + ssd_gb * 2 + price * 4
            )
            try:
                session.add(computer)
            except ProgrammingError as e:
                pass