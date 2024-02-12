#!/usr/bin/env bash

echo 'all' | TASK_MYSQL_USER=task_dev TASK_MYSQL_PWD=task_dev_pwd TASK_MYSQL_HOST=localhost TASK_MYSQL_DB=task_dev_db TASK_TYPE_STORAGE=db ./console.py
