from flask import Flask, render_template, request, redirect, url_for, session
import mysql.connector
import db as database_module

app = Flask(__name__, template_folder='pages')

mydb = database_module.connectdatabase()

session = {}

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
        return "Login Failed", 401

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

if __name__ == '__main__':
    app.run(debug=True)




























# from flask import Flask, render_template, request
# import db as db
# app = Flask(__name__)

# app = Flask(__name__, template_folder='pages')

# mydb = db.connectdatabase()

# session = {}

# @app.route('/')
# def usertype():
#    return render_template('index.html')

# @app.route('/patientlogin')
# def patientlogin():
#   return render_template('patientlogin.html')

# @app.route('/patientlogin', methods=['POST'])
# def submit():
#   if request.method == 'POST':
#         uid = request.form['uid']
#         lastname = request.form['lastname']
#         if db.authenticate(mydb, uid, lastname) == 'None':
#            print('invalid')
#            return patientlogin()
#         elif db.authenticate(mydb, uid, lastname) == 'Patient':
#            session['uid'] = uid
#            session['lastname'] = lastname
#            print('works')
#            return portal()
#         elif db.authenticate(mydb, uid, lastname) == 'Admin':
#            print('works')
#            return admin()
        
# @app.route('/doctorlogin')
# def doctorlogin():
#    return render_template('doctorlogin.html')


# @app.route('/doctorlogin', methods=['POST'])
# def dsubmit():
#    if request.method == 'POST':
#         uid = request.form['uid']
#         lastname = request.form['lastname']
#         if db.dauthenticate(mydb, uid, lastname) == 'None':
#             print('invalid')
#             return doctorlogin()
#         elif db.dauthenticate(mydb, uid, lastname) == 'True':
#             session['uid'] = uid
#             session['lastname'] = lastname
#             print('works')
#             return doctorportal()
        

# @app.route('/portal', methods=['GET'])
# def portal():
#    if 'uid' in session:
#       uid = session['uid']
#       user_info = db.get_user_info(mydb, uid)
#       print(user_info)
#       if user_info['Vaccine'] == 1:
#          user_info['Vaccine'] = 'True'
#       else:
#          user_info['Vaccine'] = 'False'

#       if user_info['COVID_Positive'] == 1:
#          user_info['COVID_Positive'] = 'True'
#       else:
#          user_info['COVID_Positive'] = 'False'

#       return render_template('portal.html', user_info = user_info)
   

# @app.route('/doctorportal', methods=['GET'])
# def doctorportal():
#    if 'uid' in session:
#       uid = session['uid']
#       doctor_info = db.get_doctor_info(mydb, uid)
#       return render_template('doctorportal.html', doctor_info=doctor_info)


# @app.route('/admin', methods=['GET'])
# def admin():
#    return render_template('admin.html')

# @app.route('/admin', methods=['POST'])
# def createentity():
#    print(request.data)
#    db.createentity(mydb, request.data)
#    return render_template('admin.html')

# @app.route('/admin', methods=['DELETE'])
# def deleteentity():
#    print(request.data)
#    db.deleteentity(mydb, request.data)
#    return render_template('admin.html')

# if __name__ == '__main__':
#   app.run(debug=True)