#!/usr/bin/python3
"""
Functions needed for the Task App
"""

from models.group import Group

def create_group(session, group_name, user_id):
    """
    Creates a new group in the database.

    Args:
    - session: SQLAlchemy session object
    - group_name (str): Name of the group to be created.
    - user_id (str): ID of the user who is creating the group.

    Returns:
    - Group: The created Group object.
    """
    group = Group(group_name=group_name, user_id=user_id)
    session.add(group)
    session.commit()
    return group
