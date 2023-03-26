from flask_sqlalchemy import SQLAlchemy

# Create db object
db = SQLAlchemy()

# Create Patient model
class PatientModel(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nhs_number = db.Column(db.Integer(), unique = True)
    name = db.Column(db.String())
    dob = db.Column(db.String())
    postcode = db.Column(db.String(10))

    def __init__(self, nhs_number,name,dob,postcode):
        self.nhs_number = nhs_number
        self.name = name
        self.dob = dob
        self.postcode = postcode

    def __repr__(self):
        return '<Patient %r>' % self.id

# Create Apppintment model
class AppointmentModel(db.Model):
    nhs_number = db.Column(db.Integer(), primary_key = True)
    status = db.Column(db.String())
    time = db.Column(db.String())
    dur = db.Column(db.String())
    clinician = db.Column(db.String(50))
    dept = db.Column(db.String(50))
    postcode = db.Column(db.String(10))

    def __init__(self, nhs_number,status,time, dur,cln,dept,postcode):
        self.nhs_number = nhs_number
        self.status = status
        self.time = time
        self.dur= dur
        self.cln = cln
        self.dept = dept
        self.postcode = postcode

    def __repr__(self):
        return '<Appointment %r>' % self.id