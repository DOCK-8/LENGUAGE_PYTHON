-- Crear base de datos (opcional si usas SQLite)
CREATE DATABASE IF NOT EXISTS sistema_matricula;
USE sistema_matricula;

-- Tabla de estudiantes
CREATE TABLE estudiantes (
    dni CHAR(8) PRIMARY KEY,
    nombres VARCHAR(100) NOT NULL
);

-- Tabla de cursos
CREATE TABLE cursos (
    codigo VARCHAR(10) PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    creditos INT NOT NULL,
    prerequisito VARCHAR(10),
    FOREIGN KEY (prerequisito) REFERENCES cursos(codigo)
);

-- Tabla de matrículas
CREATE TABLE matriculas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni CHAR(8),
    codigo_curso VARCHAR(10),
    fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (dni) REFERENCES estudiantes(dni),
    FOREIGN KEY (codigo_curso) REFERENCES cursos(codigo)
);

-- Insertar 10 cursos de ejemplo
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
