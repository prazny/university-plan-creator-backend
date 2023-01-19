from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base
# from app.models.domain.semester import plan_semester


class Form(enum.Enum):
    fulltime = 'fulltime'
    parttime = 'parttime'


class Plan(Base):
    __tablename__ = 'plans'
    id = Column(Integer, primary_key=True, index=True)
    year = Column(Integer(), nullable=False)
    form = Column(String(100))
    number_of_semesters = Column(Integer())
    lang = Column(String(100))
    field_id = Column(Integer, ForeignKey("fields.id"), nullable=False)
    # field_id = Column(Integer(), nullable = False)

    field = relationship("Field", back_populates="plans")
    # semesters = relationship("Plan", back_populates="plan")
    # semesters = relationship("Plan", secondary=plan_semester, backref="plans")

    opinions = relationship("Opinion", back_populates="plan")
