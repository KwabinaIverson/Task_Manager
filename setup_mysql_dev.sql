-- Create the database task_dev_db if it doesn't exit.
CREATE DATABASE IF NOT EXISTS task_dev_db;

-- Create user (task_dev) if doesn't exit and set password.
CREATE USER IF NOT EXISTS 'task_dev'@'localhost' IDENTIFIED BY 'task_dev_pwd';

-- Grant all privileges on task_dev_db to the user task_dev
GRANT ALL PRIVILEGES ON task_dev_db.* TO 'task_dev'@'localhost';

-- Grant SELECT privilege on performance_schema to the user task_dev
GRANT SELECT ON performance_schema.* TO 'task_dev'@'localhost';
