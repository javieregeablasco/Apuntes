-- Crear base de datos
CREATE DATABASE IF NOT EXISTS instituto;
USE instituto;

-- Tabla principal: alumnos
DROP TABLE IF EXISTS alumnos;
CREATE TABLE alumnos (
    id_alumno INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    apellido VARCHAR(50) NOT NULL
);

-- Tabla secundaria: notas (relacionada con alumnos)
DROP TABLE IF EXISTS notas;
CREATE TABLE notas (
    id_nota INT AUTO_INCREMENT PRIMARY KEY,
    id_alumno INT NOT NULL,
    asignatura VARCHAR(50) NOT NULL,
    nota DECIMAL(4,2) NOT NULL,
    FOREIGN KEY (id_alumno) REFERENCES alumnos(id_alumno)
);

-- Insertar 100 alumnos con datos de ejemplo
INSERT INTO alumnos (nombre, apellido)
	VALUES ("Carla","Pérez"), ("Luis","Gracia"), ("Ana","Roig"), ("María","Cabrera"), ("Carmen","López"),
			("Pedro","Jiménez"), ("Clarisa","Vázquez"), ("Carlos","Carolo"), ("Francisco","Gómez"), ("Luisa","López"),
            ("Carlota","Pérez"), ("Antonio","García"), ("M. José","Ruiz"), ("Mónica","Díaz"), ("Jose Luis","García"),
            ("Iker","Lafuente"), ("Javier","Lafuente"), ("Ana","Ruiz"), ("Carlos","López"), ("M. Luisa","Giner"),
            ("Perico","Gordo"), ("Lola","Monte"), ("Jorge","Ibáñez"), ("Luisito","Cabrera"), ("Lola","Flores"),
            ("Loreto","Ribo"), ("Lara","Craft"), ("Nino","Bravo"), ("Julia","Iglesias"), ("Pepito","Catedrales"),
            ("Carla","Pérez"), ("Luis","Gracia"), ("Ana","Roig"), ("María","Cabrera"), ("Carmen","López"),
			("Carlota","Pérez"), ("Antonio","García"), ("M. José","Ruiz"), ("Mónica","Díaz"), ("Jose Luis","García"),
            ("Iker","Lafuente"), ("Javier","Lafuente"), ("Ana","Ruiz"), ("Carlos","López"), ("M. Luisa","Giner"),
			("Carlota","Pérez"), ("Antonio","García"), ("M. José","Ruiz"), ("Mónica","Díaz"), ("Jose Luis","García"),
            ("Iker","Lafuente"), ("Javier","Lafuente"), ("Ana","Ruiz"), ("Carlos","López"), ("M. Luisa","Giner"),
            ("Carla","Pérez"), ("Luis","Gracia"), ("Ana","Roig"), ("María","Cabrera"), ("Carmen","López"),
			("Pedro","Jiménez"), ("Clarisa","Vázquez"), ("Carlos","Carolo"), ("Francisco","Gómez"), ("Luisa","López"),
            ("Carlota","Pérez"), ("Antonio","García"), ("M. José","Ruiz"), ("Mónica","Díaz"), ("Jose Luis","García"),
            ("Iker","Lafuente"), ("Javier","Lafuente"), ("Ana","Ruiz"), ("Carlos","López"), ("M. Luisa","Giner"),
            ("Perico","Gordo"), ("Lola","Monte"), ("Jorge","Ibáñez"), ("Luisito","Cabrera"), ("Lola","Flores"),
            ("Loreto","Ribo"), ("Lara","Craft"), ("Nino","Bravo"), ("Julia","Iglesias"), ("Pepito","Catedrales"),
            ("Carla","Pérez"), ("Luis","Gracia"), ("Ana","Roig"), ("María","Cabrera"), ("Carmen","López"),
			("Carlota","Pérez"), ("Antonio","García"), ("M. José","Ruiz"), ("Mónica","Díaz"), ("Jose Luis","García"),
            ("Iker","Lafuente"), ("Javier","Lafuente"), ("Ana","Ruiz"), ("Carlos","López"), ("M. Luisa","Giner");

-- Insertar algunas notas de ejemplo para los primeros alumnos
INSERT INTO notas (id_alumno, asignatura, nota) VALUES
(1, 'Matemáticas', 8.5),
(1, 'Historia', 7.2),
(2, 'Inglés', 9.0),
(2, 'Lengua', 6.8),
(3, 'Ciencias', 7.5),
(3, 'Matemáticas', 5.9);
