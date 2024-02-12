#!/usr/bin/python3
"""Task class the inherits from BaseModel."""

import uuid
import models
from datetime import datetime
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey, DateTime

class Task(BaseModel, Base):
    """
    Task class
    
    Defines the attributes/methods and inherits from BaseModel class.
    
    Public class attributes
    - task_id (str): Unique identifier for each task instance.
    - task_name (str): Name or title of the task.
    - description (str): Detailed description of the task.
    - start_date (str): Date when the task starts.
    - end_date (str): Date when the task is due.
    - category (str): Category or tag associated with the task.
    
    Public instance methods
    - create_task(self): Creates a new task with the given details.
    - edit_task(self): Modifies the details of an existing task.
    - set_due_date(self): Sets the starting and ending dates for the task.
    - delete_task(self): Deletes the specified task.
    """
    __tablename__ = 'tasks'
    task_name = Column(String(128))
    user_id = Column(String(60), ForeignKey("users.id"))
    task_description = Column(String(1024))
    start_date = Column(DateTime, default=datetime.utcnow)
    end_date = Column(DateTime, default=datetime.utcnow)
    category = Column(String(128))
    
    # creator = relationship("User", backref='assigned_tasks', cascade="all, delete, delete-orphan")
    
    def __init__(self, *args, **kwargs):
        """
        Constructor for Task class.
        
        Args:
            - *args: Unknown arguments
            - **kwargs: Known arguments
        """
        super().__init__(*args, **kwargs)
    
    def create_task(self, task_name, description, start_date, end_date, category):
        """
        Creates a new task with the given details.
        
        Args:
            - task_name (str): Name of the task.
            - description (str): Description of task.
            - start_date (datetime): Start of task.
            - end_date (datetime): End of task.
            - category (str): Tasks based on a certain classification or grouping.
        """
        self.task_name = task_name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.category = category
        self.save()
        
    def edit_task(self, task_name=None, description=None, start_date=None, end_date=None, category=None):
        """
        Edit an exiting task.
        
        Args:
            - task_name (str): Name of the task.
            - description (str): Description of task.
            - start_date (datetime): Start of task.
            - end_date (datetime): End of task.
            - category (str): Tasks based on a certain classification or grouping.
        """
        if task_name is not None:
            self.task_name = task_name
        if description is not None:
            self.description = description
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date
        if category is not None:
            self.category = category
        self.save()
    
    def set_due_date(self, start_date, end_date):
        """
        Create end date and time of a task.
        
        Args:
            - start_date (datetime): Start time and date for a task.
            - end_date (datetime): End time and date for a task.
        """
        self.start_date = start_date
        self.end_date = end_date
        self.save()
        
    def delete_task(self):
        """
        Deletes the specified task.
        """
        models.storage.delete(self)
