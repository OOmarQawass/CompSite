from dqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base

engine = create_engine('sqlite:///parts.db)
                       
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class Part(Base):
    __tablename__ = 'parts'
    id = Column(Integer, Sequence('part_id_seq'), primary_key=True)
    case = Column(String(50))
    cooler = Column(String(50))
    cpu = Column(String(50))
    gpu = Column(String(50))
    motherboard = Column(String(50))
    psu = Column(String(50))
    ram = Column(String(50))
    storage = Column(String(50))
    

    def __repr__(self):
        return f"<Part(name={self.name}, description={self.description}, quantity={self.quantity}, price={self.price})>"
                       