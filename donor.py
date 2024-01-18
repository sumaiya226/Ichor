from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

donor = Flask(__name__)

# Updated database URI and some improvements
donor.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Sameena22@localhost/donordb'
donor.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False  # Disable modification tracking

db = SQLAlchemy(donor)

# Check database connection and create tables
try:
    with donor.app_context():
        db.engine.connect()
        print("Connected to the database.")
        db.create_all()  # Create tables before running the app
except Exception as e:
    print(f"Error connecting to the database or creating tables: {str(e)}")


class Donor(db.Model):
    __tablename__ = 'donor'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    contact = db.Column(db.String(15), nullable=False)
    bloodgroup = db.Column(db.String(4), nullable=False)
    location = db.Column(db.String(40), nullable=False)
    lastdonationdate = db.Column(db.Date, nullable=False)

    def __init__(self, name, dob, contact, bloodgroup, location, lastdonationdate):
        self.name = name
        self.dob = dob
        self.contact = contact
        self.bloodgroup = bloodgroup
        self.location = location
        self.lastdonationdate = lastdonationdate
        
@donor.route('/')
def donorpage():
    return render_template('donate.html')

@donor.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        dob = request.form['dob']
        contact = request.form['contact']
        bloodgroup = request.form['bloodgroup']
        location = request.form['location']
        lastdonationdate = request.form['lastdonationdate']

        # Validate data
        if not name or not dob or not contact or not bloodgroup or not location or not lastdonationdate:
            return "All fields are required", 400

        # Convert contact to a string
        contact = str(contact)

        # Create a new donor record
        new_donor = Donor(name, dob, contact, bloodgroup, location, lastdonationdate)

        # Add and commit to the database
        db.session.add(new_donor)
        db.session.commit()

        return "Registration successful"

    except Exception as e:
        return f"An error occurred: {str(e)}", 500

if __name__ == '__main__':
    with donor.app_context():
        db.create_all()
    donor.run(debug=True)



