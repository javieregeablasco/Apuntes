USE miprimerabbDD;
/*
-- DROP DATABASE IF EXISTS miprimerabbdd; 
DROP TABLE IF EXISTS teacher, course;
DROP SCHEMA if exists miprimerabbdd; 

create SCHEMA miprimeraBBDD;
use miprimeraBBDD;

-- DDL data definition languaje

CREATE TABLE teacher (
	-- id INT  AUTO_INCREMENT NOT NULL,
	id INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
	-- PRIMARY KEY (id),
	name VARCHAR(255),
	surname VARCHAR(255)
);

CREATE TABLE course (
    name VARCHAR(255) NOT NULL PRIMARY KEY,
    hours INT,
    classroom VARCHAR(255),
    vacations VARCHAR(255),
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teacher(id)
);

-- DML data modification lenguajecourse

INSERT INTO teacher (name, surname) VALUES
('Alberto', 'Garcia'),
('Beatriz', 'Lopez'),
('Carmen', 'Martin');

INSERT INTO course (name, hours, classroom, vacations,teacher_id) VALUES
-- INSERT INTO course VALUES
('Math',100,'A1','2 weeks',1),
('Programmming',150,'B1','3 weeks',2),
('Computer science',150,'B1','3 weeks',2),
('English',50,'A2','1 week',1),
('Physics',200,'C1','4 weeks',1),
('Chemistry',100,'Lab1','2 weeks',3);


-- SQL queries

SELECT * FROM teacher;
SELECT hours, teacher_id FROM course;
SELECT 3*5;

SELECT * FROM course ORDER BY hours;
SELECT * FROM course ORDER BY hours DESC;
SELECT * FROM course ORDER BY hours DESC LIMIT 3;
-- tipo numerico 
SELECT name, hours FROM course WHERE hours >=100 ORDER BY hours ASC;
SELECT name, hours FROM course WHERE hours BETWEEN 100 AND 150 ORDER BY hours ASC;
-- tipo varchar
SELECT * FROM course WHERE classroom = 'B1';
-- tipo varchar cualquier caracter
SELECT * from course WHERE classroom LIKE '_1'; -- solo un caracter
SELECT * from course WHERE classroom LIKE '%2'; -- infinidad de caracteres
SELECT * FROM course WHERE name LIKE '%is%';

-- consultas de agregacion
SELECT classroom FROM course;
SELECT count(classroom) FROM course;
SELECT count(DISTINCT classroom) FROM course;
SELECT count(DISTINCT classroom) AS 'Total clases' FROM course;

SELECT sum(hours) as 'Total horas' FROM course;
SELECT avg(hours) as 'Media horas' FROM course;
SELECT max(hours) FROM course;
SELECT * FROM course where hours = (select max(hours) FROM course);
SELECT * FROM course ORDER BY hours DESC LIMIT 1 ;

SELECT teacher_id, sum(hours) AS 'Total horas' FROM course GROUP BY teacher_id; 
SELECT teacher_id, sum(hours) AS 'Total horas' FROM course GROUP BY teacher_id HAVING sum(hours)>200; 
SELECT teacher_id, sum(hours) AS `Total horas` FROM course GROUP BY teacher_id HAVING `Total horas`>200; 
SELECT teacher_id, sum(hours) AS Total_horas FROM course GROUP BY teacher_id HAVING Total_horas>200; 

-- joins
-- permite hacer consultas sobre varias tablas
SELECT * FROM course JOIN teacher ON course.teacher_id = teacher.id;
-- para simplificar se usan aliases
SELECT * 
FROM course c
JOIN teacher t  ON c.teacher_id = t.id;

-- se pueden usar los aliases con caracter retroactivo
SELECT c.name, c.hours, c.classroom, t.name AS teacher_name, t.surname
FROM course c
JOIN teacher t  ON c.teacher_id = t.id;

-- con LETF y RIGHT podemos hacer joints sobre campos vacíos
SELECT c.name, c.hours, c.classroom, t.name AS teacher_name, t.surname
FROM course c
RIGHT JOIN teacher t  ON c.teacher_id = t.id;

-- añadir profesor
INSERT INTO teacher(name, surname) VALUES
('Daniel','Hernandez');

-- añadir curso
-- INSERT INTO course(name, hours, classroom, vacations,teacher_id) VALUES
-- ('History',200,'C1','4 weeks',NULL);

INSERT IGNORE INTO course() VALUES
('History',200,'C1','4 weeks',NULL);

-- joint con registros vacios
SELECT c.name, c.hours, c.classroom, t.name AS teacher_name, t.surname
FROM course c
RIGHT JOIN teacher t  ON c.teacher_id = t.id;

SELECT c.name, c.hours, c.classroom, t.name AS teacher_name, t.surname
FROM course c
LEFT JOIN teacher t  ON c.teacher_id = t.id;

SELECT c.name, c.hours, c.classroom, t.name AS teacher_name, t.surname
FROM course c
LEFT JOIN teacher t  ON c.teacher_id = t.id 
WHERE c.hours > 100;

SELECT t.name, sum(c.hours) as Total_hours
FROM course c
RIGHT JOIN teacher t ON c.teacher_id = t.id
GROUP BY t.name; 

SELECT t.name, t.surname, sum(c.hours) as Total_hours
FROM course c
RIGHT JOIN teacher t ON c.teacher_id = t.id
GROUP BY t.name, t.surname; 

*/
-- alterar campos en las bases de datos
-- DDL version 2
SELECT * FROM course;
ALTER TABLE course DROP mandatory;
ALTER TABLE course ADD mandatory BOOL NOT NULL;
SET SQL_SAFE_UPDATES = 0;
UPDATE course SET mandatory = TRUE;
SET SQL_SAFE_UPDATES = 1;

-- las buenas practicas indican que donde hay un update debe haber un where
ALTER TABLE course ADD mandatory BOOL;
UPDATE course set mandatory = TRUE WHERE hours>=150;

-- consulta sobre booleano
SELECT * from course WHERE mandatory = TRUE;
SELECT * FROM course WHERE mandatory IS NOT NULL;

-- cambiar valores retornados de una consula (no altera valores)
SELECT name AS Nombre, coalesce(mandatory, 'No hay datos') AS 'Campo obligatorio' FROM course; 

-- eliminar campo entero
ALTER TABLE course DROP COLUMN mandatory;
-- ALTER TABLE course DROP mandatory; -- tambien funciona 

-- vaciar una tabla entera:
-- TRUNCATE TABLE course;
-- eliminar una tabla
-- DROP TABLE course;

-- Eliminar un registro de una tabla
DELETE FROM course WHERE teacher_id= 1;