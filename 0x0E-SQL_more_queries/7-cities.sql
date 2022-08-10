-- Write a script that deletes the database hbtn_0c_0 in your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities (id INT UNIQUE NOT NULL AUTO_INCREMENT, state_id INT NOT NULL ,name state_idVARCHAR(256), CONSTRAINT id_pk PRIMARY KEY (id), FOREIGN KEY (state_id) REFERENCES State(id));
