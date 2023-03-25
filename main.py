from flask import Flask
from models import db, PatientModel, AppointmentModel


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