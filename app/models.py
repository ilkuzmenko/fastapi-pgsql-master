from sqlalchemy import Column, Integer, Date
from config import Base


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    day = Column(Integer, nullable=False)
    date = Column(Date)
    troops = Column(Integer)
    tanks = Column(Integer)
    apv = Column(Integer)
    ars = Column(Integer)
    mlrs = Column(Integer)
    aaws = Column(Integer)
    airc = Column(Integer)
    helic = Column(Integer)
    uav = Column(Integer)
    missiles = Column(Integer)
    vehicle = Column(Integer)
    fueltanks = Column(Integer)
    warships_boats = Column(Integer)
    specialequipment = Column(Integer)
    srbm = Column(Integer)
