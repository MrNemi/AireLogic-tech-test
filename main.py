from flask import Flask, request, redirect, render_template
from models import db, PatientModel  # AppointmentModel

app = Flask(__name__)

# Setup configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db.init_app(app)

@app.before_first_request
def create_table():
    db.create_all()

app.run(host='localhost', port = 7000)

# Coding the Create view
@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        nhs_number = request.form['nhs_number']
        name = request.form['name']
        dob = request.form['dob']
        postcode = request.form['postcode']
        patient = PatientModel(nhs_number=nhs_number, name=name, dob=dob, postcode = postcode)
        db.session.add(patient)
        db.session.commit()
        return redirect('/data')