from fastapi import FastAPI, Depends, HTTPException
import random
from fastapi import Request
import ZODB, ZODB.FileStorage
import transaction
import BTrees._OOBTree
import datetime
from datetime import timedelta
from fastapi import Request, FastAPI, Depends, HTTPException, Header
import random
from user import *
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from email.mime.text import MIMEText
import threading
import time

storage = ZODB.FileStorage.FileStorage('data/userData.fs')
db = ZODB.DB(storage)
connection = db.open()
root = connection.root

if not hasattr(root, "doctors"):
    root.doctors = BTrees.OOBTree.BTree()
if not hasattr(root, "patients"):
    root.patients = BTrees.OOBTree.BTree()
if not hasattr(root, "appointments"):
    root.appointments = BTrees.OOBTree.BTree()
if not hasattr(root, "medications"):
    root.medications = BTrees.OOBTree.BTree()
if not hasattr(root, "vaccines"):
    root.vaccines = BTrees.OOBTree.BTree()
if not hasattr(root, "allergies"):
    root.allergies = BTrees.OOBTree.BTree()
if not hasattr(root, "medicalRecords"):
    root.medicalRecords = BTrees.OOBTree.BTree()
if not hasattr(root, "sessions"):
    root.sessions = BTrees.OOBTree.BTree()
if not hasattr(root, "others"):
    root.others = BTrees.OOBTree.BTree()
if not hasattr(root, "lab_requests"):
    root.lab_requests = BTrees.OOBTree.BTree()
if not hasattr(root, "Lab_replies"):
    root.lab_replies = BTrees.OOBTree.BTree()
if not hasattr(root, "reports"):
    root.reports = BTrees.OOBTree.BTree()
if not hasattr(root, "pastday"):
    root.pastday = BTrees.OOBTree.BTree()
if not hasattr(root, "bills"):
    root.bills = BTrees.OOBTree.BTree()

app = FastAPI()

TEMP_MEDICATIONS = []
TEMP_VACCINES = []
TEMP_ALLERGIES = []
TEMP_OTHERS = []

configuration = sib_api_v3_sdk.Configuration()

configuration.api_key['api-key'] = "xxx"

api_instance = sib_api_v3_sdk.TransactionalEmailsApi(sib_api_v3_sdk.ApiClient(configuration))

#appointment reminder
class remider_email(threading.Thread):
    def run(self,*args,**kwargs):
        while True:
            date = datetime.datetime.now().date()
        
            year = date.year
            month = date.month
            day = date.day
            
            for appointment in root.appointments:
                appointment_datetime = datetime.datetime.strptime(root.appointments[appointment].getDate(), "%d/%m/%Y")
                appointment_year = appointment_datetime.year
                appointment_month = appointment_datetime.month
                appointment_day = appointment_datetime.day
                if year == appointment_year and month == appointment_month and int(day) + 1 == int(appointment_day):
                    for patient in root.patients:
                        if root.appointments[appointment].getPatientHNNumber() == root.patients[patient].getHNNumber():
                            patient_email = root.patients[patient].getEmail()
                            topic = "Appointment Reminder"
                            body = "You have an appointment with " + root.appointments[appointment].getDoctor() + " on " + root.appointments[appointment].getDate() + " at " + root.appointments[appointment].getTime()
                            send_email(patient_email, topic, body)
            time.sleep(82800)

@app.on_event("startup")
async def startup_event():
    t = remider_email()
    t.start()

#send email
def send_email(receiver_email, subject, body):
    from_email = "patientsphere@gmail.com"
    password = "patientsphere122"
    message = MIMEText(body)
    message["Subject"] = subject
    message["From"] = from_email
    message["To"] = receiver_email
    
    send_smtp_email = sib_api_v3_sdk.SendSmtpEmail(
        to=[{"email": receiver_email}],
        sender={"email": from_email},
        subject=subject,
        html_content=body
    )
    try:
        api_response = api_instance.send_transac_email(send_smtp_email)
        print(api_response)
    except ApiException as e:
        print("Exception when calling TransactionalEmailsApi->send_transac_email: %s\n" % e)
            
# create session
def create_session(username: str):
    session_id = random.randint(0, 1000000)
    
    date = datetime.datetime.now().date()
    
    expiry = date + datetime.timedelta(days=7)

    root.sessions[session_id] = {
        "username": username,
        "expiry": expiry
    }
    transaction.commit()
    return session_id

# check user authentication
async def authenticate_user(request: Request):
    data = await request.json()
    
    username = data["username"]
    password = data["password"]
    
    user = None
    user_type = None
    if username.isnumeric():
        for patient in root.patients:
            if username == root.patients[patient].getHNNumber():
                if password == root.patients[patient].getPassword():
                    user = root.patients[patient]
                    user_type = "patient"   
                else:
                    user = "password incorrect"
                    user_type = "password incorrect"      
    elif username == "admin":
        if password == "Admin_123":
            user = "admin"
            user_type = "admin"
        else:
            user = "password incorrect"
            user_type = "password incorrect"
    else:
        for doctor in root.doctors:
            if username == root.doctors[doctor].getUserName():
                if password == root.doctors[doctor].getPassword():
                    user = root.doctors[doctor]
                    user_type = "doctor"
                else:
                    user = "password incorrect"
                    user_type = "password incorrect"
    if user is None:
        user = "None"
        user_type = "None"
    return user, user_type

# Session check
@app.post("/")
def home():
    if len(root.sessions) == 0:
        return {"message": "No session found"}
    for session in root.sessions:
        current_session = root.sessions[session]
        if current_session["expiry"] < datetime.datetime.now().date():
            del root.sessions[session]
            transaction.commit()
            return {"message": "Session expired"}
        else:
            if current_session["username"] == "admin":
                return {"message": "admin"}
            elif current_session["username"].isnumeric():
                for patient in root.patients:
                    if current_session["username"] == root.patients[patient].getHNNumber():
                        user = root.patients[patient]
                        return {"message": "patient", "user_data": user}
            else:
                for doctor in root.doctors:
                    if current_session["username"] == root.doctors[doctor].getUserName():
                        user = root.doctors[doctor]
                        return {"message": "doctor", "user_data": user}

