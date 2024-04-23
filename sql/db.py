import mysql.connector
import json
from hashlib import sha256


# Connect to MySQL (change password)
def connectdatabase():
   mydb = mysql.connector.connect(
    host="localhost",  # or your server's IP address
    user="root",
    password="TEMPORARY",   #ENTER YOUR PASSWORD                                     
    database="phase4",    #ENTER YOUR DATABASE NAME
    autocommit=True
    )
   
   return mydb
 
def querydb(querystr, mydb):
    mycursor = mydb.cursor()
    mycursor.execute(querystr)
    return mycursor.fetchall()

def authenticate(mydb, uid, password):
    mycursor = mydb.cursor(dictionary=True)
    hashed_password = sha256(password.encode()).hexdigest()
    try:
        mycursor.execute("SELECT * FROM users WHERE uid = %s AND password = %s", (uid, hashed_password))
        user = mycursor.fetchone() 
        print(user)
        return bool(user)  
    finally:
        mycursor.close()

def get_user_info(mydb, uid):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT p.Patient_ID, p.First_Name AS Patient_Name, p.age, d.*, h.*, m.MedRecID, m.COVID_Positive, m.Vaccine "
                     "FROM patients p "
                     "JOIN medical_records m ON p.Patient_ID = m.patient_id "
                     "JOIN doctors d ON p.doctor_id = d.doctor_id "
                     "JOIN hospitals h ON d.hospital_id = h.hospital_id "
                     "WHERE p.patient_id = %s", (uid,))
    return mycursor.fetchone()

def signup_user(mydb, uid, last_name, password):
    mycursor = mydb.cursor()
    hashed_password = sha256(password.encode()).hexdigest()
    mycursor.execute("INSERT INTO users (uid, last_name, password) VALUES (%s, %s, %s)", (uid, last_name, hashed_password))
    mydb.commit()
    return get_user_info(mydb, uid)

def createentity(mydb, data):
    data_dict = json.loads(data)
    mycursor = mydb.cursor()

    if data_dict['type'] == 'patient':
        if not data_dict['patientDoctorID']:
            mycursor.execute("INSERT INTO `patients` VALUES (%s, %s, %s, %s, NULL)", (data_dict['patientUID'], data_dict['patientFirstname'], data_dict['patientLastname'], data_dict['patientAge']))
        else:
            mycursor.execute("INSERT INTO `patients` VALUES (%s, %s, %s, %s, %s)", (data_dict['patientUID'], data_dict['patientFirstname'], data_dict['patientLastname'], data_dict['patientAge'], data_dict['patientDoctorID']))
    elif data_dict['type'] == 'doctor':
        if not data_dict['doctorHospitalID']:
            mycursor.execute("INSERT INTO `doctors` VALUES (%s, %s, %s, NULL)", (data_dict['doctorId'], data_dict['doctorFirstname'], data_dict['doctorLastname']))
        else:
            mycursor.execute("INSERT INTO `doctors` VALUES (%s, %s, %s, %s)", (data_dict['doctorId'], data_dict['doctorFirstname'], data_dict['doctorLastname'], data_dict['doctorHospitalID']))
    elif data_dict['type'] == 'hospital':
        if not data_dict['hospitalCountryID']:
            mycursor.execute("INSERT INTO `hospitals` VALUES (%s, NULL, %s, %s, %s)", (data_dict['hospitalID'], data_dict['hospitalName'], data_dict['hospitalGeolocation'], data_dict['hospitalCapacity']))
        else:
            mycursor.execute("INSERT INTO `hospitals` VALUES (%s, %s, %s, %s, %s)", (data_dict['hospitalID'], data_dict['hospitalCountryID'], data_dict['hospitalName'], data_dict['hospitalGeolocation'], data_dict['hospitalCapacity']))
    mydb.commit()
    return 'complete'

def deleteentity(mydb, data):
    data_dict = json.loads(data)
    mycursor = mydb.cursor()
    if data_dict['type'] == 'patient':
        mycursor.execute('DELETE FROM `patients` WHERE Patient_ID = %s', (data_dict['patientID'],))
    elif data_dict['type'] == 'doctor':
        mycursor.execute('DELETE FROM `doctors` WHERE Doctor_ID = %s', (data_dict['doctorID'],))
    elif data_dict['type'] == 'hospital':
        mycursor.execute('DELETE FROM `hospitals` WHERE Hospital_ID = %s', (data_dict['hospitalId'],))
    mydb.commit()
    return 'complete'

