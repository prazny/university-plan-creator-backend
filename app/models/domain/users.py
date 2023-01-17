from sqlalchemy import Column, Integer, String, ForeignKey, Enum, Table
import enum
from sqlalchemy.orm import relationship
from app.models.domain.base import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, index=True)
    login = Column(String(30), nullable=False)
    email = Column(String(30), nullable=False)
    password = Column(String(30), nullable=False)