# 
@app.post("/admin")
async def register(request: Request):
    data = await request.json()
    
    firstName = data["firstName"]
    middleName = data["middleName"]
    lastName = data["lastName"]
    speciality = data["speciality"]
    username = data["username"]
    password = data["password"]
    profile = data["profile"]
    email = data["email"]
    
    for doctor in root.doctors:
        if username == root.doctors[doctor].getUserName():
            return {"message": "Username already exists"}
    
    doctor = Doctor(firstName, middleName, lastName, password, username, speciality, profile, email)
    root.doctors[username] = doctor
    transaction.commit()
    return {"message": "Doctor added successfully"}

# login
@app.post("/login")
def login(user_info: dict = Depends(authenticate_user)):
    user, user_type = user_info
    
    if user == "None":
        return {"message": "User not found"}
    elif user == "password incorrect":
        return {"message": "Incorrect password"}
    elif user == "admin":
        session_id = create_session("admin")
        return {"message": "admin user", "session_id": session_id ,"user_data": user, "type": user_type}
    session_id = create_session(user.getUserName() if user_type == "doctor" else user.getHNNumber())
    return {"message": "Logged in successfully", "session_id": session_id, "user_data": user, "type": user_type}

# log out
@app.post("/logout")
async def logout():
    session_ids = list(root.sessions.keys()) 
    for session_id in session_ids:
        del root.sessions[session_id] 
    transaction.commit()
    return {"message": "Logged out successfully"}


# Add medication
@app.post("/medication")  
async def add_medication(request: Request):
    data = await request.json()
    name = data["name"]
    amount = data["amount"]
    dosage = data["dosage"]
    duration = data["duration"]
    doctor_administered = data["doctorAdministered"]
    date_administered = data["dateAdministered"]
    time_administered = data["timeAdministered"]
    sidenote = data["sideNote"]
    
    for medication in TEMP_MEDICATIONS:
        if medication.getName() == name and medication.getDateAdministered() == date_administered:
            return {"message": "Medication already added", "medication": TEMP_MEDICATIONS}
    id = random.randint(0, 1000000)
    while id in root.medications.keys():
        id = random.randint(0, 1000000)
    medication = Medication(id, name, amount, dosage, duration, doctor_administered, date_administered, time_administered, sidenote)
    TEMP_MEDICATIONS.append(medication)
    return {"message": "Medication added successfully", "medication": TEMP_MEDICATIONS}

# Delete Medication
@app.delete("/medication/{id}")
async def delete_medication(id: int):
    for medication in TEMP_MEDICATIONS:
        if medication.getID() == id:
            TEMP_MEDICATIONS.remove(medication)
            return {"message": "Medication deleted successfully", "medication": TEMP_MEDICATIONS}
    raise HTTPException(status_code=404, detail="Medication not found")

# Add vaccine
@app.post("/vaccine")  
async def add_vaccine(request: Request):
    data = await request.json()
    name = data["name"]
    dateAdministered = data["dateAdministered"]
    
    for vaccine in TEMP_VACCINES:
        if vaccine.getName() == name and vaccine.getDateAdministered() == dateAdministered:
            return {"message": "Vaccine already added", "vaccine": TEMP_VACCINES}
    id = random.randint(0, 1000000)
    while id in root.vaccines.keys():
        id = random.randint(0, 1000000)
    vaccine = Vaccine(id, name, dateAdministered)
    TEMP_VACCINES.append(vaccine)
    return {"message": "Vaccine added successfully", "vaccine": TEMP_VACCINES}


# Delete Vaccine
@app.delete("/vaccine/{id}")
async def delete_vaccine(id: int):
    for vaccine in TEMP_VACCINES:
        if vaccine.getID() == id:
            TEMP_VACCINES.remove(vaccine)
            return {"message": "Vaccine deleted successfully", "vaccine": TEMP_VACCINES}
    raise HTTPException(status_code=404, detail="Vaccine not found")

# Add Allergy
@app.post("/allergy") 
async def add_allergy(request: Request):
    data = await request.json()
    name = data["name"]
    
    for allergy in TEMP_ALLERGIES:
        if allergy.getName() == name:
            return {"message": "Allergy already added", "allergy": TEMP_ALLERGIES}
    id = random.randint(0, 1000000)
    while id in root.vaccines.keys():
        id = random.randint(0, 1000000)
    allergy = Allergy(id, name)
    TEMP_ALLERGIES.append(allergy)
    return {"message": "Allergy added successfully", "allergy": TEMP_ALLERGIES}

# Delete Allergy
@app.delete("/allergy/{id}")
async def delete_allergy(id: int):
    for allergy in TEMP_ALLERGIES:
        if allergy.getID() == id:
            TEMP_ALLERGIES.remove(allergy)
            return {"message": "Allergy deleted successfully", "allergy": TEMP_ALLERGIES}
    raise HTTPException(status_code=404, detail="Allergy not found")


# Create Patient
@app.post("/create_patient")
async def create_patient(request: Request):
    data = await request.json()
    
    profile = data["profile"]
    firstName = data["firstName"]
    middleName = data["middleName"]
    lastName = data["lastName"]
    hnNumber = data["hnNumber"]
    dob = data["birthDate"]
    sex = data["sex"]
    bloodType = data["bloodType"]
    weight = data["weight"]
    height = data["height"]
    vaccines = data["medicalInfo"]["vaccines"]
    medications = data["medicalInfo"]["medications"]
    allergies = data["medicalInfo"]["allergies"]    
    password = data["passwordID"]
    address = data["address"]
    tel = data["tel"]
    blood_pressure = data["blood_pressure"]
    email = data["email"]
    
    vaccine_list = []
    allergies_list = []
    medication_list = []
    
    for vaccine in vaccines:
        the_vaccine = Vaccine(vaccine["id"], vaccine["name"], vaccine["dateAdministered"])
        root.vaccines[vaccine["id"]] = the_vaccine
        vaccine_list.append(the_vaccine)
    for medication in medications:
        the_medication = Medication(medication["id"], medication["name"], medication["amount"], medication["dosage"], medication["duration"], medication["doctorAdministered"], medication["dateAdministered"], medication["timeAdministered"], medication["sidenote"])
        root.medications[medication["id"]] = the_medication 
        medication_list.append(the_medication)
    for allergy in allergies:
        the_allergy = Allergy(allergy["id"], allergy["allergy"])
        root.allergies[allergy["id"]] = the_allergy
        allergies_list.append(the_allergy)
    for patient in root.patients:
        if hnNumber == root.patients[patient].getHNNumber():
            medicalRecord = root.patients[patient].getMedicalRecord()
            medicalRecord.setFirstName(firstName)
            medicalRecord.setMiddleName(middleName)
            medicalRecord.setLastName(lastName)
            medicalRecord.setBirthDate(dob)
            medicalRecord.setSex(sex)
            medicalRecord.setBloodType(bloodType)
            medicalRecord.setWeight(weight)
            medicalRecord.setHeight(height)
            medicalRecord.setVaccineHistory(vaccine_list)
            medicalRecord.setMedicationHistory(medication_list)
            medicalRecord.setAllergy(allergies_list)
            medicalRecord.setAddress(address)
            medicalRecord.setTel(tel)
            medicalRecord.setBloodPressure(blood_pressure)
            root.patients[hnNumber].setPassword(password)
            transaction.commit()
            return {"message": "Patient added successfully"}
    medicalRecord = MedicalRecord(firstName, middleName, lastName, hnNumber, dob, sex, bloodType, weight, height, medication_list, allergies_list, vaccine_list, address, tel, blood_pressure)
    root.medicalRecords[hnNumber] = medicalRecord
    patient = Patient(firstName, middleName, lastName, password, hnNumber, medicalRecord, profile, email)
    root.patients[hnNumber] = patient
    transaction.commit()
    close()
    return {"message": "Patient added successfully"}

