from sqlalchemy.orm import relationship

from sql_to_neo4j.app.db.model import Base
from sqlalchemy import Column, Integer, String

class TargetType(Base):
    __tablename__ = 'target_types'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False, unique=True)


    events = relationship("Event", back_populates="target_type")