import mysql.connector
import json

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

def authenticate(mydb, uid, lastname):
     mycursor = mydb.cursor(dictionary=True)
     print(uid)
     mycursor.execute("select * from patients where Patient_ID = %s and Last_Name = %s", (uid, lastname))
     for row in mycursor.fetchall():
         print(row)
         if row['Last_Name'] == 'admin':
             print('admin ind')
             return 'Admin'
         else:
             print('pat')
             return 'Patient'
         
     return 'None'

# def createpatient(mydb, data):
#     data_string = data.decode('utf-8')
#     data_dict = json.loads(data_string)
#     print(data_dict)
#     mycursor = mydb.cursor()

#     # Need to add error check to see if it exists in table

#     if(data_dict['patientDoctorID'] == ''):
#         mycursor.execute("insert into `patients` values (%s, %s, %s, %s, NULL)", (data_dict['patientUID'],
#                                                                             data_dict['patientFirstname'],
#                                                                             data_dict['patientLastname'],
#                                                                             data_dict['patientAge']))
#         mycursor.execute("select * from `patients`")
#         for row in mycursor.fetchall():
#             print(row)
#     else:
#         mycursor.execute("insert into `patients` values (%s, %s, %s, %s, %s)", (data_dict['patientUID'],
#                                                                             data_dict['patientFirstname'],
#                                                                             data_dict['patientLastname'],
#                                                                             data_dict['patientAge'],
#                                                                             data_dict['patientDoctorID']))
#     mydb.commit()

#     return 'complete'

def createentity(mydb, data):
    data_string = data.decode('utf-8')
    data_dict = json.loads(data_string)
    print(data_dict)
    mycursor = mydb.cursor()

    if data_dict['type'] == 'patient':

        if(data_dict['patientDoctorID'] == ''):
            mycursor.execute("insert into `patients` values (%s, %s, %s, %s, NULL)", (data_dict['patientUID'],
                                                                                data_dict['patientFirstname'],
                                                                                data_dict['patientLastname'],
                                                                                data_dict['patientAge']))
            mycursor.execute("select * from `patients`")
            for row in mycursor.fetchall():
                print(row)
        else:
            mycursor.execute("insert into `patients` values (%s, %s, %s, %s, %s)", (data_dict['patientUID'],
                                                                                data_dict['patientFirstname'],
                                                                                data_dict['patientLastname'],
                                                                                data_dict['patientAge'],
                                                                                data_dict['patientDoctorID']))
    elif data_dict['type'] == 'doctor':

        if(data_dict['doctorHospitalID'] == ''):
            mycursor.execute("insert into `doctors` values (%s, %s, %s, NULL)", (data_dict['doctorId'],
                                                                                data_dict['doctorFirstname'],
                                                                                data_dict['doctorLastname']))
            mycursor.execute("select * from `doctors`")
            for row in mycursor.fetchall():
                print(row)
        else:
            mycursor.execute("insert into `doctors` values (%s, %s, %s, %s)", (data_dict['doctorId'],
                                                                                data_dict['doctorFirstname'],
                                                                                data_dict['doctorLastname'],
                                                                                data_dict['doctorHospitalID']))    
    elif data_dict['type'] == 'hospital':

        if(data_dict['hospitalCountryID'] == ''):

            mycursor.execute("insert into `hospitals` values (%s, NULL, %s, %s, %s)", (data_dict['hospitalID'],
                                                                                data_dict['hospitalName'],
                                                                                data_dict['hospitalGeolocation'],
                                                                                data_dict['hospitalCapacity']))  
        else:

            mycursor.execute("insert into `hospitals` values (%s, %s, %s, %s, %s)", (data_dict['hospitalID'],
                                                                                    data_dict['hospitalCountryID'],
                                                                                    data_dict['hospitalName'],
                                                                                    data_dict['hospitalGeolocation'],
                                                                                    data_dict['hospitalCapacity'])) 

    mydb.commit()
    return 'complete'

def deleteentity(mydb, data):
    data_string = data.decode('utf-8')
    data_dict = json.loads(data_string)
    print(data_dict)
    mycursor = mydb.cursor()

    if data_dict['type'] == 'patient':
        mycursor.execute('DELETE from `patients` where Patient_ID = (%s)', (data_dict['patientID'], ))

    elif data_dict['type'] == 'doctor':
        mycursor.execute('DELETE from `doctors` where Doctor_ID = (%s)', (data_dict['doctorID'], ))
    
    elif data_dict['type'] == 'hospital':
        mycursor.execute('DELETE from `hospitals` where Hospital_ID = (%s)', (data_dict['hospitalId'], ))

    mydb.commit()
    return 'complete'