# Get List of Patients for Doctor Side
@app.get("/patient_list")
def get_patients():
    patients = []
    for patient in root.patients:
        patient_list = {}
        patient_list["name"] = root.patients[patient].getFullName()
        patient_list["hnNumber"] = root.patients[patient].getHNNumber()
        patients.append(patient_list)
        
    return {"patients": patients}

# Get Individual Patient
@app.post("/patient_list/{hnNumber}")
async def get_patient(hnNumber: str):
    global TEMP_MEDICATIONS
    global TEMP_VACCINES
    global TEMP_ALLERGIES
    for patient in root.patients:
        if hnNumber in root.patients:
            patient = root.patients[hnNumber]
            medicalRecord = patient.getMedicalRecord()
            lab_requests = []
            for lab_request in root.lab_requests:
                if hnNumber == root.lab_requests[lab_request].getPatientHNNumber():
                    lab_requests.append(root.lab_requests[lab_request])
            TEMP_VACCINES = medicalRecord.getVaccineHistory().copy()
            TEMP_MEDICATIONS = medicalRecord.getMedicationHistory().copy()
            TEMP_ALLERGIES = medicalRecord.getAllergy().copy()
            return {
                "profile": patient.getProfile(),
                "firstName": medicalRecord.getFirstName(),
                "middleName": medicalRecord.getMiddleName(),
                "lastName": medicalRecord.getLastName(),
                "passwordID": patient.getPassword(),
                "hnNumber": medicalRecord.getHNNumber(),
                "dob": medicalRecord.getBirthDate(),
                "sex": medicalRecord.getSex(),
                "bloodType": medicalRecord.getBloodType(),
                "weight": medicalRecord.getWeight(),
                "height": medicalRecord.getHeight(),
                "vaccines": medicalRecord.getVaccineHistory().copy(),
                "medications": medicalRecord.getMedicationHistory().copy(),
                "allergies": medicalRecord.getAllergy().copy(),
                "address": medicalRecord.getAddress(),
                "tel": medicalRecord.getTel(),
                "blood_pressure": medicalRecord.getBloodPressure(),
                "lab_tests": lab_requests,
                "email": patient.getEmail()
            }

# Get List of Doctors for Admin Side         
@app.get("/doctor_list")
def get_doctors():
    doctors = []
    for doctor in root.doctors:
        doctor_list = {}
        doctor_list["name"] = root.doctors[doctor].getFullName()
        doctor_list["username"] = root.doctors[doctor].getUserName()
        doctor_list["passwordID"] = root.doctors[doctor].getPassword()
        doctor_list["speciality"] = root.doctors[doctor].getSpeciality()
        doctors.append(doctor_list)
    return {"doctors": doctors}

# Get Medical Record
@app.post("/medical_record")
async def get_medical_record(session_id: int = Header(None)):
    
    global TEMP_MEDICATIONS
    global TEMP_VACCINES
    global TEMP_ALLERGIES

    if session_id in root.sessions:
        current_session = root.sessions[session_id]
        if current_session["expiry"] < datetime.datetime.now().date():
            del root.sessions[session_id]
            transaction.commit()
            raise HTTPException(status_code=401, detail="Session expired")
        elif current_session["user_type"] == "patient":
            hnNumber = current_session["username"] 
            for patient in root.patients:
                if hnNumber == root.patients[patient].getHNNumber():
                    TEMP_VACCINES = medicalRecord.getVaccineHistory().copy()
                    TEMP_MEDICATIONS = medicalRecord.getMedicationHistory().copy()
                    TEMP_ALLERGIES = medicalRecord.getAllergy().copy()
                    medicalRecord = root.patients[patient].getMedicalRecord()
                    return {
                        "profile": root.patients[patient].getProfile(),
                        "firstName": medicalRecord.getFirstName(),
                        "middleName": medicalRecord.getMiddleName(),
                        "lastName": medicalRecord.getLastName(),
                        "hnNumber": medicalRecord.getHNNumber(),
                        "dob": medicalRecord.getBirthDate(),
                        "hnNumber": medicalRecord.getHNNumber(),
                        "dob": medicalRecord.getBirthDate(),
                        "sex": medicalRecord.getSex(),
                        "bloodType": medicalRecord.getBloodType(),
                        "weight": medicalRecord.getWeight(),
                        "height": medicalRecord.getHeight(),
                        "vaccines": medicalRecord.getVaccineHistory().copy(),
                        "medications": medicalRecord.getMedicationHistory().copy(),
                        "allergies": medicalRecord.getAllergy().copy(),
                        "address": medicalRecord.getAddress(),
                        "tel": medicalRecord.getTel(),
                        "blood_pressure": medicalRecord.getBloodPressure()
                    }
            raise HTTPException(status_code=404, detail="Patient not found")
        else:
            raise HTTPException(status_code=403, detail="Access denied, user is not a patient")
    raise HTTPException(status_code=404, detail="Session not found")


