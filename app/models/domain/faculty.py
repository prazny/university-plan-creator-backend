from sqlalchemy import Column, Integer, String, ForeignKey
from app.models.domain.base import Base
from sqlalchemy.orm import relationship


class Faculty(Base):
    __tablename__ = 'faculties'
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)

    # fields = relationship("Field", backref='faculty')
