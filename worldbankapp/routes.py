from worldbankapp import app
from flask import render_template
from wrangling_scripts.wrangling import data_wrangling

data = data_wrangling()

print(data)

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/project-one')
def project_one():
    return render_template('project-one.html')

@app.route('/project-two')
def project_two():
    return render_template('project-two.html')