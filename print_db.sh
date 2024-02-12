#!/usr/bin/env bash

echo 'SELECT * FROM users\G' | mysql -u task_dev -p task_dev_db
