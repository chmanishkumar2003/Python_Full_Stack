USE University;

Create table Courses(
	cur_id int primary key auto_increment,
    cur_name Varchar(100) not null ,
    credits int Not null,
    dep_id int,
    foreign key (dep_id) references Department (dep_id)
    );
    
Insert into Courses(cur_id,cur_name,credits,dep_id)
values
(1250,"Maths-A",2,01),
(1251,"Maths-B",2,01),
(1414,"Chemistry",4,01),
(1560,"Physics",4,01),
(0032,"C-Language",3,01);
