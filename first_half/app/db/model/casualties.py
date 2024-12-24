from sqlalchemy import Column, Integer
from sqlalchemy.orm import relationship
from first_half.app.db.model import Base

class Casualties(Base):
    __tablename__ = 'casualties'

    id = Column(Integer, primary_key=True, autoincrement=True)
    killed = Column(Integer, default=0)
    wounded = Column(Integer, default=0)

    # Relationships
    event = relationship("Event", back_populates="casualties", uselist=False)