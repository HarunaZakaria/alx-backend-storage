--Write a SQL script that creates a table users with the following
--name, email, and id
CREATE TABLE IF NOT EXISTS users (
  id int PRIMARY KEY AUTOINCREMENT NOT NULL,
  email varchar(255) UNIQUE NOT NULL,
  name varchar(255) 
)
