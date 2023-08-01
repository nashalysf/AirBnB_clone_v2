-- setting the MySQL test server for AirBnB project

-- creating db
CREATE DATABASE IF NOT EXISTS hbnb_test_db;

-- creating user
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- granting user all privileges on hbnb test db
GRANT ALL PRIVILEGES ON 'hbnb_test_db'.* TO 'hbnb_test'@'localhost';

-- granting view privileges on performance db
GRANT SELECT ON 'performance_schema'.* TO 'hbnb_test'@'localhost';

-- applies permission's update without restarting server
FLUSH PRIVILEGES;