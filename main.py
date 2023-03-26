from flask import Flask, request, redirect, render_template, url_for
from models import db, PatientModel

app = Flask(__name__)

# Setup configs
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///task.db'

# Initialize database
db.init_app(app)

# Create db file before user accesses the server
@app.before_first_request
def create_table():
    db.create_all()

# Coding the Create view
@app.route('/', methods = ['POST','GET'])
def mainpage():
    if request.method == 'POST':
        nhs_number = request.form['nhs_number']
        name = request.form['name']
        dob = request.form['dob']
        postcode = request.form['postcode']
        new_patient = PatientModel(nhs_number=nhs_number,\
             name=name, dob=dob, postcode = postcode)
        
        try:
            db.session.add(new_patient)
            db.session.commit()
            return redirect('/')
        except:
             return 'There was an issue adding new patient details'
        
    else:
        patient = PatientModel.query.all()
        return render_template('mainpage.html', patient=patient)
    
# Coding the Read/Retrieve views




if __name__ == "__main__":
    app.run(host='localhost', port = 5000, debug =True)