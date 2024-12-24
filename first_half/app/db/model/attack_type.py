from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from first_half.app.db.model import Base


class AttackType(Base):
    __tablename__ = 'attack_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)

    # Relationships
    events = relationship("Event", back_populates="attack_type")