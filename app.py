from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthcare.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(app)

# DATABASE MODEL

class Patient(DB.Model):
    id = DB.Column(DB.Integer, primary_key=True)
    name = DB.Column(DB.String(100))
    email = DB.Column(DB.String(100))
    password = DB.Column(DB.String(100))

# HOME

@app.route('/')
def home():
    return render_template('login.html')

# LOGIN

@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']

    user = Patient.query.filter_by(email=email, password=password).first()

    if user:
        return redirect('/dashboard')

    return 'Invalid Login'

# REGISTER

@app.route('/register', methods=['POST'])
def register():

    name = request.form['name']
    email = request.form['email']
    password = request.form['password']

    new_user = Patient(
        name=name,
        email=email,
        password=password
    )

    DB.session.add(new_user)
    DB.session.commit()

    return redirect('/')

# DASHBOARD

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

# DOCTORS

@app.route('/doctors')
def doctors():
    return render_template('doctors.html')

# APPOINTMENT

@app.route('/appointment')
def appointment():
    return render_template('appointment.html')

# RECORDS

@app.route('/records')
def records():
    return render_template('records.html')

# EMERGENCY

@app.route('/emergency')
def emergency():
    return render_template('emergency.html')

# PRESCRIPTION

@app.route('/prescription')
def prescription():
    return render_template('prescription.html')

if __name__ == '__main__':

    with app.app_context():
        DB.create_all()

    app.run(debug=True)