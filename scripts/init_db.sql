CREATE DATABASE IF NOT EXISTS ticketing_db;

USE ticketing_db;

CREATE TABLE tickets (
    id INT AUTO_INCREMENT PRIMARY KEY,
    conciertoname VARCHAR(255) NOT NULL,
    precio DECIMAL(10,2) NOT NULL,
    status VARCHAR(20) NOT NULL DEFAULT 'available'
);

