from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from app.database import Base
class Crew(Base):
    __tablename__ = "crews"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    captain = Column(String, nullable=False)
    ship = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
class Character(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    role = Column(String, nullable=False)
    bounty = Column(Integer, nullable=False)
    crew_id = Column(Integer, ForeignKey("crews.id"))
