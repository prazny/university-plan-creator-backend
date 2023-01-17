from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Table
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base

plan_semester = Table(
    "plan_semester",
    Base.metadata,
    Column("semester_id", ForeignKey("semesters.id")),
    Column("plan_id", ForeignKey("plans.id")),

)


class Semester(Base):
    __tablename__ = 'semesters'
    id = Column(Integer, primary_key=True, index=True)
    max_ects_deficit = Column(Integer(), nullable=False)
    semester_number = Column(Integer(), nullable=False)

    plans = relationship("Semester", secondary=plan_semester, backref="semesters")
