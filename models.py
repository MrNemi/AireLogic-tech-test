from flask_sqlalchemy import SQLAlchemy

# Create db object
db = SQLAlchemy()

# Create Patient model
class PatientModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    nhs_number = db.Column(db.Integer(), unique = True)
    name = db.Column(db.String())
    DOB = db.Column(db.String(12))
    postcode = db.Column(db.String(10))

    def __init__(self, nhs_number,name,DOB,postcode):
        self.nhs_number = nhs_number
        self.name = name
        self.DOB = DOB
        self.postcode = postcode

    def __repr__(self):
        return f"{self.name}:{self.nhs_number}"


# Create Appointment Model
class AppointmentModel(db.Model):
    __tablename__ = "table"

    id = db.Column(db.Integer, primary_key=True)
    patient = db.Column()
    status = db.Column(db.String())
    time = db.Column(db.String(12))
    duration = db.Column(db.String(10))
    clinician = db.Column(db.String(50))
    department = db.Column(db.String(50))
    postcode = db.Column(db.String(10))
    app_id = db.Column(db.UUID(), unique = True)

    def __init__(self, nhs_number,name,DOB,postcode):
        self.nhs_number = nhs_number
        self.name = name
        self.DOB = DOB
        self.postcode = postcode

    def __repr__(self):
        return f"{self.patient}:{self.status}"