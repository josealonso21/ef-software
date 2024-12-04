CREATE DATABASE IF NOT EXISTS ticketing_db;

USE ticketing_db;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255),
    status VARCHAR(20) DEFAULT 'available',
    user_id INT DEFAULT NULL
);

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);