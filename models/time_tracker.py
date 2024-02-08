#!/usr/bin/python3
"""Record time spent on a task by tracking time to start and time to end."""

from models.base_model import BaseModel

class TimeTracker(BaseModel):
    """
    TimeTracker
    
    Records the time spent on a task by capturing start and end
    
    Public class attributes
        - task_id (str): Unique identifier for a task.
        - user_id (str): Unique identifier for a user.
        - time_start (str): Starting time for a task.
        - time_end (str): Ending time for a task.
        
    Public class method
        - track_time_spent(self, time_start, time_end): Records the time spent on a task by capturing start and end.
    """
    task_id = ""
    user_id = ""
    time_start = ""
    time_end = ""
    
    def __init__(self, *args, **kwargs):
        """Initialize TimeTracker class"""
        super().__init__(*args, **kwargs)
