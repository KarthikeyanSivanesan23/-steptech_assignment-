# -steptech_assignment-
Hai! Team myself S.Karthikeyan Completed Bsc computer science 
This is how I create django project according to your assignment 
first create folder Tap assignment open is vs code
open terminal type django -admin startproject Tap
cd go to project Tap
python manage.py startapp TapApp
create urls in TapApp
and python manage.py makemigrations
python manage.py migrate
edit in setting add mysql database and localhost and host number
add TapApp in app function
import views in url and make configuration 
create urls for home page 
and create function in in views for home
and create templates folder in Tap and create new_users.html ,users_list.html,edit,delet.html
create functions for html
i add some of bootstrap templates for frontend 
and push my project after completion 
And I create my Second assignment For Mysql database creation for users
CREATE DATABASE users;
USE users;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    role VARCHAR(255) NOT NULL
);
INSERT INTO users (name, email, role) VALUES
('Karthikeyan', 'karthikeyansiva@gmail.com', 'Web Developer'),
('Yazhini', 'yazhinisiva21@gmail.com', 'Bank'),
('Sivanesan', 'Sivanesansobiya@gmail.com', 'Superent'),
('Sobiya', 'sobiyasiva@gmail.com', 'Housewife');
select * from users;

