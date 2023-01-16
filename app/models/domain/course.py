from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base


class Type(enum.Enum):
    laboratory = 'laboratory'
    practice = 'practice'
    lecture = 'lecture'
    project = 'project'
    seminar = 'seminar'
    lang_course = 'lang_course'
    thesis = 'thesis'


class Form(enum.Enum):
    stationary = 'stationary'
    remote = 'remote'


class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    ects = Column(Integer, nullable=False)
    cnps = Column(Integer, nullable=False)
    zzu = Column(Integer, nullable=False)
    bu = Column(Integer, nullable=False)
    hours_count = Column(Integer, nullable=False)
    direction = Column(String(50), nullable=False)
    code = Column(String(50), nullable=False)
    type = Column(Enum(Type), nullable=False)
    completing_form = Column(String(50))
    course_form = Column(Enum(Form), nullable=False)
