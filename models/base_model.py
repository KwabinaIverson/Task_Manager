#!/usr/bin/python3
"""
BaseModel takes care of the initialization, serialization and deserialization of future instances.
"""

import uuid
import models
import inspect
from os import getenv
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

time = "%Y-%m-%dT%H:%M:%S.%f"

if models.sqlStorage_t == "db":
    Base = declarative_base()
else:
    Base = object

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
    if models.sqlStorage_t == "db":
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
                if key != "__class__":
                    setattr(self, key, value)
            if kwargs.get("created_at", None) and type(self.created_at) is str:
                self.created_at = datetime.strptime(kwargs["created_at"], time)
            else:
                self.created_at = datetime.utcnow()
            if kwargs.get("updated_at", None) and type(self.updated_at) is str:
                self.updated_at = datetime.strptime(kwargs["updated_at"], time)
            else:
                self.updated_at = datetime.utcnow()
            if kwargs.get("id", None) is None:
                self.id = str(uuid.uuid4())
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at
        
    def save(self):
        """
        Updates the public instance attribute `updated_at` 
        with the current datetime.
        """
        self.updated_at = datetime.utcnow()
        models.storage.new(self)
        models.storage.save()
        
    def to_dict(self):
        """
        Returns a dictionary representation of the instance.

        Returns:
        - dict: Dictionary containing all keys/values of __dict__ of the instance.
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = new_dict["created_at"].strftime(time)
        if "updated_at" in new_dict:
            new_dict["updated_at"] = new_dict["updated_at"].strftime(time)
        new_dict["__class__"] = self.__class__.__name__
        if "_sa_instance_state" in new_dict:
            del new_dict["_sa_instance_state"]
        frame = inspect.currentframe().f_back
        func_name = frame.f_code.co_name
        class_name = ''
        if 'self' in frame.f_locals:
            class_name = frame.f_locals["self"].__class__.__name__
        is_fs_writing = func_name == 'save' and class_name == 'FileStorage'
        if 'password' in new_dict and not is_fs_writing:
            del new_dict['password']
        return new_dict
    
    def __str__(self):
        """
        Returns a string representation of the BaseModel instance.

        Returns:
        - str: String representation in the format: "[<class name>] (<self.id>) <self.__dict__>"
        """
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)
    
    def delete(self):
        """delete the current instance from the storage"""
        models.storage.delete(self)
