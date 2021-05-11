CREATE USER '';
--Create all required users and permissions for ip access

GRANT ALL ON '%'.* TO 'x'
FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS zoomDB DEFAULT CHARSET=uft8;
USE zoomDB;
CREATE TABLE user (
    userEmail   VARCHAR(250) NOT NULL, 
    userPassword    VARCHAR(128) NOT NULL,
    userName    VARCHAR(50) NOT NULL, 
    PRIMARY KEY(userEmail)
);
