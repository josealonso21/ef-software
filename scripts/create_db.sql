CREATE DATABASE IF NOT EXISTS ticketing;
USE ticketing;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255)
);

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    event_name VARCHAR(255),
    status VARCHAR(50) DEFAULT 'available',
    user_id INT,
    FOREIGN KEY (user_id) REFERENCES users(id)
);