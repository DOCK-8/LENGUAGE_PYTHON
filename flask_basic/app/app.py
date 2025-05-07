from flask import Flask, render_template, request

from reniec import InfoPerson
from database import InsertStudent, InsertMatricula, InsertCourses, ShowTable, GetMatriculasCursos 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', courses = ShowTable("cursos"), students = ShowTable("estudiantes"), matriculas = ShowTable("matriculas"))
@app.route('/matricula', methods = ['GET','POST'])
def dni():        
    if request.method == 'POST':
        number_dni = request.form.get("dni")
        data_test = {
            'nombres' : 'lucas',
            'apellidoPaterno' : 'Carrion',
            'apellidoMaterno' : 'Sideral',
            'numeroDocumento' : 12345544
        }
        list_cursos = GetMatriculasCursos(number_dni)
        all_cursos = ShowTable("cursos")
        enable_cursos = []
        for curso_ava in all_cursos: 
            if curso_ava[0] not in list_cursos and (curso_ava[3] in list_cursos or curso_ava[3] is None):
                enable_cursos.append(curso_ava)
        return render_template('matricula.html', data = data_test, cursos = enable_cursos)
    return render_template('matricula.html', data = None)
@app.route('/matricula', methods = ['GET','POST'])
def matricula():
    if request.method == 'POST':
        curso = request.form.get("curso_id_matricula")
        dni = request.form.get("dni_matricula")
        return render_template('matricula.html', message = curso+dni, data = None)
    return render_template('matricula.html', data = None)

@app.route('/cursoscreate')
def course():
    return render_template('courses.html')