# Create Appointment
@app.post("/appointment")
async def create_appointment(request: Request):
    appointment_duration = timedelta(minutes=30)

    data = await request.json()
    doctor = data["doctor"]
    hnNumber = data["patient"]
    appointment_date = datetime.datetime.strptime(data["date"], "%d/%m/%Y")
    appointment_time = datetime.datetime.strptime(data["time"], "%H:%M")

    appointment_datetime = datetime.datetime.combine(appointment_date.date(), appointment_time.time())
    
    for existing_appointment in root.appointments.values():
        existing_appointment_date = datetime.datetime.strptime(existing_appointment.getDate(), "%d/%m/%Y")
        existing_appointment_time = datetime.datetime.strptime(existing_appointment.getTime(), "%H:%M").time()
        existing_start_time = datetime.datetime.combine(existing_appointment_date, existing_appointment_time)
        existing_end_time = existing_start_time + appointment_duration
        
        if existing_appointment.getDoctor() == doctor:
            if existing_start_time <= appointment_datetime < existing_end_time:
                return {"message": "Doctor is not available at this time"}
            elif existing_start_time <= appointment_datetime + appointment_duration < existing_end_time:
                return {"message": "Doctor is not available at this time"}
    
    id = random.randint(0, 1000000)
    while id in root.appointments.keys():
        id = random.randint(0, 1000000)
    
    appointment = Appointment(id, appointment_date.strftime("%d/%m/%Y"), appointment_time.strftime("%H:%M"), doctor, hnNumber)
    root.appointments[id] = appointment
    transaction.commit()
    
    for patient in root.patients:
        if hnNumber == root.patients[patient].getHNNumber():
            patient_email = root.patients[patient].getEmail()
             
    topic = "Appointment Confirmation"
    body = "Your appointment has been confirmed with " + doctor + " on " + appointment_date.strftime("%d/%m/%Y") + " at " + appointment_time.strftime("%H:%M")
    send_email(patient_email, topic, body)
    return {"message": "Appointment added successfully"}

# Get List of Appointments for Patient Side
@app.post("/appointment_list")
async def get_appointments(request: Request):
    data = await request.json()
    patient = data["patient"]
    appointments = []
    for appointment in root.appointments:
        if patient == root.appointments[appointment].getPatientHNNumber():
            appointment_list = {}
            appointment_list["date"] = root.appointments[appointment].getDate()
            appointment_list["time"] = root.appointments[appointment].getTime()
            appointment_list["doctor"] = root.appointments[appointment].getDoctor()
            appointments.append(appointment_list)
    return {"appointments": appointments}

# Get Doctor Schedule
@app.post("/doctor_schedule")
async def get_doctor_schedule(request: Request):
    data = await request.json()
    doctor = data["doctor"]
    appointments = []
    for appointment in root.appointments:
        if doctor == root.appointments[appointment].getDoctor():
            appointment_list = {}
            appointment_list["date"] = root.appointments[appointment].getDate()
            appointment_list["time"] = root.appointments[appointment].getTime()
            appointment_list["patientHN"] = root.appointments[appointment].getPatientHNNumber()
            for patient in root.patients:
                if root.appointments[appointment].getPatientHNNumber() == root.patients[patient].getHNNumber():
                    appointment_list["patientName"] = root.patients[patient].getFullName()
            appointments.append(appointment_list)
    return {"appointments": appointments}

# Change Profile for Doctor
@app.post("/profile_change")
async def change_profile(request: Request):
    data = await request.json()
    username = data["username"]
    password = data["new_password"]
    
    for doctor in root.doctors:
        if username == root.doctors[doctor].getUserName():
            root.doctors[doctor].setPassword(password)
            transaction.commit()
    return {"message": "Password changed successfully"}

# Get List of Patients Reports
@app.get("/patient_report")
async def get_patients_report(request: Request):
    patients = []
    for patient in root.patients:
        patient_list = {}
        patient_list["name"] = root.patients[patient].getFullName()
        patient_list["hnNumber"] = root.patients[patient].getHNNumber()
        patients.append(patient_list)
    return {"patients": patients}

# Get Individual Patient's Report
@app.get("/patient_report/{hnNumber}")
async def get_patient_report(hnNumber: str):
    global TEMP_MEDICATIONS
    global TEMP_VACCINES
    global TEMP_OTHERS
    for patient in root.patients:
        if hnNumber == root.patients[patient].getHNNumber():
            for report in root.reports:
                if hnNumber == root.reports[report].getHNNumber():
                    TEMP_OTHERS = []
                    for other in root.reports[report].getOther():
                        for others in root.others:
                            if other["id"] == root.others[others].getID():
                                TEMP_OTHERS.append(root.others[others])
                    return {
                        "message": "Report found",
                        "firstName": root.patients[hnNumber].getFirstName(),
                        "middleName": root.patients[hnNumber].getMiddleName(),
                        "lastName": root.patients[hnNumber].getLastName(),
                        "hnNumber": root.patients[hnNumber].getHNNumber(),
                        "summary": root.reports[report].getSummary(),
                        "vaccines": root.reports[report].getVaccine().copy(),
                        "medications": root.reports[report].getMedication().copy(),
                        "lab_tests": root.reports[report].getLab().copy(),
                        "others": root.reports[report].getOther().copy()
                    }
            medicalRecord = root.patients[patient].getMedicalRecord()
            thedate = datetime.datetime.now().date()
            day = thedate.day
            month = thedate.month
            year = thedate.year
            date = str(month) + "/" + str(day) + "/" + str(year)
            TEMP_VACCINES = []
            for vaccine in medicalRecord.getVaccineHistory():
                print(vaccine.getDateAdministered())
                if vaccine.getDateAdministered() == date:
                    TEMP_VACCINES.append(vaccine)
                    
            TEMP_MEDICATIONS = []
            for medication in medicalRecord.getMedicationHistory():
                print(medication.getDateAdministered())
                if medication.getDateAdministered() == date:
                    TEMP_MEDICATIONS.append(medication)
                    
            return {
                "message": "No report found",
                "firstName": medicalRecord.getFirstName(),
                "middleName": medicalRecord.getMiddleName(),
                "lastName": medicalRecord.getLastName(),
                "hnNumber": medicalRecord.getHNNumber(),
                "vaccines": TEMP_VACCINES,
                "medications": TEMP_MEDICATIONS
            }
    raise HTTPException(status_code=404, detail="Patient not found")

