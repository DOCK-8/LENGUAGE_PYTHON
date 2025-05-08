from flask import Flask, render_template, request

from reniec import InfoPerson
from database import InsertStudent, InsertMatricula, InsertCourses, ShowTable, GetMatriculasCursos 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', courses = ShowTable("cursos"), students = ShowTable("estudiantes"), matriculas = ShowTable("matriculas"))

@app.route('/matricula', methods=['GET', 'POST'])
def matricula():
    if request.method == 'POST':
        form_type = request.form.get("form_type")
        
        if form_type == "buscar_dni":
            number_dni = request.form.get("dni")
            data_test = InfoPerson(number_dni).json()
            list_cursos = GetMatriculasCursos(number_dni)
            all_cursos = ShowTable("cursos")
            enable_cursos = [
                curso for curso in all_cursos
                if curso[0] not in list_cursos and (curso[3] in list_cursos or curso[3] is None)
            ]
            return render_template('matricula.html', data=data_test, cursos=enable_cursos)

        elif form_type == "registrar_matricula":
            curso = request.form.get("curso_id_matricula")
            dni = request.form.get("dni_matricula")
            InsertMatricula(dni, curso)
            return render_template('matricula.html', message=f"Matriculado {dni} en curso {curso}", data=None)
        elif form_type == "agregar_dni":
            data_name = request.form.get("data_name")+" "+request.form.get("data_firstname")+" "+request.form.get("data_secondname")
            data_dni = request.form.get("data_dni")
            InsertStudent(data_dni, data_name)
            return render_template('matricula.html', data=None, message = f"Estudiante {data_name} registrado")

    return render_template('matricula.html', data=None)

@app.route('/cursoscreate')
def course():
    return render_template('courses.html')
