#!/usr/bin/bash

import models
import sqlalchemy
from os import getenv
from sqlalchemy import create_engine
from models.base_model import BaseModel, Base
from models.group import Group
from models.task import Task
from models.user import User
from sqlalchemy.orm import scoped_session, sessionmaker

classes = {"User": User, "Task": Task, "Group": Group,}

class DBStorage:
    """Storage for FileStorage and Mysql"""
    __engine = None
    __session = None
    
    def __init__(self):
        
        TASK_MYSQL_USER = getenv('TASK_MYSQL_USER')
        TASK_MYSQL_PWD= getenv('TASK_MYSQL_PWD')
        TASK_MYSQL_HOST = getenv('TASK_MYSQL_HOST')
        TASK_MYSQL_DB = getenv('TASK_MYSQL_DB')
        TASK_ENV = getenv('TASK_ENV')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(TASK_MYSQL_USER,
                                             TASK_MYSQL_PWD,
                                             TASK_MYSQL_HOST,
                                             TASK_MYSQL_DB),
                                      pool_pre_ping=True)
        
        if TASK_ENV == "test":
            Base.metadata.drop_all(bind=self.__engine)
            
    def all(self, cls=None):
        """
        Queries on the current database session (self.__session) 
        all objects depending of the class name (argument cls).
        
        Argument:
            - cls (class): Classes created in the program.
        
        Return:
            - This method returns a dictionary (like FileStorage).
        """
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)
    
    def new(self, obj):
        """
        Adds the object to the current database session.
        
        Argument:
            - obj (object): Information to be added to database session.
        """
        self.__session.add(obj)
            
    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()
        
    def delete(self, obj=None):
        """
        Delete from the current database session.
        
        Argument:
            - obj (object): Information to be added to database session.
        """
        if obj is not None:
            self.__session.delete(obj)
            
    def reload(self):
        """
        Creates all tables in the database.
        Creates the current database session.
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()
        
    def close(self):
        """
        Closes Session
        """
        self.__session.close()

    def get(self, cls, id):
        """Retrieves an object of a class with id"""
        obj = None
        if cls is not None and issubclass(cls, BaseModel):
            obj = self.__session.query(cls).filter(cls.id == id).first()
        return obj

    def count(self, cls=None):
        """Retrieves the number of objects of a class or all (if cls==None)"""
        return len(self.all(cls))
