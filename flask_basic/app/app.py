from flask import Flask, render_template, request

from reniec import InfoPerson
from database import InsertStudent, InsertMatricula, InsertCourses, ShowTable 

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', courses = ShowTable("cursos"), students = ShowTable("estudiantes"), matriculas = ShowTable("matriculas"))
@app.route('/matricula')
def matricula():
    return render_template('matricula.html')
@app.route('/matricula', methods = ['POST'])
def dni():        
    return render_template('matricula.html')
