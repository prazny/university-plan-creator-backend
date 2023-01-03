from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base


class Level(enum.Enum):
    undergraduate = 'undergraduate'
    engineering = 'engineering'


class Profile(enum.Enum):
    academic = 'academic'
    practical = 'practical'


class Field(Base):
    __tablename__ = 'fields'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    profile = Column(Enum(Profile), nullable=False)
    level = Column(Enum(Level), nullable=False)
    faculty_id = Column(Integer, ForeignKey("faculties.id"), nullable=False)

    faculty = relationship("Faculty", back_populates="fields")
    #plans = relationship("Plan", back_populates="field")