# Add Other Information
@app.post("/other")
async def add_other(request: Request):
    data = await request.json()
    name = data["name"]
    price = data["price"]

    for other in TEMP_OTHERS:
        if other.getName() == name:
            return {"message": "Other already added", "other": TEMP_OTHERS}
    id = random.randint(0, 1000000)
    while id in root.others.keys():
        id = random.randint(0, 1000000)
    other = Other(id, name, price)
    root.others[id] = other
    transaction.commit()
    TEMP_OTHERS.append(other)
    return {"message": "Other added successfully", "other": TEMP_OTHERS}

# Delete Other information
@app.delete("/other/{id}")
async def delete_other(id: int):
    for other in TEMP_OTHERS:
        if other.getID() == id:
            TEMP_OTHERS.remove(other)
            del root.others[id]
            return {"message": "Other deleted successfully", "other": TEMP_OTHERS}
    raise HTTPException(status_code=404, detail="Other not found")

# Create Draft Report
@app.post("/draft_report")
async def draft_report(request: Request):
    data = await request.json()
    hnNumber = data["hnNumber"]
    summary = data["summary"]
    vaccines = data["price_vaccine"]["vaccine"]
    medications = data["price_medication"]["medication"]
    lab_tests = data["price_lab_tests"]["lab_test"]
    others = data["other"]["other"]
    
    for report in root.reports:
        if hnNumber == root.reports[report].getHNNumber():
            id = root.reports[report].getID()
            report = Report(id, hnNumber, summary, vaccines, medications, lab_tests, others)
            root.reports[id] = report
            transaction.commit()
            return {"message": "Report drafted successfully"}
    id = random.randint(0, 1000000)
    while id in root.reports.keys():
        id = random.randint(0, 1000000)
    report = Report(id, hnNumber, summary, vaccines, medications, lab_tests, others)
    root.reports[id] = report
    transaction.commit()
    return {"message": "Report drafted successfully"}

# Confirm Report
@app.post("/confirm_report")
async def confirm_report(request: Request):
    data = await request.json()
    hnNumber = data["hnNumber"]
    summary = data["summary"]
    vaccines = data["price_vaccine"]["vaccine"]
    medications = data["price_medication"]["medication"]
    lab_tests = data["price_lab_tests"]["lab_test"]
    others = data["other"]["other"]
    date = data["date"]
    id = random.randint(0, 1000000)
    for report in root.reports:
        if date == root.reports[report].getDate():
            id = root.reports[report].getID()
            report = Report(id, hnNumber, summary, vaccines, medications, lab_tests, others, "pending", date)
            root.reports[id] = report
            return {"message": "Bill confirmed successfully"}
    while id in root.bills.keys():
        id = random.randint(0, 1000000)
    bill = Bill(id, hnNumber, summary, vaccines, medications, lab_tests, others, "pending", date)
    root.bills[id] = bill
    for report in root.reports:
        if hnNumber == root.reports[report].getHNNumber():
            del root.reports[report]
            transaction.commit()
    transaction.commit()
    return {"message": "Bill confirmed successfully"}

# Get List of Bills for Patient Side
@app.post("/get_bills")
async def get_bills(request: Request):
    data = await request.json()
    hnNumber = data["hnNumber"]
    bills = []
    for bill in root.bills:
        if hnNumber == root.bills[bill].getHNNumber():
            bill_list = {}
            bill_list["id"] = root.bills[bill].getID()
            bill_list["date"] = root.bills[bill].getDate()
            total_price = float(root.bills[bill].getTotalPrice())
            if total_price == 0 and root.bills[bill].getStatus() == "pending":
                for vaccine in root.bills[bill].getVaccines():
                    total_price += float(vaccine["price"])
                for medication in root.bills[bill].getMedications():
                    total_price += float(medication["price"])
                for lab_test in root.bills[bill].getLabTests():
                    total_price += float(lab_test["price"])
                for other in root.bills[bill].getOthers():
                    total_price += float(other["price"])
                root.bills[bill].setTotalPrice(total_price)
                transaction.commit()
            bill_list["totalPrice"] = total_price
            bill_list["status"] = root.bills[bill].getStatus()
            bills.append(bill_list)
    return {"bills": bills} 

# Get Individual Bill for Patient Side
@app.post("/view_bill")
async def get_bill(request: Request):
    data = await request.json()
    id = data["bill_id"]
    for bill in root.bills:
        if id == str(root.bills[bill].getID()):
            bill_list = {}
            bill_list["id"] = root.bills[bill].getID()
            bill_list["date"] = root.bills[bill].getDate()
            bill_list["status"] = root.bills[bill].getStatus()
            hnNumber = root.bills[bill].getHNNumber()
            for patient in root.patients:
                if hnNumber == root.patients[patient].getHNNumber():
                    bill_list["hnNumber"] = hnNumber
                    bill_list["patientName"] = root.patients[patient].getFullName()
            total_price = root.bills[bill].getTotalPrice()
            bill_list["totalPrice"] = total_price
            items = []
            for vaccine in root.bills[bill].getVaccines():
                item = {}
                item["name"] = vaccine["name"]
                item["price"] = vaccine["price"]
                items.append(item)
            for medication in root.bills[bill].getMedications():
                item = {}
                item["name"] = medication["name"]
                item["price"] = medication["price"]
                items.append(item)
            for lab_test in root.bills[bill].getLabTests():
                item = {}
                item["name"] = lab_test["labType"]
                item["price"] = lab_test["price"]
                items.append(item)
            for other in root.bills[bill].getOthers():
                item = {}
                item["name"] = other["name"]
                item["price"] = other["price"]
                items.append(item)
            bill_list["items"] = items
            return {"bill": bill_list}

