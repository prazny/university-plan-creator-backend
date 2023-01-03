from sqlalchemy import Column, Integer, String, ForeignKey, Enum
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base


class Module(Base):
    __tablename__ = 'modules'
    id = Column(Integer, primary_key=True, index=True)

