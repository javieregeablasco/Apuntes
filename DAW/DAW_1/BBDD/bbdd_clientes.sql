CREATE SCHEMA alumnos;
USE alumnos;

drop table if exists clientes;

CREATE TABLE clientes (
	id INT AUTO_INCREMENT PRIMARY KEY,
    name varchar(255) not null,
    age int default 20 not null,
    ciudad varchar(255) not null,
    fecha DATE DEFAULT (CURDATE()),
    hora TIME default (current_time()),
    CONSTRAINT chk_mayor_de_edad check (age >= 18)
);

INSERT INTO clientes (name, age, ciudad) values
('Juan', 25, 'Madrid'),
('Maria', 30, 'Barcelona'),
('Pedro', 35, 'Madrid'),
('Ana', 28, 'Barcelona'),
('Luis', 22, 'Madrid'),
('Sofia', 27, 'Barcelona'), 
('Carlos', 31, 'Madrid'),
('Laura', 29, 'Barcelona'),
('Jorge', 26, 'Madrid'),
('Marta', 24, 'Barcelona'), 
('Diego', 32, 'Madrid'),
('Lucia', 27, 'Barcelona'),
('Alberto', 29, 'Madrid'),
('Sara', 26, 'Barcelona'),  
('Andres', 30, 'Madrid'),
('Isabel', 28, 'Barcelona'),
('Fernando', 27, 'Madrid'),
('Carmen', 25, 'Barcelona'),
('Rafael', 31, 'Madrid'), 
('Elena', 29, 'Barcelona'),
('Sergio', 26, 'Madrid'),
('Patricia', 28, 'Barcelona'),
('Javier', 30, 'Madrid'),
('Miriam', 27, 'Barcelona'),
('Oscar', 29, 'Madrid'),
('Vanessa', 26, 'Barcelona');

SELECT * FROM clientes;
DESCRIBE clientes;