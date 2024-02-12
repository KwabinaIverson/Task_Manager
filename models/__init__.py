#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv
import models

sqlStorage_t = getenv("TASK_TYPE_STORAGE")

if sqlStorage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()