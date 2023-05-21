from hospital import app
from flask import render_template, request, url_for, redirect,session

# Define the User class
class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
class D_user:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Patient:
    def __init__(self, name, dob,gender,bg,phoneno, address,):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.bg = bg
        self.phoneno = phoneno
        self.address = address
        self.prescriptions = []
        self.appointments = []
        
    def add_prescription(self, medicine, dosage,advice):
        prescription = self.Prescription(medicine, dosage, advice)
        self.prescriptions.append(prescription)
        
    def add_appointment(self, date, time, doctor,department):
        appointment = self.Appointment(date, time, doctor,department)
        self.appointments.append(appointment)
        
    class Prescription:
        def __init__(self, medicine, dosage,advice):

            self.medicine = medicine
            self.dosage = dosage
            self.advice = advice
    class Appointment:
        def __init__(self, date, time, doctor,department,status='pending'):
            self.date = date
            self.time = time
            self.doctor = doctor
            self.department = department
            self.status = status

class Doctor:
    def __init__(self,id, name, dob,gender,specilazition,department,fee, avilability,phoneno, address,sallary):
        self.id = id
        self.name = name
        self.dob = dob
        self.gender = gender
        self.specilazition = specilazition
        self.department = department
        self.fee = fee
        self.avilability = avilability
        self.phoneno = phoneno
        self.address = address
        self.sallary = sallary
        self.appointments = []
        
    def add_appointment(self,patient, date, time, status,treated):
        appointment = self.Appointment(patient,date, time,status,treated)
        self.appointments.append(appointment)
    class Appointment:
        def __init__(self,patient, date, time, status,treated):
            self.patient=patient
            self.date = date
            self.time = time
            self.status = status
            self.treated = treated
            

users = []
doctors = []
registred_patient = {}
doctors_lst = {}
patient_lst = []
appointment_list = []

department = {'Cardiology':['Mr.Smith','Mr.Jhon','Mr.Tom'],'Neurology':['Mr.Singh','Mr Roy'],
        'Oncology':['Mr.Ayushman','Ms.Jiva'],'Pediatrics':['Ms.Choudhary', 'Ms Kiara'],
        'ENT':['Mr.Smith','Mr.Jhon','Mr.Tom']}

doctors.append(D_user('Smith123','12345'))
doctors.append(D_user('Jhon123','12345'))
doctors.append(D_user('Tom123','12345'))
doctors.append(D_user('Singh123','12345'))
doctors.append(D_user('Roy123','12345'))
doctors.append(D_user('Ayushman123','12345'))
doctors.append(D_user('Jiva123','12345'))
doctors.append(D_user('Choudhary123','12345'))
doctors.append(D_user('Kiara123','12345'))



