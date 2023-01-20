from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Table
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base

plan_semester = Table(
    "plan_semester",
    Base.metadata,
    Column("plan_id", ForeignKey("plans.id"), primary_key=True),
    Column("semester_id", ForeignKey("semesters.id"), primary_key=True)
)

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

    fields = relationship("Field", back_populates="plans")
    semesters = relationship("Semester", secondary=plan_semester, backref="plans")
