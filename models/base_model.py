#!/usr/bin/python3
"""
BaseModel takes care of the initialization, serialization and deserialization of future instances.
"""

import uuid
from datetime import datetime
import models
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, MetaData

Base = declarative_base()

class BaseModel:
    """
    BaseModel class
    
    Defines all common attributes/methods for other classes.
    
    Public instance attributes:
    - id (str): Unique identifier for each BaseModel instance.
    - created_at (datetime): Timestamp for when the BaseModel instance was created.
    - updated_at (datetime): Timestamp for when the BaseModel instance was last updated.
    
    Public instance methods:
    - save(self): Updates the public instance attribute `updated_at` with the current datetime.
    - to_dict(self): Returns a dictionary containing all keys/values of __dict__ of the instance.
    
    Special method:
    - __str__(self): Returns a string representation of the BaseModel instance.
    """
    id = Column(String(60), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    updated_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instance.
        
        Args:
            -*args: Unused
            -**kwargs: Dictionary of attribute names and values.
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
                    
            if "id" not in kwargs:
                self.id = str(uuid.uuid4())
                
            if "created_at" not in kwargs:
                self.created_at = self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
        
    def save(self):
        """
        Updates the public instance attribute `updated_at` 
        with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        models.storage.save()
        models.storage.new(self)
        
    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
        - dict: Dictionary containing all keys/values of __dict__ of the instance.
        """
        instance_dict = self.__dict__.copy()
        instance_dict['created_at'] = self.created_at.isoformat()
        instance_dict['updated_at'] = self.updated_at.isoformat()
        instance_dict['__class__'] = self.__class__.__name__
        return instance_dict
    
    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
        - str: String representation in the format: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
