CREATE DATABASE crypto_client;

CREATE TABLE clients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    api_key VARCHAR(255) NOT NULL, 
    api_secret VARCHAR(255) NOT NULL, 
    email VARCHAR(255) NOT NULL,
    MoneyToTrade INT UNSIGNED,
);