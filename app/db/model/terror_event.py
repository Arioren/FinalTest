from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.model import Base

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, autoincrement=True)
    year = Column(Integer, nullable=False)
    month = Column(Integer, nullable=True)
    day = Column(Integer, nullable=True)
    gang_name = Column(String, nullable=True)
    total_terrorists = Column(Integer, nullable=True)
    description = Column(String, nullable=True)
    attack_type_id = Column(Integer, ForeignKey('attack_types.id'), nullable=False)
    target_type_id = Column(Integer, ForeignKey('target_types.id'), nullable=False)
    casualties_id = Column(Integer, ForeignKey('casualties.id'), nullable=False)
    location_id = Column(Integer, ForeignKey('locations.id'), nullable=False)

    # Relationships
    attack_type = relationship("AttackType", back_populates="events")
    target_type = relationship("TargetType", back_populates="events")
    casualties = relationship("Casualties", back_populates="event")
    location = relationship("Location", back_populates="event", uselist=False)