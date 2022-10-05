.read data.sql


CREATE TABLE bluedog AS
  SELECT color,pet from students where color="blue" and pet="dog";

CREATE TABLE bluedog_songs AS
  SELECT color,pet,song from students where color="blue" and pet="dog";


CREATE TABLE smallest_int_having AS
  SELECT time,smallest from students group by smallest having count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT a.pet,a.song,a.color,b.color from students as a,students as b where a.time!=b.time and a.pet=b.pet and a.song=b.song;


CREATE TABLE sevens AS
  SELECT seven from students,numbers where students.time=numbers.time and numbers."7"="True" and students.number=7;


CREATE TABLE avg_difference AS
  SELECT round(avg(abs(number-smallest))) from students;

