#!/usr/bin/python3
"""User that inherits from BaseModel"""

from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import relationship, backref

class User(BaseModel, Base):
    """
    User class that inherits from BaseModel.

    Public class attributes:
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))
    
    tasks = relationship("Task", backref="creator", cascade="all, delete, delete-orphan")
    
    groups = relationship("Group", back_populates="users", cascade="all, delete, delete-orphan")
    
    def __init__(self, *args, **kwargs):
        """Constructor for User class."""
        super().__init__(*args, **kwargs)
