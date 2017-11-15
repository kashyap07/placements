drop table if exists postLog;
CREATE TABLE postLog (
  slno Integer NOT NULL ,
  stud_id varchar(15) Not Null ,
  LastPost Timestamp Not Null Default CURRENT_TIMESTAMP,
  Message varchar(200),
  primary key(slno),
  foreign key(stud_id) REFERENCES Student(stud_id)
);


