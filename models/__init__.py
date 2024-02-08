#!/usr/bin/python3

from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage
from models.base_model import BaseModel
from models.user import User
from models.task import Task
from models.group import Group
from os import environ

# Check Database type
sqlStorage = environ.get('TASK_TYPE_STORAGE')

if sqlStorage == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
