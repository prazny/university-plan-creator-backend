from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base


class Activity(Base):
    __tablename__ = 'activities'
    id = Column(Integer, primary_key=True, index=True)
    ects = Column(Integer(), nullable=False)
    cnps = Column(Integer(), nullable=False)
    zzu = Column(Integer(), nullable=False)
    bu = Column(Integer(), nullable=False)