#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.user import User
from models.task import Task
from models.group import Group

print("-- User --")
print("All objects: {}".format(storage.count()))
print("User objects: {}".format(storage.count(User)))

first_user_id = list(storage.all(User).values())[0].id
print("First user: {}".format(storage.get(User, first_user_id)))

print("-- Task --")
print("All objects: {}".format(storage.count()))
print("Task objects: {}".format(storage.count(Task)))

first_task_id = list(storage.all(Task).values())[0].id
print("First task: {}".format(storage.get(Task, first_task_id)))

print("-- Group --")
print("All objects: {}".format(storage.count()))
print("Group objects: {}".format(storage.count(Group)))

first_group_id = list(storage.all(Group).values())[0].id
print("First group: {}".format(storage.get(Group, first_group_id)))
