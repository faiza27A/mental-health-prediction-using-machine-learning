from jinja2 import Template
from flask import Flask, render_template,request
import numpy as np

app = Flask(__name__)
import pickle
       
@app.route('/')
def index():
    return render_template('index.html', my_title = 'Home')


@app.route('/form')
def form():
    return render_template('form.html', my_title = 'form page')

 
       
@app.route('/validate',methods=['post'])
def validate():
       
        with open('mymodel','rb') as  f:
                lr = pickle.load(f)

        Age = int(request.form.get('age'))
        Gender= int( request.form.get('gender'))
        Self_employed = int(request.form.get('self_employed'))
        Family_history = int(request.form.get('family_history'))
        Work_interface = int(request.form.get('work_interface'))
        No_employees = int(request.form.get('no_employees'))
        Remote_work = int(request.form.get('remote_work'))
        Tech_company = int(request.form.get('tech_company'))
        Benefits = int(request.form.get('benefits'))
        Care_options = int(request.form.get('care_option'))
        Wellness_Program = int(request.form.get('wellness_program'))
        Seek_help = int(request.form.get('seek_help'))    
        Anonymity = int(request.form.get('anonymity'))     
        Leave = int(request.form.get('leave') )
        Mental_health_consequence = int(request.form.get('mentalhealthconsequence'))
        Phys_health_consequence = int(request.form.get('physhealthconsequence'))
        Coworkers = int(request.form.get('coworkers'))
        Supervisor = int(request.form.get('supervisor'))
        Mental_health_interview = int(request.form.get('mentalhealthinterview'))
        Phys_health_interview =int( request.form.get('physhealthinterview'))
        
        MentalVSPhysical = int(request.form.get('mentalvsphysical'))

        Obs_consequence = int(request.form.get('obs_consequence'))
        
        new_input=np.array([[Age,Gender,Self_employed,Family_history,Work_interface,No_employees,Remote_work,Tech_company,Benefits,Care_options,Wellness_Program,Seek_help,Anonymity,Leave,Mental_health_consequence ,Phys_health_consequence,Coworkers,Supervisor,Mental_health_interview,Phys_health_interview,MentalVSPhysical,Obs_consequence]])
        result =lr.predict(new_input)
        if result==1:
           msg =' needs  '
        else:
           msg ='   not need   ' 
        return  render_template('result.html',prediction=msg,my_title='Result Page')


@app.route('/about')
def about():
    return render_template('about.html', my_title = 'About')

@app.route('/contact')
def contact():
    return render_template('contact2.html', my_title = 'Contact')

@app.route('/project')
def project():
    return render_template('project.html', my_title = 'resume page')
 
@app.route('/resume')
def resume():
    resume_url =request.args.get('name')
    return render_template('resume.html', my_title = 'Resume',resume_url=resume_url)


if __name__ == '__main__':
    app.run(debug = True)