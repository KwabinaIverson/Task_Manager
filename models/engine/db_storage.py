#!/usr/bin/bash

from os import environ
from sqlalchemy import (create_engine)
from models.base_model import Base
from models.group import Group
from models.task import Task
from models.user import User
from sqlalchemy.orm import scoped_session
from sqlalchemy.orm import sessionmaker

class DBStorage:
    """Storage for FileStorage and Mysql"""
    __engine = None
    __session = None
    
    def __init__(self):
        
        sqlUser = environ.get('TASK_MYSQL_USER')
        sqlPwd = environ.get('TASK_MYSQL_PWD')
        sqlHost = environ.get('TASK_MYSQL_HOST')
        sqlDB = environ.get('TASK_MYSQL_DB')
        sqlEnv = environ.get('TASK_ENV')
        
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(sqlUser, sqlPwd, sqlHost, sqlDB),
                                      pool_pre_ping=True)
        
        if sqlEnv == "test":
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
        session = self.__session
        dic = {}
        if not cls:
            tables = [User, Task, Group]
        else:
            if type(cls) == str:
                cls = eval(cls)
            
            tables = cls
            
        for table in tables:
            query = session.query(table).all()
            
            for rows in query:
                key = "{}.{}".format(type(rows).__name__, rows.id)
                dic[key] = rows
        
        return dic
    
    def new(self, obj):
        """
        Adds the object to the current database session.
        
        Argument:
            - obj (object): Information to be added to database session.
        """
        if obj:
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
        if obj:
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
