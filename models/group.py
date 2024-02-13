#!/usr/bin/bash
"""Group class takes care of creating groups and keeping track of list of tasks."""

import models
import uuid
from models.base_model import BaseModel, Base
from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey, DateTime, Table


"""group_users_association = Table(
        'group_users', Base.metadata,
        Column('group_id', String(60), ForeignKey("groups.id"), 
               nullable=False, primary_key=True),
        Column('user_id', String(60), ForeignKey("users.id"), 
               nullable=False, primary_key=True)
    )
"""

class Group(BaseModel, Base):
    """
    Group class
    
    Takes care of creating groups and keeping track of list of tasks.
    
    Public instance attributes
        - group_id (str): The unique identifier of the group.
        - group_name (str): The name of the group.
        - group_users (lists): List of all users in the group.
        - group_task (lists): List of tasks assigned to the group.
        - task_description (str): Task for the group.
    
    Public instance methods
        - create_group(self, group_id, group_name): Creates a new group with a unique identifier and name.
        - add_user_to_group(self, group_id, user_id):  Adds a user to the group.
        - remove_user_from_group(self, group_id, user_id): Remove user from the group.
        - assign_task_to_group(self, group_id, group_task):  Assigns a task to the group.
    """
    if models.sqlStorage_t == "db":
        __tablename__ = "groups"
        group_name = Column(String(128), nullable=False)
        # task_id = Column(String(60), ForeignKey("tasks.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"))
        # Associated with the table
        users = relationship("User", back_populates="groups", single_parent=True, cascade="all, delete, delete-orphan")
    else:
        group_name = ""
    
    def __init__(self, *args, **kwargs):
        """
        Initialize a new Group instance.
        
        Args:
            - *args
            - **kwargs
        """
        super().__init__(*args, **kwargs)
        
    def create_group(self, group_id, group_name):
        """
        Creates group using group_id and group_name
        
        Args:
            - group_id (str): Group's unique identifier.
            - group_name (str): Group name.
        """
        # Generate a unique group_id using uuid.uuid4()
        self.group_id = group_id
        self.group_name = group_name
        self.save()
    
    def add_user_to_group(self, group_id ,user_id):
        """
        Adds a user to a specific group.
        
        Args:
            - group_id (str): Group unique identifier.
            - user_id (str): User unique identifier.
        """
        if group_id is not None:
            self.group_users.append(user_id)
            
        self.save()
    
    def remove_user_from_group(self, group_id, user_id):
        """
        Removes a user from a specific group.
        
        Args:
            - group_id (str): Group unique identifier.
            - user_id (str): User unique identifier.
        """
        if group_id is not None:
            self.group_users.remove(user_id)
            
    def create_group_task(self, group_id, task_description):
        """
        Creates a group task and associates it with the specified group.

        Args:
            - group_id (str): Group unique identifier.
            - task_description (str): Description of the task.

        Returns:
            - str: Message indicating the success or failure of the task creation.
        """
        if group_id not in self.group_tasks:
            self.group_tasks[group_id] = [task_description]
        else:
            self.group_tasks[group_id].append(task_description)

        return f"Task '{task_description}' created successfully for group '{group_id}'."
    
    def assign_task_to_group(self, group_id, group_task):
        """
        Assigns task to a specific group.
        
        Args:
            - group_id (str): Group unique identifier.
            - group_task (str): Task for the group.
        """
        if group_id not in self.group_tasks:
            self.group_tasks[group_id] = [group_task]
        else:
            self.group_tasks[group_id].append(group_task)
