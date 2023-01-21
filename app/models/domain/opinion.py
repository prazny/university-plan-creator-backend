import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.models.domain.base import Base


class Status(enum.Enum):
    positive = 'positive'
    negative = 'negative'


class Opinion(Base):
    __tablename__ = 'opinions'
    id = Column(Integer, primary_key=True, index=True)
    is_approved = Column(Boolean, nullable=False)
    description = Column(String(50), nullable=False)
    status = Column(Enum(Status), nullable=True)

    user = relationship("User", back_populates="opinions")
    user_id = Column(Integer, ForeignKey('users.id'))

    plan = relationship("Plan", back_populates="opinions")
    plan_id = Column(Integer, ForeignKey('plans.id'))
