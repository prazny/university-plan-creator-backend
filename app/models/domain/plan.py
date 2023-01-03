from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base
from app.models.domain.semester import plan_semester


class Form(enum.Enum):
    fulltime = 'fulltime'
    parttime = 'parttime'


class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer(), nullable=False)
    form = Column(Enum(Form))
    number_of_semesters = Column(Integer())
    lang = Column(String(100))
    field_id = Column(Integer, ForeignKey("fields.id"), nullable=False)

    field = relationship("Field", back_populates="plans")
    semesters = relationship("Plan", secondary=plan_semester, back_populates="plans")
