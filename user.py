import persistent

class User(persistent.Persistent):
    def __init__(self, firstName, middleName, lastName, password, profile, email):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.password = password
        self.profile = profile
        self.email = email
    
    def getFullName(self):      
        if self.middleName:
            return f"{self.firstName} {self.middleName} {self.lastName}"
        return f"{self.firstName} {self.lastName}"
    
    def getFirstName(self): 
        return self.firstName
    
    def getMiddleName(self):  
        return self.middleName
    
    def getLastName(self):     
        return self.lastName 
    
    def getPassword(self):   
        return self.password
    
    def getProfile(self):   
        return self.profile
    
    def getEmail(self):
        return self.email
    
    def setFirstName(self, firstName):  
        self.firstName = firstName
    
    def setMiddleName(self, middleName): 
        self.middleName = middleName
    
    def setLastName(self, lastName):  
        self.lastName = lastName
    
    def setPassword(self, password):  
        self.password = password

class Patient(User, persistent.Persistent):
    def __init__(self, firstName, middleName, lastName, password, hnNumber, medicalRecord, profile, email):
        super().__init__(firstName, middleName, lastName, password, profile, email)
        self.hnNumber = hnNumber
        self.medicalRecord = medicalRecord
    
    def getHNNumber(self):   
        return self.hnNumber
    
    def getMedicalRecord(self):  
        return self.medicalRecord
  
class MedicalStaff(User, persistent.Persistent):
    def __init__(self, firstName, middleName, lastName, password, userName, profile, email):
        super().__init__(firstName, middleName, lastName, password, profile, email)
        self.userName = userName
    
    def getUserName(self):    
        return self.userName

class Doctor(MedicalStaff, persistent.Persistent):
    def __init__(self, firstName, middleName, lastName, password, userName, speciality, profile, email):
        super().__init__(firstName, middleName, lastName, password, userName, profile, email)
        self.speciality = speciality
    
    def getFullName(self):  
        return "Dr." + super().getFullName()
    
    def getSpeciality(self):   
        return self.speciality
    
class MedicalRecord(persistent.Persistent):
    def __init__(self, firstName, middleName, lastName, hnNumber, birthDate, sex, bloodType, weight, height, medicationHistory, allergy, vaccineHistory, address, tel, bloodPressure):
        self.firstName = firstName
        self.middleName = middleName
        self.lastName = lastName
        self.hnNumber = hnNumber
        self.birthDate = birthDate
        self.sex = sex
        self.bloodType = bloodType
        self.weight = weight
        self.height = height
        self.medicationHistory = medicationHistory
        self.allergy = allergy
        self.vaccineHistory = vaccineHistory
        self.address = address
        self.tel = tel
        self.bloodPressure = bloodPressure
        self.appointmentList = []
    
    def getFullName(self):    
        if self.middleName:
            return f"{self.firstName} {self.middleName} {self.lastName}"
        return f"{self.firstName} {self.lastName}"
    
    def getFirstName(self):   
        return self.firstName
    
    def getMiddleName(self):   
        return self.middleName
    
    def getLastName(self):   
        return self.lastName
    
    def getHNNumber(self):    
        return self.hnNumber
    
    def getBirthDate(self):     
        return self.birthDate
    
    def getSex(self):     
        return self.sex
    
    def getBloodType(self):  
        return self.bloodType
    
    def getWeight(self):  
        return self.weight
    
    def getHeight(self):     
        return self.height
    
    def getMedicationHistory(self):     
        return self.medicationHistory
    
    def getAllergy(self): 
        return self.allergy
    
    def getVaccineHistory(self):   
        return self.vaccineHistory

    def getAddress(self):   
        return self.address
    
    def getTel(self):    
        return self.tel
    
    def getBloodPressure(self):  
        return self.bloodPressure
    
    def setFirstName(self, firstName):  
        self.firstName = firstName
        
    def setMiddleName(self, middleName):
        self.middleName = middleName
        
    def setLastName(self, lastName):
        self.lastName = lastName
        
    def setHNNumber(self, hnNumber):
        self.hnNumber = hnNumber
        
    def setBirthDate(self, birthDate):
        self.birthDate = birthDate
    
    def setSex(self, sex):
        self.sex = sex
    
    def setBloodType(self, bloodType):
        self.bloodType = bloodType
    
    def setWeight(self, weight):
        self.weight = weight
    
    def setHeight(self, height):
        self.height = height

    def setAddress(self, address):
        self.address = address
        
    def setTel(self, tel):
        self.tel = tel
        
    def setBloodPressure(self, bloodPressure):
        self.bloodPressure = bloodPressure
    
    def setMedicationHistory(self, medicationHistory):
        self.medicationHistory = medicationHistory
    
    def setAllergy(self, allergy):
        self.allergy = allergy
        
    def setVaccineHistory(self, vaccineHistory):
        self.vaccineHistory = vaccineHistory

