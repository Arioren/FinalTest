
from elastic_project.app.db.model import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    province = Column(String, nullable=True)
    country_id = Column(Integer, ForeignKey('countries.id'), nullable=False)

    # Relationships with explicit foreign_keys
    country = relationship("Country", back_populates="cities")
    location = relationship("Location", back_populates="city", uselist=False)