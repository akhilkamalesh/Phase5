from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import db as database_module

app = Flask(__name__, template_folder='pages')

mydb = database_module.connectdatabase()

session = {}

@app.route('/user_auth')
def user_auth():
    return render_template('user_auth.html')

@app.route('/doctor_auth')
def doctor_auth():
    return render_template('doctor_auth.html')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    uid = request.form['uid']
    password = request.form['password']
    if database_module.authenticate(mydb, uid, password):
        session['uid'] = uid
        return redirect(url_for('portal'))
    else:
        return "Incorrect Password or UID. Try again", 401

@app.route('/signup', methods=['POST'])
def signup():
    uid = request.form['uid']
    lastname = request.form['lastname']
    password = request.form['password']
    
    if database_module.user_exists(mydb, uid, lastname):
        return "This user already has an account", 409
    try:
        if database_module.signup_user(mydb, uid, lastname, password):
            session['uid'] = uid
            return redirect(url_for('portal'))
        else:
            return "Signup Failed", 400
    except mysql.connector.IntegrityError as e:
        return f"THIS USER ALREADY HAS AN ACCOUNT. PLEASE SIGN IN", 500

@app.route('/portal', methods=['GET'])
def portal():
    if 'uid' in session:
        uid = session['uid']
        user_info = database_module.get_user_info(mydb, uid)
        if not user_info:
            return "No user information available", 404
        return render_template('portal.html', user_info=user_info)
    return redirect(url_for('index'))

@app.route('/admin', methods=['GET'])
def admin():
    return render_template('admin.html')

@app.route('/admin', methods=['POST', 'DELETE', 'PUT'])
def handle_admin():
    if request.method == 'POST':
        # Access JSON data from a POST request
        data = request.data
        database_module.createentity(mydb, data)
        # Process the data and return a response
        return "Data is successfully imported"

    elif request.method == 'DELETE':
        # Access JSON data from a DELETE request
        data = request.data
        database_module.deleteentity(mydb, data)
        # Now you can work with the JSON data
        # Process the data and return a response
        return "Data is sucessfully deleted!"
    
    elif request.method == 'PUT':
        print('inside')
        data = request.data
        database_module.updateentity(mydb, data)
        return "Data is updated"

@app.route('/logout')
def logout():
    session.pop('uid', None)
    return redirect(url_for('index'))

@app.route('/doctor_login', methods=['POST'])
def doctor_login():
    lastname = request.form['lastname']
    password = request.form['password']
    if database_module.authenticate_doctor(mydb, lastname, password):
        session['lastname'] = lastname
        session['role'] = 'doctor'
        return redirect(url_for('doctor_portal', lastname=lastname))
    else:
        return "Incorrect Password or Doctor ID. Try again", 401

@app.route('/doctor_signup', methods=['POST'])
def doctor_signup():
    try:
        doctor_id = request.form['doctor_id']
        lastname = request.form['lastname']
        password = request.form['password']
    except KeyError as e:
        return f"Missing field: {str(e)}", 400

    if database_module.doctor_exists(mydb, lastname):
        return "This doctor already has an account", 409

    if database_module.signup_doctor(mydb, doctor_id, lastname, password):
        return redirect(url_for('doctor_login'))
    else:
        return "Signup Failed", 400

@app.route('/doctor_portal', methods=['GET'])
def doctor_portal():
    lastname = request.args['lastname']

    if session['lastname'] == lastname and session['role'] == 'doctor':
        data, user_data, country_data = database_module.getDocView(mydb, session['lastname'])
        return render_template('doctorportal.html', data=data, country_data = country_data, user_info = user_data)  

    return "LOGIN FAILD", 400

@app.route('/admin_login', methods=['POST'])
def admin_login():
    username = request.form['username']
    password = request.form['password']
    if database_module.authenticate_admin(mydb, username, password):
        session['admin_username'] = username
        return redirect(url_for('admin_portal'))
    else:
        return "Incorrect username or password. Try again", 401

@app.route('/admin_portal', methods=['GET'])
def admin_portal():
    if 'admin_username' in session:
        return render_template('admin.html')
    else:
        return redirect(url_for('admin_login_form'))

@app.route('/admin_login_form')
def admin_login_form():
    return render_template('admin_login_form.html')


@app.route('/create_admin', methods=['POST'])
def create_admin():
    if 'admin_username' not in session:
        return redirect(url_for('admin_login_form'))  

    username = request.form['username']
    password = request.form['password']

    if database_module.create_admin_user(username, password):
        return "Admin created successfully!"
    else:
        return "Failed to create admin."


from hashlib import sha256

@app.route('/change_password', methods=['POST'])
def change_password():
    if 'uid' not in session:
        return redirect(url_for('login'))  

    new_password = request.form['new_password']
    hashed_password = sha256(new_password.encode()).hexdigest()  

    if database_module.update_password(session['uid'], hashed_password):
        return "Password changed successfully!"
    else:
        return "Failed to change password.", 400

if __name__ == '__main__':
    app.run(debug=True)