doctors_lst['Smith123'] = Doctor('Smith123','Mr.Smith','11-11-11','Male','Heart','Cardiology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',0000)
doctors_lst['Jhon123'] = Doctor('Jhon123','Mr.Jhon','11-11-11','Male','Heart','Cardiology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',0000)
doctors_lst['Tom123'] = Doctor('Tom123','Mr.Tom','11-11-11','Male','Heart','Cardiology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)
doctors_lst['Singh123'] = Doctor('Singh123','Mr.Singh','11-11-11','Male','Heart','Neurology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)
doctors_lst['Roy123'] = Doctor('Roy123','Ms Roy','11-11-11','Male','Heart','Neurology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)
doctors_lst['Ayushman123'] = Doctor('Ayushman123','Mr.Ayushman','11-11-11','Male','Heart','Oncology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)
doctors_lst['Jiva123'] = Doctor('Jiva123','Ms.Jiva','11-11-11','Male','Heart','Oncology',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)
doctors_lst['Choudhary123'] = Doctor('Choudhary123','Ms.Choudhary','11-11-11','Male','Heart','Pediatrics',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)
doctors_lst['Kiara123'] = Doctor('Kiara123','Ms Kiara','11-11-11','Male','Heart','Pediatrics',1000,{'Monday':'9:30 to 2:00'},'0000000000','AA-BB-CC-DD',000)


#-----------------------------------------------------------Login Signup---------------------------------------------------------

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        c_password = request.form['password']

        for user in users:
            if user.username == username:
                error = 'Username already exists'
                print(error)
                return render_template('signup.html', error=error)
            elif user.email == email:
                error = 'Email already exists'
                return render_template('signup.html', error=error)
            elif password != c_password:
                error  = "Password doesn't match"
                return render_template('signup.html', error=error)
            else:
                new_user = User(username, email, password)
                users.append(new_user)
                return redirect('/p_login')
        if password != c_password:
            error  = "Password doesn't match"
            return render_template('signup.html', error=error)
        else:
            new_user = User(username, email, password)
            users.append(new_user)
            return redirect('/p_login')
        
    return render_template('signup.html')

# Define the login route and form
@app.route('/p_login', methods=['GET', 'POST'])
def p_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username and password are correct
        for user in users:
            if user.username == username and user.password == password:
                session['username'] = username
                return redirect(url_for('profile'))

        error = 'Incorrect username or password'
        return render_template('p_login.html', error=error)

    # Render the login page
    return render_template('p_login.html')

@app.route('/a_login', methods=['GET', 'POST'])
def a_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username,password)
        # Check if the username and password are correct
        if username == "admin@123" and password == 'admin':
            print('ankit')
            session['username'] = username
            return redirect('/aview_doctor')

        error = 'Incorrect username or password'
        return render_template('a_login.html', error=error)

    # Render the login page
    return render_template('a_login.html')

@app.route('/d_login', methods=['GET', 'POST'])
def d_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check if the username and password are correct
        for user in doctors:
            if user.username == username and user.password == password:
                session['username'] = username
                
                return redirect(url_for('home', username=username))

        error = 'Incorrect username or password'
        return render_template('d_login.html', error=error)

    # Render the login page
    return render_template('d_login.html')

# Define the sign-out route
@app.route('/logout') 
def logout():
    # Clear the session
    session.clear()




    # Redirect the user to the login page
    return redirect('/')

@app.route('/password', methods=['GET', 'POST'])
def password():
    
    if request.method=="POST":
        flag = False
        password = request.form.get('password')
        for doctor in doctors:
            if doctor.username == session.get('username'):
                doctor.password = password
                flag = True
        if flag == False:
            return render_template('derror.html',r = 'No account with username')
        else:
            return render_template('derror.html',r ='Password Changed')

    
    return render_template('pass.html')

@app.route('/forgetpass', methods=['GET', 'POST'])
def forgetpass():
    
    if request.method=="POST":
        flag = False
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        for user in users:
            if user.username == username and user.email == email:
                user.password = password
                flag = True
        if flag == False:
            return '<center><h2>Something Wrong</h2></center>'
        else:
            return redirect(url_for('p_login'))

    
    return render_template('pat_for_pass.html')

# Define the home page
@app.route('/home/<username>', methods=['GET', 'POST'])
def home(username):
    return render_template('d_home.html',doctor = doctors_lst[username])

    # Redirect the user to the login page

@app.route('/')
def w():
   return  render_template('login.html')

# ------------------------------------------- all the routes----------------------------------------------------------------------


@app.route('/patient', methods=['GET', 'POST'])
def patient_details():
    username = session.get('username')
    if request.method=="POST":
       
        name=request.form.get("name")
        dob = request.form.get('dob')
        gender = request.form.get('gender')
        bg = request.form.get('bg')
        phoneno = request.form.get('phone_no')
        address = request.form.get('address')
        
        registred_patient[username] = Patient(name,dob,gender,bg,phoneno,address)
        
        
        return redirect(url_for('profile'))
    else:
        
        return render_template('registration.html')
@app.route('/update_patient', methods=['GET', 'POST'])
def update_details():
    
    if request.method=="POST":
        username = session.get('username')
        name=request.form.get("name")
        value=request.form.get("value")
        if name=='name':
            registred_patient[username].name=value
        elif name=='gender':
            registred_patient[username].gender=value
        elif name=='bg':
            registred_patient[username].bg=value
        elif name=='phone':
            registred_patient[username].phoneno=value
        elif name=='address':
            registred_patient[username].address=value
        
        return redirect(url_for('profile'))
    else:
        
        return render_template('update.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    username = session.get('username')
    
    if username in registred_patient:
        return render_template('profile.html',personal_details = registred_patient[username])
    else:
        return render_template('error.html',r = 'CREATE YOUR PROFILE')




@app.route('/booking', methods=['GET', 'POST'])
def bookappointment():
    username = session.get('username')
    if request.method=="POST":
        appoint = request.form.to_dict()
        
        k = []
        v = []
        for key, item in appoint.items():
            k.append(key)
            v.append(item)

        doctors_lst[v[0]].add_appointment(username,appoint['date'],appoint['time'],'Not Confirmed','No')
        if username in registred_patient:
            registred_patient[username].add_appointment(appoint['date'],appoint['time'],doctors_lst[v[0]].name,k[0])
        else:
            return redirect(url_for('patient_details'))
        return render_template('appoint.html',personal_details = registred_patient[username])
    else:
        return render_template('book_appo.html',department=department,username=username,doctors = doctors_lst)

@app.route('/book', methods=['POST','GET'])
def book():
    username = session.get('username')
    if username in registred_patient:
        return render_template('appoint.html',personal_details = registred_patient[username])    
    else:
        return redirect(url_for('patient_details'))

@app.route('/view_doctor', methods=['POST','GET'])
def view_doctor():
    return render_template('v_doctor.html',doctors = doctors_lst)    

@app.route('/add_department', methods = ['GET','POST'])
def add_department():
    if request.method =='POST':
        department[request.form['name']] = []
        return redirect(url_for('add_department',department=department))
    else:
        
        return render_template('add_department.html',department=department)
    
@app.route('/add_doctor', methods = ['GET','POST'])
def add_doctor():
    if request.method =='POST':
        dict = request.form.to_dict()
        depart = dict['depart']
        id = dict['d']
        name = dict['name']
        dob = dict['dob']
        gender = dict['gender']
        special = dict['special']
        fee = dict['fee']
        avilability = dict['avilability']
        phn = dict['phn']
        address = dict['address']
        sallary = dict['sal']        
        doctors_lst[id] = Doctor(id,name,dob,gender,special,depart,fee,avilability ,phn,address,sallary)
        department[dict['depart']].append(name)
        return redirect(url_for('dregister',department=department))
    else:
        return render_template('add_doctor.html',department=department)
@app.route('/delete_department', methods = ['GET','POST'])
def delete_department():
    if request.method =='POST':
        depart = request.form['depart']
        del department[depart]
        return redirect(url_for('delete_department',department=department))
    else:
        return render_template('delete_depart.html',department=department)
    
@app.route('/remove_doctor', methods = ['GET','POST'])
def remove_doctor():
    if request.method =='POST':
        dict = request.form['depart']
        return redirect(url_for('delete_doctor',depart = dict))
    else:
        return render_template('remove_doc.html',department=department)
@app.route('/delete_doctor/<depart>/', methods = ['GET','POST'])
def delete_doctor(depart):
    if request.method =='POST':
        doctor= request.form['doctor']
        department[depart].remove(doctor)
        return redirect(url_for('remove_doctor',department=department))
    else:
        return render_template('delete_doctor.html',department=department,depart=depart)
@app.route('/aview_doctor', methods=['POST','GET'])
def aview_doctor():
    return render_template('av_doctor.html',doctors = doctors_lst)

@app.route('/aview_patient', methods=['POST','GET'])
def aview_patient():
    return render_template('av_patient.html',patients = registred_patient)
@app.route('/a_appoint',methods = ['GET','POST'])
def a_appoint():
    return render_template('a_appoint.html',doctors = doctors_lst)

@app.route('/dregister', methods=['GET', 'POST'])
def dregister():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        for user in doctors:
            if user.username == username:
                error = 'Username already exists'
                return render_template('dregister.html', error=error)
        
        new_user = D_user(username, password)
        doctors.append(new_user)
        return redirect('/add_doctor')
    return render_template('dregister.html')

@app.route('/d_profile',methods = ['GET','POST'])
def d_profile():
    username = session.get('username')

    return render_template('d_home.html',doctor = doctors_lst[username])
@app.route('/d_appoint',methods = ['GET','POST'])
def d_appoint():
    username = session.get('username')
    if request.method =='POST':

        status = request.form.to_dict()
        for key,value in status.items():
            pid = key
            st = value
        
        for appoint in registred_patient[pid].appointments:
            if appoint.doctor == doctors_lst[username].name:
                if st=='Confirm':
                    st='Confirmed'
                else:
                    st = 'Canceled'
                appoint.status = st
        
        # for appoint in doctors_lst[username].appointmnets:
        #     if appoint.patient == pid:
        #         appoint.status = st
        return redirect(url_for('d_appoint'))

    return render_template('d_appoint.html',doctor = doctors_lst[username])



@app.route('/prescription/<patient>', methods=['GET', 'POST'])
def prescription(patient):
    if request.method == 'POST':
        medicine = request.form['medicine']
        dosages = request.form['dosages']
        advice = request.form['advice']
        registred_patient[patient].add_prescription(medicine, dosages,advice)
        return redirect(url_for('prescription', patient=patient))
    return render_template('prescription.html')

