-- Create the database (task_test_db) if it doesn't exit.
CREATE DATABASE IF NOT EXISTS task_test_db;

-- Create user for task_test_db, if it doesn't exit create it and set password.
CREATE USER IF NOT EXISTS 'task_test'@'localhost' IDENTIFIED BY 'task_test_pwd';

-- Grant all privileges on task_test_db to the user task_test
GRANT ALL PRIVILEGES ON task_test_db.* TO 'task_test'@'localhost';

-- Grant SELECT privilege on performance_schema to the user task_dev
GRANT SELECT ON performance_schema.* TO 'task_test'@'localhost';
