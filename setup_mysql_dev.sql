-- Setting MySQL server, creates user and applies access

-- creating db
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- creating user
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- granting user usage to all db & tables
GRANT USAGE ON *.* TO 'hbnb_dev'@'localhost';

-- granting view privileges on performance db
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_dev'@'localhost';

-- grantinng user all privileges on hbnb dev db
GRANT ALL PRIVILEGES ON 'hbnb_dev_db'.* TO 'hbnb_dev'@'localhost';

-- applies permission's update without restarting server
FLUSH PRIVILEGES;