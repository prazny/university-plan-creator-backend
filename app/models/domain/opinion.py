import enum

from sqlalchemy import Column, Integer, String, Enum, Boolean

from app.models.domain.base import Base


class OpinionStatus(enum.Enum):
    positive = 'Positive'
    negative = 'Negative'


class Opinion(Base):
    __tablename__ = 'opinions'
    id = Column(Integer, primary_key=True, index=True)
    is_approved = Column(Boolean, nullable=False)
    description = Column(String(50), nullable=False)
    type = Column(Enum(OpinionStatus), nullable=True)
