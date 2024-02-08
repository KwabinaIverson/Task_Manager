#!/usr/bin/env bash

echo 'create User email="Iverson" password="1234354" first_name="Iverson" last_name="Kwabina"' | TASK_MYSQL_USER=task_dev TASK_MYSQL_PWD=task_dev_pwd TASK_MYSQL_HOST=localhost TASK_MYSQL_DB=task_dev_db TASK_TYPE_STORAGE=db ./console.py
