from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base
from app.models.domain.activity import Activity


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


class Course(Activity):
    __tablename__ = 'courses'
    __mapper_args__ = {'polymorphic_identity': 'course'}
    id = Column(Integer, ForeignKey('activities.id'), primary_key=True, index=True)
    hours_count = Column(Integer, nullable=False)
    code = Column(String(50), nullable=False)
    type = Column(Enum(Type), nullable=False)
    completing_form = Column(String(50))
    course_form = Column(Enum(Form), nullable=False)
