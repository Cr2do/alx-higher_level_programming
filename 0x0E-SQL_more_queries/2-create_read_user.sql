-- Write a script that deletes the database hbtn_0c_0 in your MySQL server.
CREATE DATABASE IF NOT EXISTS user_0d_2;
CREATE USER IF NOT EXISTS `user_0d_2`@`localhost` IDENTIFIED BY "user_0d_2_pwd";
GRANT SELECT on `hbtn_0d_2`.* TO `user_0d_2`@`localhost`;
