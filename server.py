from flask import Flask, render_template, request
import db as db
app = Flask(__name__)

app = Flask(__name__, template_folder='pages')

mydb = db.connectdatabase()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/', methods=['POST'])
def submit():
  if request.method == 'POST':
        uid = request.form['uid']
        lastname = request.form['lastname']
        if db.authenticate(mydb, uid, lastname) == 'None':
           print('inside')
           return index()
        elif db.authenticate(mydb, uid, lastname) == 'Patient':
           print('works')
           return portal()
        elif db.authenticate(mydb, uid, lastname) == 'Admin':
           print('works')
           return admin()
        
@app.route('/portal', methods=['GET'])
def portal():
   return render_template('portal.html')

@app.route('/admin', methods=['GET'])
def admin():
   return render_template('admin.html')

@app.route('/admin', methods=['POST'])
def createentity():
   print(request.data)
   db.createentity(mydb, request.data)
   return render_template('admin.html')

# @app.route('/admin/createdoctor', methods=['POST'])
# def createdoctor():
#    db.createdoctor(mydb, request.data)
#    return render_template('admin.html')


if __name__ == '__main__':
  app.run(debug=True)