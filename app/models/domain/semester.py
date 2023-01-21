from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Table
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base

semesters_activities = Table(
    "semesters_activities",
    Base.metadata,
    Column("semester_id", ForeignKey("semesters.id"), primary_key=True),
    Column("activity_id", ForeignKey("activities.id"), primary_key=True),
)

class Semester(Base):
    __tablename__ = 'semesters'
    id = Column(Integer, primary_key=True, index=True)
    max_ects_deficit = Column(Integer(), nullable=False)
    semester_number = Column(Integer(), nullable=False)
    # plan_id = Column(Integer(), ForeignKey('plans.id'), nullable=False)
    activities = relationship('Activity', secondary=semesters_activities, backref='semesters')

    #plans = relationship("Semester", secondary=plan_semester, backref="semesters")

