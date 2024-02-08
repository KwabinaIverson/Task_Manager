#!/usr/bin/python3
"""
TaskManager class stores all list of task.
"""

from models.base_model import BaseModel

class TaskManager(BaseModel):
    """
    Stores all list of tasks created in a list.
    
    Public class attribute.
        - tasks (list/array): Store tasks created.
    
    Public instance methods.
        - add_task(self, task_details): Add a task to a list of tasks.
        - edit_task(self, task_id, new_details): Edit an exiting task.
        - delete_task(self, task_id): Removes specific task from the list.
    """
    tasks = []
    
    def __init__(self, *args, **kwargs):
        """Initiate Task Manager class and inherit from BaseModel"""
        super().__init__(*args, **kwargs)
        
    def add_task(self, task_details):
        """
        Adds a new task to the list of tasks.

        Parameters
        - task_details (str): Details of the new task.
        """
        TaskManager.tasks.append(task_details)