# Apply Discount from Patient's Side
@app.post("/apply_discount")
async def apply_discount(request: Request):
    data = await request.json()
    id = data["bill_id"]
    discount = data["discount"]
    if discount == "Health Insurance Card":
        insurance = data["insurance"]
    for bill in root.bills:
        if id == str(root.bills[bill].getID()):
            total_price = root.bills[bill].getTotalPrice()
            bill_list = {}
            bill_list["id"] = root.bills[bill].getID()
            bill_list["date"] = root.bills[bill].getDate()
            hnNumber = root.bills[bill].getHNNumber()
            for patient in root.patients:
                if hnNumber == root.patients[patient].getHNNumber():
                    bill_list["hnNumber"] = hnNumber
                    bill_list["patientName"] = root.patients[patient].getFullName()
            total_price = float(total_price)
            if discount == "Medical Golden Card":
                total_price = 30
            elif discount == "Health Insurance Card":
                total_price = total_price - (total_price * insurance)
            elif discount == "Clinic Member Card":
                total_price = total_price - (total_price * 0.1)
            bill_list["totalPrice"] = total_price
            root.bills[bill].setTotalPrice(total_price)
            root.bills[bill].setStatus("Pending (Discount Applied)")
            transaction.commit()
            bill_list["status"] = root.bills[bill].getStatus()
            items = []
            for vaccine in root.bills[bill].getVaccines():
                item = {}
                item["name"] = vaccine["name"]
                item["price"] = vaccine["price"]
                items.append(item)
            for medication in root.bills[bill].getMedications():
                item = {}
                item["name"] = medication["name"]
                item["price"] = medication["price"]
                items.append(item)
            for lab_test in root.bills[bill].getLabTests():
                item = {}
                item["name"] = lab_test["labType"]
                item["price"] = lab_test["price"]
                items.append(item)
            for other in root.bills[bill].getOthers():
                item = {}
                item["name"] = other["name"]
                item["price"] = other["price"]
                items.append(item)
            bill_list["items"] = items
            return {"message": "Discount applied successfully", "bill": bill_list}

# Get List of Bills for Doctor Side
@app.get("/doctor_get_bills")
async def get_bills():
    bills = []
    for bill in root.bills:
        bill_list = {}
        bill_list["id"] = root.bills[bill].getID()
        bill_list["date"] = root.bills[bill].getDate()
        bill_list["status"] = root.bills[bill].getStatus()
        hnNumber = root.bills[bill].getHNNumber()
        for patient in root.patients:
            if hnNumber == root.patients[patient].getHNNumber():
                bill_list["hnNumber"] = hnNumber
                bill_list["patientName"] = root.patients[patient].getFullName()
        total_price = root.bills[bill].getTotalPrice()
        if total_price == 0 and root.bills[bill].getStatus() == "pending":
            for vaccine in root.bills[bill].getVaccines():
                total_price += float(vaccine["price"])
            for medication in root.bills[bill].getMedications():
                total_price += float(medication["price"])
            for lab_test in root.bills[bill].getLabTests():
                total_price += float(lab_test["price"])
            for other in root.bills[bill].getOthers():
                total_price += float(other["price"])
            root.bills[bill].setTotalPrice(total_price)
            transaction.commit()
        bill_list["totalPrice"] = total_price
        bills.append(bill_list)
    return {"bills": bills}

# Change Status for Bill Payment
@app.post("/change_status")
async def change_status(request: Request):
    data = await request.json()
    id = data["bill_id"]
    for bill in root.bills:
        if id == str(root.bills[bill].getID()):
            bill_list = {}
            root.bills[bill].setStatus("Completed")
            transaction.commit()
            bill_list["id"] = root.bills[bill].getID()
            bill_list["date"] = root.bills[bill].getDate()
            bill_list["status"] = root.bills[bill].getStatus()
            hnNumber = root.bills[bill].getHNNumber()
            for patient in root.patients:
                if hnNumber == root.patients[patient].getHNNumber():
                    bill_list["hnNumber"] = hnNumber
                    bill_list["patientName"] = root.patients[patient].getFullName()
            total_price = root.bills[bill].getTotalPrice()
            bill_list["totalPrice"] = total_price
            items = []
            for vaccine in root.bills[bill].getVaccines():
                item = {}
                item["name"] = vaccine["name"]
                item["price"] = vaccine["price"]
                items.append(item)
            for medication in root.bills[bill].getMedications():
                item = {}
                item["name"] = medication["name"]
                item["price"] = medication["price"]
                items.append(item)
            for lab_test in root.bills[bill].getLabTests():
                item = {}
                item["name"] = lab_test["labType"]
                item["price"] = lab_test["price"]
                items.append(item)
            for other in root.bills[bill].getOthers():
                item = {}
                item["name"] = other["name"]
                item["price"] = other["price"]
                items.append(item)
            bill_list["items"] = items
            return {"bill": bill_list}

# Get Lab Tests for individual Patient
@app.post("/lab_test_list")
async def get_lab_tests(request: Request):
    data = await request.json()
    hnNumber = data["hnNumber"]
    date = data["date"]

    lab_tests = []
    for lab_test in root.lab_requests:
        if hnNumber == root.lab_requests[lab_test].getPatientHNNumber() and date == root.lab_requests[lab_test].getDate():
            lab_tests.append(root.lab_requests[lab_test])
    return {"lab_tests": lab_tests}

# Get List of Specialities of Doctors for appointment combo box
@app.get("/doctor_speciality")
async def get_doctor_speciality():
    speciality = []
    for doctor in root.doctors:
        speciality_list = {}
        speciality_list["speciality"] = root.doctors[doctor].getSpeciality()
        speciality.append(speciality_list)
    return {"speciality": speciality}

@app.get("/doctor_speciality/{specialty}")
async def get_doctor_speciality(specialty: str):
    doctors = []
    for doctor in root.doctors:
        if specialty == root.doctors[doctor].getSpeciality():
            doctor_list = {}
            doctor_list["name"] = root.doctors[doctor].getFullName()
            doctors.append(doctor_list)
    return {"doctors": doctors}

# Make Lab Request for individual Patient
@app.post("/lab_request")
async def make_lab_request(request: Request):
    data = await request.json()
    
    date = data["date"][16:]
    time = data["time"][16:]
    requestType = data["requestType"]
    urgency = data["urgency"]
    faculty = data["faculty"]
    hnNumber = data["hnNumber"]
    patientName = data["patientName"]
    doctorName = data["doctorName"]
    reason = data["reason"]
    
    for labRequest in root.lab_requests:
        if hnNumber == root.lab_requests[labRequest].getPatientHNNumber() and date == root.lab_requests[labRequest].getDate() and time == root.lab_requests[labRequest].getTime():
            return {"message": "Lab request already added"}
    id = random.randint(0, 1000000)
    while id in root.others.keys():
        id = random.randint(0, 1000000)
    labRequest = Lab_request(id, date, time, requestType, urgency, faculty, hnNumber, patientName, doctorName, reason)
    root.lab_requests[id] = labRequest
    transaction.commit()
    return {"message": "Lab request added successfully"}

