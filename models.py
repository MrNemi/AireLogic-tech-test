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