import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean

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
    user = Column(String(50), nullable=False)
    plan = Column(String(50), nullable=False)