def updateentity(mydb, data):
    print(data)
    data_dict = json.loads(data)
    mycursor = mydb.cursor()
    if data_dict['type'] == 'patient':
        print('inside')
        mycursor.execute('UPDATE patients SET First_Name = %s, Last_Name = %s, Age = %s, Doctor_ID = %s WHERE Patient_ID = %s', (data_dict['patientFirstname'], data_dict['patientLastname'], data_dict['patientAge'], data_dict['patientDoctorID'], data_dict['patientUID']))
    elif data_dict['type'] == 'doctor':
        mycursor.execute('UPDATE doctors SET First_Name = %s, Last_Name = %s WHERE Doctor_ID = %s', (data_dict['doctorFirstname'], data_dict['doctorLastname'], data_dict['doctorId']))
    elif data_dict['type'] == 'hospital':
        mycursor.execute('UPDATE hospitals SET Name = %s, Geolocation = %s, Capacity = %s WHERE Hospital_ID = %s', (data_dict['hospitalName'], data_dict['hospitalGeolocation'], data_dict['hospitalCapacity'], data_dict['hospitalID']))
    mydb.commit()
    return 'complete'

def user_exists(mydb, uid, lastname):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM users WHERE uid = %s AND last_name = %s", (uid, lastname))
    return bool(mycursor.fetchone())

def get_doctor_info(mydb, uid):
    mycursor = mydb.cursor(dictionary=True)
    print(uid)
    patients = []
    doctor = []
    mycursor.execute("select p.First_Name, p.Last_Name, p.age from patients p where Doctor_ID = %s", (uid, ))
    for row in mycursor.fetchall():
        patients.append(row)
    
    mycursor.execute("select * from doctors d join hospitals h on d.Hospital_ID = h.Hospital_ID")
    for row in mycursor.fetchall():
        doctor.append(row)

    return {'patients': patients, 'doctors': doctor}


def authenticate_doctor(mydb, lastname, password):
    mycursor = mydb.cursor(dictionary=True)
    hashed_password = sha256(password.encode()).hexdigest()
    mycursor.execute("SELECT * FROM doctor_auth WHERE lastname = %s AND password_hash = %s", (lastname, hashed_password))
    result = mycursor.fetchone()
    mycursor.close()
    return bool(result)



def signup_doctor(mydb, doctor_id, lastname, password):
    hashed_password = sha256(password.encode()).hexdigest()
    mycursor = mydb.cursor()
    mycursor.execute("INSERT INTO doctor_auth (doctor_id, lastname, password_hash) VALUES (%s, %s, %s)", (doctor_id, lastname, hashed_password))
    mydb.commit()
    mycursor.close()

def doctor_exists(mydb, lastname):
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM doctor_auth WHERE lastname = %s", (lastname,))
    result = mycursor.fetchone()
    mycursor.close()
    return bool(result)

def getDocView(mydb, last_name):
    cursor = mydb.cursor()
    cursor.execute("SELECT Doctor_ID FROM doctors WHERE Last_Name = '%s'"%last_name)
    id = cursor.fetchall()
    cursor.execute("SELECT * FROM patients WHERE Doctor_ID = %s"%id[0])
    data = cursor.fetchall()
    cursor.execute("Select * FROM doctors WHERE Last_Name = '%s'"%last_name)
    user_data = cursor.fetchall()
    cursor.execute("Select * FROM country")
    country_data = cursor.fetchall()
    mydb.close()
    
    return data, user_data, country_data

def getPatientView(mydb, uid):
    cursor = mydb.cursor()
    cursor.execute("Select * FROM patients WHERE Patient_ID = %s"%uid)
    user_data = cursor.fetchall()
    cursor.execute("Select * FROM country")
    country_data = cursor.fetchall()
    mydb.close()

    return country_data, user_data

def getAdminView(mydb, uid):
    cursor = mydb.cursor()
    cursor.execute("SELECT * FROM country")
    data = cursor.fetchall()
    
    cursor.execute("Select * FROM patients WHERE Patient_ID = %s"%uid)
    user_data = cursor.fetchall()
    mydb.close()


def authenticate_admin(mydb, username, password):
    mycursor = mydb.cursor(dictionary=True)
    mycursor.execute("SELECT * FROM admin_auth WHERE username = %s AND password_hash = %s", (username, password))
    result = mycursor.fetchone()
    mycursor.close()
    return bool(result)


def create_admin_user(username, password):
    mydb = connectdatabase()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("INSERT INTO admin_auth (username, password_hash) VALUES (%s, %s)", (username, password))
        mydb.commit()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    finally:
        mycursor.close()


def update_password(uid, hashed_password):
    mydb = connectdatabase()
    mycursor = mydb.cursor()
    try:
        mycursor.execute("UPDATE users SET password = %s WHERE uid = %s", (hashed_password, uid))
        mydb.commit()
        return True
    except mysql.connector.Error as err:
        print("Error:", err)
        return False
    finally:
        mycursor.close()


