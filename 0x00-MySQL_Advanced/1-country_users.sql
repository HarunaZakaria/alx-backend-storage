--Write a SQL script that creates a table users following these requirements:
--id, name, email, and country.
CREATE TABLE IF NOT EXISTS users (
  id INT NOT NULL AUTO_INCREMENT,
  email VARCHAR(255) UNIQUE NOT NULL,
  name VARCHAR(255),
  country ENUM('US', 'CO', 'TN') DEFAULT 'US' NOT NULL
  PRIMARY KEY(id) 
);
