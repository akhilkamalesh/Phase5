import mysql.connector
import json
from hashlib import sha256

# Connect to MySQL (change password)
def connectdatabase():
   mydb = mysql.connector.connect(
    host="localhost",  # or your server's IP address
    user="root",
    password="Protocol10",
    database="CS4604"   
    )
   
   return mydb
 
def querydb(querystr, mydb):
    mycursor = mydb.cursor()
    mycursor.execute(querystr)
    # for row in mycursor.fetchall():
    #     print(row)
    return mycursor.fetchall()

def authenticate(mydb, uid, password):
    mycursor = mydb.cursor(dictionary=True)
    hashed_password = sha256(password.encode()).hexdigest()
    print(hashed_password)
    mycursor.execute("SELECT * FROM users WHERE uid = %s AND password = %s", (uid, hashed_password))
    print(mycursor.fetchone())
    return bool(mycursor.fetchone()) 

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
    data_dict = json.loads(data)
    mycursor = mydb.cursor()
    if data_dict['type'] == 'patient':
        mycursor.execute('UPDATE patients SET First_Name = %s, Last_Name = %s, Age = %s, Doctor_ID = %s WHERE Patient_ID = %s', (data_dict['patientFirstname'], data_dict['patientLastname'], data_dict['patientAge'], data_dict['patientDoctorID'], data_dict['patientUID']))
    elif data_dict['type'] == 'doctor':
        mycursor.execute('UPDATE doctors SET First_Name = %s, Last_Name = %s WHERE Doctor_ID = %s', (data_dict['doctorFirstname'], data_dict['doctorLastname'], data_dict['doctorId']))
    elif data_dict['type'] == 'hospital':
        mycursor.execute('UPDATE hospitals SET Name = %s, Geolocation = %s, Capacity = %s WHERE Hospital_ID = %s', (data_dict['hospitalName'], data_dict['hospitalGeolocation'], data_dict['hospitalCapacity'], data_dict['hospitalId']))
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
