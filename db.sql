CREATE DATABASE fastApiShule;

USE fastApiShule;

CREATE TABLE users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100)
);

-- create the tables for the system of house management 
CREATE TABLE houses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  location VARCHAR(100),
  price INT
);
