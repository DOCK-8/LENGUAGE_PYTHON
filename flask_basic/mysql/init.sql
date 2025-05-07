-- Crear base de datos y usarla
CREATE DATABASE IF NOT EXISTS sistema_matricula;
USE sistema_matricula;

-- Crear tabla de estudiantes
CREATE TABLE estudiantes (
    dni CHAR(8) PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL
);

-- Crear tabla de cursos
CREATE TABLE cursos (
    codigo VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    creditos INT NOT NULL,
    prerequisito VARCHAR(10),
    FOREIGN KEY (prerequisito) REFERENCES cursos(codigo)
);

-- Crear tabla de matrículas
CREATE TABLE matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni CHAR(8),
    codigo_curso VARCHAR(10),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dni) REFERENCES estudiantes(dni),
    FOREIGN KEY (codigo_curso) REFERENCES cursos(codigo)
);

-- Insertar cursos
INSERT INTO cursos (codigo, nombre, creditos, prerequisito) VALUES
('CS101', 'Introducción a la programación', 4, NULL),
('CS102', 'Estructuras de datos', 4, 'CS101'),
('CS103', 'Sistemas operativos', 3, 'CS102'),
('CS104', 'Base de datos', 4, 'CS101'),
('CS105', 'Redes', 3, 'CS102'),
('CS106', 'Inteligencia Artificial', 4, 'CS102'),
('CS107', 'Computación gráfica', 3, 'CS102'),
('CS108', 'Desarrollo web', 4, 'CS101'),
('CS109', 'Seguridad informática', 3, 'CS102'),
('CS110', 'Ingeniería de software', 3, 'CS101');

-- Insertar estudiantes
INSERT INTO estudiantes (dni, nombres) VALUES
('12345678', 'Juan Pérez'),
('87654321', 'María Gómez'),
('11223344', 'Luis Torres'),
('22334455', 'Ana Ramírez'),
('33445566', 'Carlos Mendoza');

-- Insertar matrículas anteriores

-- Juan Pérez
INSERT INTO matriculas (dni, codigo_curso) VALUES
('12345678', 'CS101'),
('12345678', 'CS102'),
('12345678', 'CS104');

-- María Gómez
INSERT INTO matriculas (dni, codigo_curso) VALUES
('87654321', 'CS101'),
('87654321', 'CS108'),
('87654321', 'CS110');

-- Luis Torres
INSERT INTO matriculas (dni, codigo_curso) VALUES
('11223344', 'CS101'),
('11223344', 'CS102'),
('11223344', 'CS103'),
('11223344', 'CS106');

-- Ana Ramírez
INSERT INTO matriculas (dni, codigo_curso) VALUES
('22334455', 'CS101'),
('22334455', 'CS102'),
('22334455', 'CS105');

-- Carlos Mendoza
INSERT INTO matriculas (dni, codigo_curso) VALUES
('33445566', 'CS101'),
('33445566', 'CS108');
