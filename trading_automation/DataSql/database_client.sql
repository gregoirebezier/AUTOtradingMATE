CREATE DATABASE crypto_client;

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    api_key VARCHAR(255), 
    api_secret VARCHAR(255), 
    email VARCHAR(255)
);