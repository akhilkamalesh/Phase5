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

def createpatient(mydb, data):
    data_string = data.decode('utf-8')
    data_dict = json.loads(data_string)
    print(data_dict)
    mycursor = mydb.cursor()

    # Need to add error check to see if it exists in table

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
    mydb.commit()

    return 'complete'