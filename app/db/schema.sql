drop table if exists entries;
create table entries (
  id integer primary key autoincrement,
  title text not null,
  'text' text not null
);

create table Placement_Employee
(
	u_name varchar(10),
	password varchar(10),
	primary key(u_name)
);

create table Company
(
	comp_id varchar(10),
	comp_name varchar(20),
	address varchar(50),
	description varchar(50),
	sector varchar(20),
	tier integer,
	contact integer,
	primary key(comp_id)
);

create table Student
(
	stud_id varchar(10),
	name varchar(20),
	cgpa numeric(4,2) CHECK(cgpa <= 10 and cgpa > 0),
	sec_cgpa numeric(4,2) CHECK(sec_cgpa <= 10 and sec_cgpa > 0),
	prim_cgpa numeric(4,2) CHECK(prim_cgpa <= 10 and prim_cgpa > 0),
	contact integer,
	email varchar(20),
	backlogs integer,
	dept varchar(10),
	password varchar(10),
	primary key(stud_id)
);

create table Eligibility
(
	comp_id varchar(10),
	dept varchar(10),
	cgpa numeric(4,2) CHECK(cgpa <= 10 and cgpa > 0),
	sec_cgpa numeric(4,2) CHECK(sec_cgpa <= 10 and sec_cgpa > 0),
	prim_cgpa numeric(4,2) CHECK(prim_cgpa <= 10 and prim_cgpa > 0),
	backlogs integer,
	internship char(1),
	primary key(comp_id,dept),
	foreign key(comp_id) REFERENCES Company(comp_id)
);

create table Mode_of_Selection
(
	comp_id varchar(10),
	mode varchar(10),
	gd char(1),
	interview char(1),
	rounds integer,
	primary key(comp_id),
	foreign key(comp_id) REFERENCES Company(comp_id)
);

create table Job_Info
(
	comp_id varchar(10),
	role varchar(10),
	ctc integer,
	stipend integer,
	location varchar(50),
	jd varchar(100),
	primary key(comp_id,role),
	foreign key(comp_id) REFERENCES Company(comp_id)
);

create table Calendar
(
	comp_id varchar(10),
	date DATETIME,
	purpose varchar(50),
	primary key(comp_id, date),
	foreign key(comp_id) REFERENCES Company(comp_id)
);

create table Registered
(
	stud_id varchar(10),
	comp_id varchar(10),
	primary key(stud_id, comp_id)	
);

create table Placed
(
	stud_id varchar(10),
	comp_id varchar(10),
	ftjob char(1),
	internship char(1),
	role varchar(10),
	primary key(stud_id, comp_id),
	foreign key(stud_id) REFERENCES Student(stud_id),
	foreign key(comp_id) REFERENCES Company(comp_id)
);