# Get Lab Request for individual Patient
@app.post("/get_lab_requests")
async def get_lab_requests(request: Request):
    data = await request.json()
    department = data["department"]
    lab_requests = []
    for lab_request in root.lab_requests:
        if department == root.lab_requests[lab_request].getFaculty() and root.lab_requests[lab_request].getReply() == None:
            lab_request_list = {}
            lab_request_list["date"] = root.lab_requests[lab_request].getDate()
            lab_request_list["time"] = root.lab_requests[lab_request].getTime()
            lab_request_list["requestType"] = root.lab_requests[lab_request].getLabType()
            lab_request_list["urgency"] = root.lab_requests[lab_request].getUrgency()
            lab_request_list["hnNumber"] = root.lab_requests[lab_request].getPatientHNNumber()
            lab_request_list["patientName"] = root.lab_requests[lab_request].getPatientName()
            lab_request_list["doctorName"] = root.lab_requests[lab_request].getRequestingDoctor()
            lab_request_list["reason"] = root.lab_requests[lab_request].getReason()
            lab_requests.append(lab_request_list)
    return {"lab_requests": lab_requests}         
  
# Get List of Departments
@app.get("/department")
async def get_department():
    department = []
    for doctor in root.doctors:
        if root.doctors[doctor].getSpeciality() not in department:
            department.append(root.doctors[doctor].getSpeciality())
    return {"department": department}

# Create Lab Reply for Individual Patient
@app.post("/lab_reply/{hnNumber}/{date}/{time}")
async def lab_reply(hnNumber: str, date: str, time: str):
    lab_request_details = {}
    for request in root.lab_requests:
        if hnNumber == root.lab_requests[request].getPatientHNNumber() and date == root.lab_requests[request].getDate() and time == root.lab_requests[request].getTime():
            lab_request_details["date"] = root.lab_requests[request].getDate()
            lab_request_details["time"] = root.lab_requests[request].getTime()
            lab_request_details["requestType"] = root.lab_requests[request].getLabType()
            lab_request_details["urgency"] = root.lab_requests[request].getUrgency()
            lab_request_details["faculty"] = root.lab_requests[request].getFaculty()
            lab_request_details["hnNumber"] = root.lab_requests[request].getPatientHNNumber()
            lab_request_details["patientName"] = root.lab_requests[request].getPatientName()
            lab_request_details["doctorName"] = root.lab_requests[request].getRequestingDoctor()
            lab_request_details["reason"] = root.lab_requests[request].getReason()
    return {"lab_request": lab_request_details}

# Make Lab Reply for Individual Patient
@app.post("/make_lab_reply")
async def make_lab_reply(request: Request):
    data = await request.json()
    
    note = data["note"]
    filename = data["file"]
    hnNumber = data["hnNumber"]
    date = data["date"]
    time = data["time"]
    id = random.randint(0, 1000000)
    while id in root.others.keys():
        id = random.randint(0, 1000000)
    lab_reply = Lab_reply(id, note, filename)
    root.lab_replies[id] = lab_reply
    for lab_request in root.lab_requests:
        if hnNumber == root.lab_requests[lab_request].getPatientHNNumber() and date == root.lab_requests[lab_request].getDate() and time == root.lab_requests[lab_request].getTime():
            root.lab_requests[lab_request].setReply(lab_reply)
            transaction.commit()
            return {"message": "Lab reply added successfully"}

# Reject Lab Request for Individual Patient    
@app.post("/reject_lab_request")
async def reject_lab_request(request: Request):
    data = await request.json()
    
    hnNumber = data["hnNumber"]
    date = data["date"]
    time = data["time"]
    
    id = random.randint(0, 1000000)
    while id in root.others.keys():
        id = random.randint(0, 1000000)
    
    lab_result = Lab_reply(id, None, None)
    root.lab_replies[id] = lab_result
    
    for lab_request in root.lab_requests:
        if hnNumber == root.lab_requests[lab_request].getPatientHNNumber() and date == root.lab_requests[lab_request].getDate() and time == root.lab_requests[lab_request].getTime():
            root.lab_requests[lab_request].setReply(lab_result)
            transaction.commit()
            return {"message": "Lab request rejected successfully"}

# Get List of Lab Replies for Doctor Side       
@app.post("/view_received_replies")
async def received_replies(request: Request):
    data = await request.json()
    
    name = data["name"]
    
    lab_replies = []
    for lab_request in root.lab_requests:
        if root.lab_requests[lab_request].getReply() != None and name == root.lab_requests[lab_request].getRequestingDoctor():
            lab_reply_list = {}
            lab_reply_list["date"] = root.lab_requests[lab_request].getDate()
            lab_reply_list["time"] = root.lab_requests[lab_request].getTime()
            lab_reply_list["requestType"] = root.lab_requests[lab_request].getLabType()
            lab_reply_list["hnNumber"] = root.lab_requests[lab_request].getPatientHNNumber()
            lab_reply_list["patientName"] = root.lab_requests[lab_request].getPatientName()
            lab_replies.append(lab_reply_list)
    return {"lab_replies": lab_replies}

# View Induvidual Lab Reply for Doctor Side
@app.post("/view_lab_reply/{hnNumber}/{date}/{time}")
async def view_lab_reply(hnNumber: str, date: str, time: str):
    lab_reply_details = {}
    for lab_request in root.lab_requests:
        if hnNumber == root.lab_requests[lab_request].getPatientHNNumber() and date == root.lab_requests[lab_request].getDate() and time == root.lab_requests[lab_request].getTime():
            lab_reply = root.lab_requests[lab_request].getReply()
            lab_reply_details["date"] = root.lab_requests[lab_request].getDate()
            lab_reply_details["hnNumber"] = root.lab_requests[lab_request].getPatientHNNumber()
            lab_reply_details["time"] = root.lab_requests[lab_request].getTime()
            lab_reply_details["requestType"] = root.lab_requests[lab_request].getLabType()
            lab_reply_details["note"] = lab_reply.getNote()
            lab_reply_details["file"] = lab_reply.getFile()
            lab_reply_details["patientName"] = root.lab_requests[lab_request].getPatientName()
    return {"lab_reply": lab_reply_details}

