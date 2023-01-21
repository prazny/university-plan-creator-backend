from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    ects = Column(Integer(), nullable=False)
    cnps = Column(Integer(), nullable=False)
    zzu = Column(Integer(), nullable=False)
    bu = Column(Integer(), nullable=False)
    type_of_activity = Column('type', String(50))
    __mapper_args__ = {'polymorphic_on': type_of_activity}
