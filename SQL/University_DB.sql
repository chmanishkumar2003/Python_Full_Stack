USE University;

CREATE TABLE Department (
    dep_id INT PRIMARY KEY AUTO_INCREMENT,
    dep_name VARCHAR(100) NOT NULL UNIQUE
);

insert into Department(dep_id,dep_name)
Values
(1,"CSE"),
(2,"ECE"),
(3,"CSE-AI/ML"),
(4,"CSBS"),
(5,"MECHANICAL");