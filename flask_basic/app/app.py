from flask import Flask, render_template, request, redirect, url_for

from reniec import InfoPerson
from database import InsertStudent, InsertMatricula, InsertCourses, ShowTable, GetMatriculasCursos, SearchElement, DeleteMatricula


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', courses = ShowTable("cursos"), students = ShowTable("estudiantes"), matriculas = ShowTable("matriculas"))

@app.route('/matricula',methods=['GET', 'POST'])
def matricula():
    if request.method == 'POST':
        form_type = request.form.get("form_type")
        
        if form_type == "buscar_dni":
            number_dni = request.form.get("dni")
            user_search = SearchElement(number_dni)
            if not bool(user_search):
                data_test = InfoPerson(number_dni).json()
                return render_template('matricula.html', data=data_test, cursos=[], matriculas = [], message = "No se encuentra registrado en la Escuela")
            else:
                data_test = {
                    "nombreCompleto":user_search[0][1],
                    "numeroDocumento":user_search[0][0]
                }
                list_cursos = GetMatriculasCursos(number_dni)
                list_cursos_code = [curso[2] for curso in list_cursos]
                all_cursos = ShowTable("cursos")
                enable_cursos = [
                    curso for curso in all_cursos
                    if curso[0] not in list_cursos_code and (curso[3] in list_cursos_code or curso[3] is None)
                ]
                return render_template('matricula.html', data=data_test, cursos=enable_cursos, matriculas = list_cursos, message = None)
        elif form_type == "registrar_matricula":
            curso = request.form.get("curso_id_matricula")
            dni = request.form.get("dni_matricula")
            InsertMatricula(dni, curso)
            return render_template('matricula.html', message=f"Matriculado {dni} en curso {curso}", data=None)
        elif form_type == "agregar_dni":
            data_name = request.form.get("data_name_complete")
            data_dni = request.form.get("data_dni")
            InsertStudent(data_dni, data_name)
            return render_template('matricula.html', data=None, message = f"Estudiante {data_name} registrado")
        
    return render_template('matricula.html', data=None)

@app.route('/cursoscreate')
def course():
    return render_template('courses.html')

@app.route('/desmatricular', methods=['POST'])
def matricula_cancelar():
    dni = request.form.get("matricula_dni")
    course = request.form.get("matricula_course")
    forzar = request.form.get("forzar_eliminacion")

    all_courses = ShowTable("cursos")
    cursos_matriculados = GetMatriculasCursos(dni)
    cursos_matriculados_code = [m[2] for m in cursos_matriculados]

    dependientes = [
        c[0] for c in all_courses
        if c[3] == course and c[0] in cursos_matriculados_code
    ]

    if dependientes and not forzar:
        mensaje = f"No se puede cancelar la matrícula en {course} porque es prerequisito de {dependientes}"
        return render_template('matricula.html', message=mensaje, data = None)

    # Si se forzó o no hay dependientes, eliminamos
    ids_a_eliminar = []

    if dependientes and forzar:
        for dep in dependientes:
            # Buscar la matrícula por curso
            for m in cursos_matriculados:
                if m[2] == dep:
                    ids_a_eliminar.append(m[0])  # m[0] es el id de matrícula

    # Agregar también el curso original
    for m in cursos_matriculados:
        if m[2] == course:
            ids_a_eliminar.append(m[0])

    # Eliminar todas las matrículas necesarias
    for id_m in ids_a_eliminar:
        DeleteMatricula(id_m)

    mensaje = f"Se canceló la matrícula en el curso {course}."
    if dependientes and forzar:
        mensaje += f" También se eliminaron: {', '.join(dependientes)}"

    data_test = InfoPerson(dni).json()
    cursos_matriculados = GetMatriculasCursos(dni)
    cursos_matriculados_code = [m[2] for m in cursos_matriculados]
    enable_cursos = [
        c for c in all_courses
        if c[0] not in cursos_matriculados_code and (c[3] in cursos_matriculados_code or c[3] is None)
    ]

    return render_template('matricula.html', data=data_test, cursos=enable_cursos, matriculas=cursos_matriculados, message=mensaje)
