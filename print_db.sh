#!/usr/bin/env bash

echo 'SELECT * FROM tasks\G' | mysql -u task_dev -p task_dev_db