# Get Lab Result for Individual Patient
@app.post("/get_lab_result")
async def get_lab_result(request: Request):
    data = await request.json()
    
    hnNumber = data["hnNumber"]
    
    lab_replies = []
    for lab_request in root.lab_requests:
        if hnNumber == root.lab_requests[lab_request].getPatientHNNumber():
            lab_reply_list = {}
            lab_reply_list["date"] = root.lab_requests[lab_request].getDate()
            lab_reply_list["time"] = root.lab_requests[lab_request].getTime()
            lab_reply_list["labType"] = root.lab_requests[lab_request].getLabType()
            lab_reply_list["hnNumber"] = root.lab_requests[lab_request].getPatientHNNumber()
            lab_reply_list["requesting_doctor"] = root.lab_requests[lab_request].getRequestingDoctor()
            lab_reply_list["lab_test"] = root.lab_requests[lab_request].getReply()
            lab_replies.append(lab_reply_list)
    return {"lab_replies": lab_replies}

# Search for Patient List from HN Number
@app.get("/patient_list/{search}")
async def search_patient(search: str):
    patients = []
    for patient in root.patients:
        if search in root.patients[patient].getHNNumber():
            patient_list = {}
            patient_list["name"] = root.patients[patient].getFullName()
            patient_list["hnNumber"] = root.patients[patient].getHNNumber()
            patients.append(patient_list)
    return {"patients": patients}

# Get Doctor List from searching username
@app.get("/doctor_list/{search_username}")
async def search_doctor(search_username: str):
    doctors = []
    for doctor in root.doctors:
        if search_username in root.doctors[doctor].getUserName():
            doctor_list = {}
            doctor_list["name"] = root.doctors[doctor].getFullName()
            doctor_list["username"] = root.doctors[doctor].getUserName()
            doctor_list["passwordID"] = root.doctors[doctor].getPassword()
            doctor_list["speciality"] = root.doctors[doctor].getSpeciality()
            doctors.append(doctor_list)
    return {"doctors": doctors}

# Search Doctor Schedule by Date and HN Number
@app.post("/doctor_schedule/{search_date}/{search_hn}")
async def search_doctor_schedule(request: Request, search_date: str, search_hn: str):
    data = await request.json()
    doctor = data["doctor"]
    appointments = []
    for appointment in root.appointments:
        date_object = datetime.datetime.strptime(root.appointments[appointment].getDate(), "%m/%d/%Y")
        formatted_date = date_object.strftime("%m-%d-%Y")
        if doctor == root.appointments[appointment].getDoctor() and search_date == formatted_date and search_hn == root.appointments[appointment].getPatientHNNumber():
            appointment_list = {}
            appointment_list["date"] = root.appointments[appointment].getDate()
            appointment_list["time"] = root.appointments[appointment].getTime()
            appointment_list["patientHN"] = root.appointments[appointment].getPatientHNNumber()
            for patient in root.patients:
                if root.appointments[appointment].getPatientHNNumber() == root.patients[patient].getHNNumber():
                    appointment_list["patientName"] = root.patients[patient].getFullName()
            appointments.append(appointment_list)
    return {"appointments": appointments}

# Search Appointment by Date
@app.post("/appointment_list/{search_date}")
async def search_appointment(request: Request, search_date: str):
    data = await request.json()
    patient = data["patient"]
    appointments = []
    for appointment in root.appointments:
        date_object = datetime.datetime.strptime(root.appointments[appointment].getDate(), "%d/%m/%Y")
        formatted_date = date_object.strftime("%m-%d-%Y")
        if patient == root.appointments[appointment].getPatientHNNumber() and search_date == formatted_date:
            appointment_list = {}
            appointment_list["date"] = root.appointments[appointment].getDate()
            appointment_list["time"] = root.appointments[appointment].getTime()
            appointment_list["doctor"] = root.appointments[appointment].getDoctor()
            appointments.append(appointment_list)
    return {"appointments": appointments}

# Cancel Appointment
@app.post("/cancel_appointment")
async def cancel_appointment(request:Request):
    data = await request.json()
    date = data["date"]
    time = data["time"]
    doctor = data["doctor"]
    patient = data["patient"]
    for appointment in root.appointments:
        if date == root.appointments[appointment].getDate() and time == root.appointments[appointment].getTime() and doctor == root.appointments[appointment].getDoctor() and patient == root.appointments[appointment].getPatientHNNumber():
            del root.appointments[appointment]
            transaction.commit()
            return {"message": "Appointment cancelled successfully"}
    return {"message": "Appointment not found"}

# Reset Report      
async def reset_report():
    for report in root.reports:
        del root.reports[report]
        transaction.commit()

# Checking the appointment date
@app.get("/close")
async def close():
    global TEMP_MEDICATIONS
    global TEMP_VACCINES
    global TEMP_ALLERGIES
    global TEMP_OTHERS
    TEMP_MEDICATIONS = []
    TEMP_VACCINES = []
    TEMP_ALLERGIES = []
    TEMP_OTHERS = []
    date = datetime.datetime.now().date()
    
    day = date.day
    month = date.month
    year = date.year
    
    if len(root.pastday) == 0:
        pastdate = PastDate(day, month, year)
        root.pastday["pastdate"] = pastdate
        transaction.commit()
    else:
        if root.pastday["pastdate"].getYear() < year:
            reset_report()
            root.pastday["pastdate"].setYear(year)
            root.pastday["pastdate"].setMonth(month)
            root.pastday["pastdate"].setDay(day)
            transaction.commit()
        elif root.pastday["pastdate"].getMonth() < month:
            reset_report()
            root.pastday["pastdate"].setMonth(month)
            root.pastday["pastdate"].setDay(day)
            transaction.commit()
        elif root.pastday["pastdate"].getDay() < day:
            reset_report()
            root.pastday["pastdate"].setMonth(month)
            root.pastday["pastdate"].setDay(day)
            transaction.commit()




