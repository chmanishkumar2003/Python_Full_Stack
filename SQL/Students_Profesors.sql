USE University;

Create table Student(
	stu_id int primary key auto_increment,
    First_name Varchar(100) Not null,
	Last_name Varchar(100) Not null,
    email varchar(100) unique,
    Phone Varchar(10),
    dob date,
    enrolment_date Date Null,
    status  ENUM('active','inactive','alumni') Not null  Default 'active'
);

Create table Profesors(
	pro_id int primary key auto_increment,
    pro_name Varchar(100) Not null
);
