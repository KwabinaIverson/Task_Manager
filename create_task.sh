#!/usr/bin/env bash

# Set task parameters
TASK_NAME="Finish updating DB"
TASK_DESCRIPTION="Finish fixing error in the code"
START_DATE="2024-02-10T08:00:00.000000"
END_DATE="2024-02-10T17:00:00.000000"

# Construct the command
command="create Task task_name=\"$TASK_NAME\" task_description=\"$TASK_DESCRIPTION\" start_date=\"$START_DATE\" end_date=\"$END_DATE\""

# Execute the command
echo "$command" | TASK_MYSQL_USER=task_dev \
                TASK_MYSQL_PWD=task_dev_pwd \
                TASK_MYSQL_HOST=localhost \
                TASK_MYSQL_DB=task_dev_db \
                TASK_TYPE_STORAGE=db \
                ./console.py
