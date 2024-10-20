CREATE DATABASE registration_db;
USE registration_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id VARCHAR(50) NOT NULL,
    mobile_number VARCHAR(15) NOT NULL,
    password VARCHAR(100) NOT NULL
);

SHOW TABLES;

DESCRIBE users;

