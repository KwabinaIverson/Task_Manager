#!/usr/bin/python3
"""User that inherits from BaseModel"""

import models
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, MetaData
from sqlalchemy.orm import relationship, backref
from hashlib import md5

class User(BaseModel, Base):
    """
    User class that inherits from BaseModel.

    Public class attributes:
    - email: string - empty string
    - password: string - empty string
    - first_name: string - empty string
    - last_name: string - empty string
    """
    if models.sqlStorage_t == "db":
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=False)
        last_name = Column(String(128), nullable=False)
        tasks = relationship("Task", backref="creator", cascade="all, delete, delete-orphan")
        groups = relationship("Group", back_populates="users", cascade="all, delete, delete-orphan")
    else:
        email = ""
        password = ""
        first_name = ""
        last_name = ""
    
    def __init__(self, *args, **kwargs):
        """Constructor for User class."""
        super().__init__(*args, **kwargs)

    def __setattr__(self, name, value):
        """Encrypt password with md5"""
        if name == "password":
             value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