class Medication(persistent.Persistent):
    def __init__(self, id, name, amount, dosage, duration, doctorAdministered, dateAdministered, timeAdministered, sidenote):
        self.id = id
        self.name = name
        self.amount = amount
        self.dosage = dosage
        self.duration = duration
        self.doctorAdministered = doctorAdministered
        self.dateAdministered = dateAdministered
        self.timeAdministered = timeAdministered
        self.sidenote = sidenote
    
    def getID(self):
        return self.id 
    
    def getName(self):
        return self.name 
    
    def getAmount(self):
        return self.amount 
    
    def getDosage(self):
        return self.dosage 
    
    def getDuration(self):
        return self.duration 
    
    def getSidenote(self):
        return self.sidenote 
    
    def getDoctorAdministered(self):
        return self.doctorAdministered 
    
    def getDateAdministered(self):
        return self.dateAdministered 
    
    def getTimeAdministered(self):
        return self.timeAdministered 
        
    def setAmount(self, amount):
        self.amount = amount 
        
    def setDosage(self, dosage):
        self.dosage = dosage 

class Vaccine(persistent.Persistent):
    def __init__(self, id, name, dateAdministered):
        self.id = id
        self.name = name
        self.dateAdministered = dateAdministered

    def getID(self):
        return self.id 
    
    def getName(self):
        return self.name 
    
    def getDateAdministered(self):
        return self.dateAdministered 
    
class Allergy(persistent.Persistent):
    def __init__(self, id, allergy):
        self. id = id
        self.allergy = allergy
        
    def getID(self):
        return self.id 

    def getName(self):
        return self.allergy 
    
class Other(persistent.Persistent):
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def getID(self):
        return self.id 
    
    def getName(self):
        return self.name 
    
    def getPrice(self):
        return self.price 
    
class Appointment(persistent.Persistent):
    def __init__(self, id, date, time, doctor, patientHNNumber):
        self.id = id
        self.date = date
        self.time = time
        self.doctor = doctor
        self.patientHNNumber = patientHNNumber

    def getID(self):
        return self.id 
    
    def getDate(self):
        return self.date 
    
    def getTime(self):
        return self.time 
    
    def getDoctor(self):
        return self.doctor 
    
    def getPatientHNNumber(self):
        return self.patientHNNumber 
 
class Report(persistent.Persistent):
    def __init__(self, id, hnNumber,  summary, vaccine, medication, lab, other):
        self.id = id
        self.hnNumber = hnNumber
        self.summary = summary
        self.vaccine = vaccine
        self.medication = medication
        self.lab = lab
        self.other = other

    def getID(self):
        return self.id 
    
    def getHNNumber(self):
        return self.hnNumber 

    def getSummary(self):
        return self.summary 

    def getVaccine(self):
        return self.vaccine 
    
    def getMedication(self):
        return self.medication 
    
    def getLab(self):
        return self.lab 
    
    def getOther(self):
        return self.other 
    
class Bill(persistent.Persistent):
    def __init__(self, id, hnNumber, summary, vaccines, medications, lab_tests, others, status, date):
        self.id = id
        self.hnNumber = hnNumber
        self.summary = summary
        self.vaccines = vaccines
        self.medications = medications
        self.lab_tests = lab_tests
        self.others = others
        self.status = status
        self.date = date
        self.total_price = 0

    def getID(self):
        return self.id 
    
    def getHNNumber(self):
        return self.hnNumber 
    
    def getSummary(self):
        return self.summary
    
    def getVaccines(self):
        return self.vaccines 
    
    def getMedications(self):
        return self.medications 
    
    def getLabTests(self):
        return self.lab_tests 
    
    def getOthers(self):
        return self.others 

    def getStatus(self):
        return self.status 
    
    def getDate(self):
        return self.date 

    def getTotalPrice(self):
        return self.total_price 
    
    def setStatus(self, status):
        self.status = status 
    
    def setTotalPrice(self, total_price):
        self.total_price = total_price 

class Lab_reply(persistent.Persistent):
    def __init__(self, id, notes, file):
        self.id = id
        self.notes = notes
        self.file = file
    
    def getID(self):
        return self.id 
    
    def getNote(self):
        return self.notes 
    
    def getFile(self):
        return self.file 

class Lab_request(persistent.Persistent):
    def __init__(self, id, date, time, labType, urgency, faculty, patientHNNumber, patientName, requesting_doctor, reason):
        self.id = id
        self.date = date
        self.time = time
        self.labType = labType
        self.urgency = urgency
        self.faculty = faculty
        self.requesting_doctor = requesting_doctor
        self.patientHNNumber = patientHNNumber
        self.patientName = patientName
        self.reason = reason
        self.reply = None
    
    def getID(self):
        return self.id 
    
    def getDate(self):
        return self.date 
    
    def getTime(self):
        return self.time 
    
    def getLabType(self):
        return self.labType 
    
    def getUrgency(self):
        return self.urgency 
    
    def getFaculty(self):
        return self.faculty 
    
    def getRequestingDoctor(self):
        return self.requesting_doctor 
    
    def getPatientHNNumber(self):
        return self.patientHNNumber 
    
    def getPatientName(self):
        return self.patientName 
    
    def getReason(self):
        return self.reason 
    
    def getReply(self):
        return self.reply 
    
    def setReply(self, reply):
        self.reply = reply 
    
class PastDate(persistent.Persistent):
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
    
    def getDay(self):  
        return self.day
    
    def getMonth(self):     
        return self.month
    
    def getYear(self): 
        return self.year
    
    def setDay(self, day): 
        self.day = day
        
    def setMonth(self, month): 
        self.month = month
        
    def setYear(self, year): 
        self.year = year