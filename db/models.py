from datetime import datetime

from sqlalchemy import Column, DateTime, Float, Integer, String

from .base import Base


class PrimaryIdModel(Base):
    """Абстрактная модель с id primary key"""
    __abstract__ = True

    id = Column(Integer,
                primary_key=True,
                unique=True,
                nullable=False)


class Computer(PrimaryIdModel):
    __tablename__ = 'computers'

    url = Column(String(500))
    visited_on = Column(DateTime(), default=datetime.now)
    name = Column(String(255))
    cpu_hhz = Column(Float)
    ram_gb = Column(Integer)
    ssd_gb = Column(Integer)
    price_rub = Column(Integer)
    rank = Column(Float)
