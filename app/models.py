from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Table,
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

ram_motherboard_compatibility = Table(
    'ram_motherboard_compatibility',
    Base.metadata,
    Column('ram_id', Integer, ForeignKey('ram.id')),
    Column('motherboard_id', Integer, ForeignKey('motherboard.id'))
)


class Case(Base):
    __tablename__ = 'case'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    form_factor = Column(String)


class Storage(Base):
    __tablename__ = 'storage'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    capacity = Column(String)
    type = Column(String)


class PSU(Base):
    __tablename__ = 'psu'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    wattage = Column(String)
    effeciency_rating = Column(String)


class GPU(Base):
    __tablename__ = 'gpu'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    vram = Column(String)


class Cooler(Base):
    __tablename__ = 'cooler'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    type = Column(String)
    size = Column(String)


class CPU(Base):
    __tablename__ = 'cpu'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    socket = Column(String)


class RAM(Base):
    __tablename__ = 'ram'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    speed = Column(String)
    capacity = Column(String)
    type = Column(String)

    motherboards = relationship(
        'Motherboard',
        secondary=ram_motherboard_compatibility,
        back_populates='rams'
    )


class Motherboard(Base):
    __tablename__ = 'motherboard'

    id = Column(Integer, primary_key=True)
    model = Column(String)
    chipset = Column(String)
    form_factor = Column(String)
    cpu_id = Column(String)
    cooler_id = Column(String)
    ram_id = Column(String)
    case_id = Column(String)

    rams = relationship(
        'RAM',
        secondary=ram_motherboard_compatibility,
        back_populates='motherboards'
    )

class Part(Base):
    __abstract__ = True
    id = Column(Integer, primary_key=True)
    model = Column(String)