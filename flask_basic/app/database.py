import mysql.connector

# TABLES:
# matriculas
# +--------------+-------------+------+-----+-------------------+-------------------+
# | Field        | Type        | Null | Key | Default           | Extra             |
# +--------------+-------------+------+-----+-------------------+-------------------+
# | id           | int         | NO   | PRI | NULL              | auto_increment    |
# | dni          | char(8)     | YES  | MUL | NULL              |                   |
# | codigo_curso | varchar(10) | YES  | MUL | NULL              |                   |
# | fecha        | timestamp   | YES  |     | CURRENT_TIMESTAMP | DEFAULT_GENERATED |
# +--------------+-------------+------+-----+-------------------+-------------------+
# cursos
# +--------------+--------------+------+-----+---------+-------+
# | Field        | Type         | Null | Key | Default | Extra |
# +--------------+--------------+------+-----+---------+-------+
# | codigo       | varchar(10)  | NO   | PRI | NULL    |       |
# | nombre       | varchar(100) | NO   |     | NULL    |       |
# | creditos     | int          | NO   |     | NULL    |       |
# | prerequisito | varchar(10)  | YES  | MUL | NULL    |       |
# +--------------+--------------+------+-----+---------+-------+
# estudiantes
# +---------+--------------+------+-----+---------+-------+
# | Field   | Type         | Null | Key | Default | Extra |
# +---------+--------------+------+-----+---------+-------+
# | dni     | char(8)      | NO   | PRI | NULL    |       |
# | nombres | varchar(100) | NO   |     | NULL    |       |
# +---------+--------------+------+-----+---------+-------+
    
enviroments = {
    "user" : "root",
    "password" : "root",
    "host" : "database",
    "database" : "sistema_matricula"
}

def ShowTable(name):
    my_sql = mysql.connector.connect(**enviroments)
    if my_sql.is_connected():
        print("Se conecto")
        cursor = my_sql.cursor()
        cursor.execute(f'SELECT * FROM {name}')
        rows = cursor.fetchall()
        my_sql.close()
        return rows
    else:
        print("No conecto")

def SearchElement(content):
    my_sql = mysql.connector.connect(**enviroments)
    if my_sql.is_connected():
        print("Se conecto")
        cursor = my_sql.cursor()
        cursor.execute(f'SELECT * FROM estudiantes WHERE dni = %s',(content,))
        rows = cursor.fetchall()
        my_sql.close()
        return rows
    else:
        print("No conecto")

def GetMatriculasCursos(dni):
    my_sql = mysql.connector.connect(**enviroments)
    if my_sql.is_connected():
        print("Se conecto")
        cursor = my_sql.cursor()
        cursor.execute(f'SELECT codigo_curso,dni,fecha FROM matriculas WHERE dni = {dni}')
        rows = cursor.fetchall()
        my_sql.close()
        return rows
    else:
        print("No conecto")

def InsertElement(instruction, data):
    my_sql = mysql.connector.connect(**enviroments)
    if my_sql.is_connected():
        print("Se conecto")
        cursor = my_sql.cursor()
        cursor.execute(instruction, data)
        my_sql.commit()
        my_sql.close()
    else:
        print("No conecto")

def InsertStudent(dni, nombre):
    instruction = ("INSERT INTO estudiantes"
        "(dni, nombres) "
        "VALUES (%s, %s)")
    datas = (dni, nombre)
    InsertElement(instruction, datas)

def InsertCourses(id, nombre, creditos, pre):
    instruction = ("INSERT INTO cursos "
           "(codigo, nombre, creditos, prerequisito) "
           "VALUES (%s, %s, %s, %s)")
    datas = (id, nombre, creditos, pre)
    InsertElement(instruction, datas)

def InsertMatricula(dni, code):
    instruction = ("INSERT INTO matriculas "
           "(dni, codigo_curso) "
           "VALUES (%s, %s)")
    datas = (dni, code)
    InsertElement(instruction, datas)
