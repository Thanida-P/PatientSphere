import os
from PySide6.QtWidgets import (QMainWindow, QApplication, QDialog, QMessageBox, QVBoxLayout, QLineEdit, QDateEdit, QFileDialog
,QPushButton, QTableWidgetItem, QTimeEdit, QComboBox, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QTableWidgetItem, QWidget)
from PySide6.QtCore import QUrl, QJsonDocument, QJsonValue, QDate
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
from PySide6.QtGui import QPixmap, QImage
import sys
from user import *
from main_ui_ui import Ui_MainWindow
from static import *
from camera import Camera
from datetime import datetime
import shutil

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PatientSphere")
        self.network_manager = QNetworkAccessManager()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.check_session()

        self.vaccine_list = []
        self.medication_list = []
        self.allergy_list = []
        self.lab_test_list = []
        self.other_list = []
        self.profile = ""
        self.file = ""
        self.current_user = {}

        # connect buttons
        self.ui.loginButton.clicked.connect(self.login)
        # DOCTOR
        self.ui.home_Button.clicked.connect(self.switch_to_doctor_home)
        self.ui.home_patient_icon.clicked.connect(self.manage_patient_list)
        self.ui.patientListButton.clicked.connect(self.manage_patient_list)
        self.ui.AddPatientButton.clicked.connect(self.add_patient_page)
        self.ui.browse_page.clicked.connect(self.browse_profile)
        self.ui.take_pic_button.clicked.connect(self.patient_take_picture)
        self.ui.add_vaccine_button.clicked.connect(self.add_vaccine_page)
        self.ui.add_medication_button.clicked.connect(self.add_medication_page)
        self.ui.add_allergy_button.clicked.connect(self.add_allergy_page)
        self.ui.delete_vaccine_button.clicked.connect(self.delete_vaccine)
        self.ui.delete_medication_button.clicked.connect(self.delete_medication)
        self.ui.delete_allergy_button.clicked.connect(self.delete_allergy)
        self.ui.confirm_button_2.clicked.connect(self.create_patient)
        self.ui.cancel_button_2.clicked.connect(self.cancel_add_patient)
        self.ui.edit_patient_info_button.clicked.connect(self.edit_patient_info)
        self.ui.edit_patient_info.clicked.connect(self.edit_patient_info_from_profile)
        self.ui.view_patient_info_button.clicked.connect(self.view_patient_info)
        self.ui.back_button_2.clicked.connect(self.switch_to_doctor_patient_list)
        self.ui.doctor_setting_button.clicked.connect(self.profile_page)
        self.ui.doctor_setting_button_2.clicked.connect(self.profile_page)
        self.ui.confirm_button.clicked.connect(self.profile_change)
        self.ui.cancel_button.clicked.connect(self.doctor_linedit_clear)
        self.ui.reportButton.clicked.connect(self.view_patients_report)
        self.ui.home_report_icon.clicked.connect(self.view_patients_report)
        self.ui.reportButton.clicked.connect(self.view_patients_report)
        self.ui.home_lab_icon.clicked.connect(self.get_lab_request)
        self.ui.labButton.clicked.connect(self.get_lab_request) 
        self.ui.bill_list_icon.clicked.connect(self.doctor_view_bill_list)
        self.ui.billButton.clicked.connect(self.doctor_view_bill_list)
        self.ui.doctor_view_bill_button.clicked.connect(self.doctor_view_bill)
        self.ui.confirm_payment_button.clicked.connect(self.change_status)
        self.ui.submit_button.clicked.connect(self.make_lab_request)
        self.ui.make_lab_request_button.clicked.connect(self.get_department)
        self.ui.report_cancel_button.clicked.connect(self.cancel_report)
        self.ui.viewButton.clicked.connect(self.view_lab_reply)
        self.ui.backBT.clicked.connect(self.back_from_view_lab_reply)
        self.ui.home_schedule_icon.clicked.connect(self.manage_doctor_schedule)
        self.ui.scheduleButton.clicked.connect(self.manage_doctor_schedule)
        self.ui.report_edit_button.clicked.connect(self.report_page)
        self.ui.report_add_other.clicked.connect(self.add_other_dialog)
        self.ui.report_delete_other.clicked.connect(self.delete_other)
        self.ui.searchButton.clicked.connect(self.search_patient)
        self.ui.search_button.clicked.connect(self.search_schedule)
        self.ui.view_received_replies.clicked.connect(self.view_received_replies) 
        self.ui.backBT2.clicked.connect(self.view_received_replies)
        self.ui.backBT3.clicked.connect(self.view_received_replies)
        self.ui.reject_lab_reply.clicked.connect(self.reject_lab_request)
        self.ui.report_draft_button.clicked.connect(self.draft_report)
        self.ui.report_confirm_button.clicked.connect(self.confirm_report)
        

        # PATIENT
        self.ui.home_Button_2.clicked.connect(self.switch_to_patient_home)
        self.ui.new_appointment_button.clicked.connect(self.get_specialty_list)
        self.ui.patient_appointment_icon.clicked.connect(self.manage_schedule)
        self.ui.manageAppointmentButton.clicked.connect(self.manage_schedule)
        self.ui.search_date_button.clicked.connect(self.search_appointment)
        self.ui.patient_record_icon.clicked.connect(self.display_medical_record)
        self.ui.viewMedRecord_button.clicked.connect(self.display_medical_record)
        self.ui.select_discount.currentIndexChanged.connect(self.toggle_discount)
        self.ui.apply_discount_button.clicked.connect(self.apply_discount)
        self.ui.view_bill_button.clicked.connect(self.view_bill)
        self.ui.cancel_appointment.clicked.connect(self.cancel_appointment)
        self.ui.billPaymentButton.clicked.connect(self.manage_bill_payment)
        self.ui.patient_payment_icon.clicked.connect(self.manage_bill_payment)
        self.ui.upload_file_button.clicked.connect(self.file_upload)
        self.ui.insurance.setVisible(False)


        # ADMIN
        self.ui.addDoctorButton.clicked.connect(self.add_doctor)
        self.ui.browse_page_2.clicked.connect(self.browse_profile2)
        self.ui.take_pic_button_2.clicked.connect(self.doctor_take_picture)
        self.ui.back_button.clicked.connect(self.cancel_add_doctor)
        self.ui.see_doctor_list_button.clicked.connect(self.view_doctor_list)
        self.ui.make_lab_reply_button.clicked.connect(self.lab_reply_page)
        self.ui.confirm_lab_reply.clicked.connect(self.submit_lab_reply)
        self.ui.cancel_lab_reply.clicked.connect(self.cancel_lab_reply)
        self.ui.cancel_lab_reply.clicked.connect(self.cancel_lab_reply)
        self.ui.search_username_button.clicked.connect(self.search_doctor)


        # SHOW PASSWORD 
        self.ui.show_password_button.clicked.connect(self.show_password)
        self.ui.show_old_password.clicked.connect(self.show_old_password)
        self.ui.show_new_password.clicked.connect(self.show_new_password)
        self.ui.show_confirm_password.clicked.connect(self.show_confirm_password)
        
        
        # LOG OUT
        self.ui.logout_button.clicked.connect(self.logout)
        self.ui.logout_button_2.clicked.connect(self.logout)
        self.ui.logout_button_3.clicked.connect(self.logout)
        self.ui.logout_button_4.clicked.connect(self.logout)
        self.ui.logout_button_5.clicked.connect(self.logout) 

############################################# LOG IN ##########################################################################

    def login(self):
        username, password = self.get_login_data()
        
        if username == "" or password == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in both username and password fields.")
            dialog.exec()
            return

        url = QUrl("http://localhost:5000/login") # api endpoint for login
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "username": QJsonValue(username),
            "password": QJsonValue(password)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_login_reply)

    def get_login_data(self):
        username = self.ui.username.text()
        password = self.ui.password.text()

        return username, password

    def handle_login_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            headers = reply.rawHeaderPairs()
            for header in headers:
                if header[0].data().decode() == b"Set-Cookie":
                    self.session_cookie = header[1].data().decode().split(";")[0]
            
            data = reply.readAll()
            login_data = QJsonDocument.fromJson(data).object()
            
            message = login_data["message"]

            if message == "User not found":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("User not found.")
                dialog.exec()
                return
            elif message == "Incorrect password":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Your password is incorrect. Please try again.")
                dialog.exec()
                return
            elif message == "admin user":
                self.ui.directory.setHidden(True)
                self.ui.stackedWidget.setCurrentIndex(6)
            else:
                user = login_data["user_data"]
                user_type = login_data["type"]
                self.current_user = user
                if user_type == "patient":
                    if user["middleName"] != "":
                        name = f"{user['firstName']} {user['middleName']} {user['lastName']}"
                    else:
                        name = f"{user['firstName']} {user['lastName']}"
                    self.ui.Username_2.setText(name)
                    self.ui.Username_7.setText(name)
                    profile = open(user["profile"], "rb").read()
                    image = QPixmap.fromImage(QImage.fromData(profile))
                    self.ui.userprofile_pic_7.setIcon(image)
                    self.ui.userprofile_pic_2.setIcon(image)
                    self.ui.stackedWidget.setCurrentIndex(3)
                else:
                    if user["middleName"] != "":
                        name = f"{user['firstName']} {user['middleName']} {user['lastName']}"
                    else:
                        name = f"{user['firstName']} {user['lastName']}"
                    self.ui.Username_6.setText(name)
                    self.ui.Username.setText(name)
                    profile = open(user["profile"], "rb").read()
                    image = QPixmap.fromImage(QImage.fromData(profile))
                    self.ui.doctor_setting_button.setIcon(image)
                    self.ui.doctor_setting_button_2.setIcon(image)
                    self.ui.stackedWidget.setCurrentIndex(2)
        else:
            print(reply.errorString())


############################################# CHECK LOGIN SESSION ##########################################################################
  
    def check_session(self):
        url = QUrl("http://localhost:5000/")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, QJsonDocument().toJson())
        reply.finished.connect(self.handle_session_reply)
    
    def handle_session_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            session_data = QJsonDocument.fromJson(data).object()
            if session_data["message"] == "No session found" or session_data["message"] == "Session expired" or session_data["message"] == "admin":
                self.login_page()
            elif session_data["message"] == "patient":
                user = session_data["user_data"]
                self.current_user = user
                if user["middleName"] != "":
                    name = f"{user['firstName']} {user['middleName']} {user['lastName']}"
                else:
                    name = f"{user['firstName']} {user['lastName']}"
                
                profile = open(user["profile"], "rb").read()
                image = QPixmap.fromImage(QImage.fromData(profile))
                self.ui.userprofile_pic_7.setIcon(image)
                self.ui.userprofile_pic_2.setIcon(image)
                self.ui.Username_2.setText(name)
                self.ui.Username_7.setText(name)
                self.ui.stackedWidget.setCurrentIndex(3)
            elif session_data["message"] == "doctor":
                user = session_data["user_data"]
                self.current_user = user
                if user["middleName"] != "":
                    name = f"Dr.{user['firstName']} {user['middleName']} {user['lastName']}"
                else:
                    name = f"Dr.{user['firstName']} {user['lastName']}"
                profile = open(user["profile"], "rb").read()
                image = QPixmap.fromImage(QImage.fromData(profile))
                self.ui.doctor_setting_button.setIcon(image)
                self.ui.doctor_setting_button_2.setIcon(image)
                self.ui.Username_6.setText(name)
                self.ui.Username.setText(name)
                self.ui.stackedWidget.setCurrentIndex(2)
        else:
            print(reply.errorString())

############################################# REDIRECT PAGES ########################################################################

    def switch_to_doctor_home(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_patient_home(self):
        self.ui.stackedWidget.setCurrentIndex(3)
    
    def cancel_add_doctor(self):
        self.ui.stackedWidget.setCurrentIndex(6)  
        
    def switch_to_doctor_patient_list(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.scrollArea.verticalScrollBar().setValue(0)

    def add_patient_page(self):
        self.profile = ""
        self.patient_linedit_clear()
        self.reset_table()
        self.ui.upload_photo.clear()
        self.ui.stackedWidget_2.setCurrentIndex(1) 
        self.ui.scrollArea.verticalScrollBar().setValue(0)

    def login_page(self):
        self.ui.stackedWidget.setCurrentIndex(1)

    def manage_schedule(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.stackedWidget_3.setCurrentIndex(1)
        self.ui.scrollArea_2.verticalScrollBar().setValue(0)
        self.check_sidebars()
        self.display_schedule()


############################################ SIDEBAR HIGHLIGHT #######################################################################          
    
    def check_sidebars(self):
        self.ui.patientListButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.scheduleButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.labButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.reportButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.viewMedRecord_button.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.manageAppointmentButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.billPaymentButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        self.ui.billButton.setStyleSheet("background-color: rgb(39, 86, 193);")
        
        if self.ui.stackedWidget.currentIndex() == 4 and self.ui.stackedWidget_2.currentIndex() == 0:
            self.ui.patientListButton.setStyleSheet("background-color: rgb(144, 194, 255);")
        
        if self.ui.stackedWidget.currentIndex() == 4 and self.ui.stackedWidget_2.currentIndex() == 4:
            self.ui.scheduleButton.setStyleSheet("background-color: rgb(144, 194, 255);")
       
        if self.ui.stackedWidget.currentIndex() == 4 and self.ui.stackedWidget_2.currentIndex() == 2:
            self.ui.labButton.setStyleSheet("background-color: rgb(144, 194, 255);")
       
        if self.ui.stackedWidget.currentIndex() == 4 and self.ui.stackedWidget_2.currentIndex() == 6:
            self.ui.reportButton.setStyleSheet("background-color: rgb(144, 194, 255);")
       
        if self.ui.stackedWidget.currentIndex() == 4 and self.ui.stackedWidget_2.currentIndex() == 13:
            self.ui.billButton.setStyleSheet("background-color: rgb(144, 194, 255);")
        
        if self.ui.stackedWidget.currentIndex() == 5 and self.ui.stackedWidget_3.currentIndex() == 0:
            self.ui.viewMedRecord_button.setStyleSheet("background-color: rgb(144, 194, 255);")
        
        if self.ui.stackedWidget.currentIndex() == 5 and self.ui.stackedWidget_3.currentIndex() == 1:
            self.ui.manageAppointmentButton.setStyleSheet("background-color: rgb(144, 194, 255);")
        
        if self.ui.stackedWidget.currentIndex() == 5 and self.ui.stackedWidget_3.currentIndex() == 3:
            self.ui.billPaymentButton.setStyleSheet("background-color: rgb(144, 194, 255);")

############################################ DOCTOR : Profile Page For Changing Password ######################################

    def profile_page(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(3)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        user = self.current_user
        if user["middleName"] != "":
            name = f"{user['firstName']} {user['middleName']} {user['lastName']}"
        else:
            name = f"{user['firstName']} {user['lastName']}"
        
        profile = open(user["profile"], "rb").read()
        image = QPixmap.fromImage(QImage.fromData(profile))
        self.ui.fullName_profile.setText(name)
        self.ui.speciality_profile.setText(user["speciality"])
        self.ui.doctor_profile_2.setPixmap(image)
        self.ui.doctor_profile_2.setScaledContents(True)
        self.ui.doctor_profile_2.setFixedSize(50, 50)
    
    def profile_change(self):
        url = QUrl("http://localhost:5000/profile_change")
        old_password = self.ui.old_password.text()
        if self.current_user["password"] != old_password:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Old password is incorrect.")
            dialog.exec()
            return
        new_password = self.ui.new_password.text()
        confirm_password = self.ui.confirm_new_password.text()
        if new_password != confirm_password:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Password do not match.")
            dialog.exec()
            return
        
        data = QJsonDocument({
            "username": QJsonValue(self.current_user["userName"]),
            "new_password": QJsonValue(new_password)
        })
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_profile_change_reply)
        
    def handle_profile_change_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Password changed successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Password changed successfully.")
                dialog.exec()
        else:
            print(reply.errorString())
            
    def doctor_linedit_clear(self):
        self.ui.old_password.clear()
        self.ui.new_password.clear()
        self.ui.confirm_new_password.clear()         

############################################ DOCTOR : Display List Of Patients ##########################################################

    def manage_patient_list(self):
        url = QUrl("http://localhost:5000/patient_list")
        request = QNetworkRequest(url)
        
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_patient_list_reply)
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.check_sidebars()
    
    def handle_patient_list_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patient_list = QJsonDocument.fromJson(data).object()
            self.display_patient_list(patient_list["patients"])
        else:
            print(reply.errorString())
    
    def display_patient_list(self, patient_list):
        table = self.ui.patient_list_table
        table.setRowCount(len(patient_list))
        for row, patient in enumerate(patient_list):
            table.setItem(row, 0, QTableWidgetItem(patient["hnNumber"]))
            table.setItem(row, 1, QTableWidgetItem(patient["name"]))

    def search_patient(self):
        search = self.ui.lineEdit_search.text()
        url = QUrl(f"http://localhost:5000/patient_list/{search}")
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_search_patient_reply)

    def handle_search_patient_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patient_list = QJsonDocument.fromJson(data).object()
            self.display_search_patient_list(patient_list["patients"])
        else:
            print(reply.errorString())

    def display_search_patient_list(self, patient_list):
        table = self.ui.patient_list_table
        table.setRowCount(len(patient_list))
        for row, patient in enumerate(patient_list):
            table.setItem(row, 0, QTableWidgetItem(patient["hnNumber"]))
            table.setItem(row, 1, QTableWidgetItem(patient["name"]))

############################################ DOCTOR : Adding New Patient #####################################################################
    
    def create_patient(self):
        profile, firstName, middleName, lastName, hnNumber, birthDate, sex, bloodType, weight, height, passwordID, address, tel, blood_pressure, email = self.get_patient_data()
        vaccines = self.vaccine_list
        medications = self.medication_list
        allergies = self.allergy_list
        profile = self.profile
        medicalInfo = {"vaccines": vaccines, "medications": medications, "allergies": allergies}
        if firstName == "" or lastName == "" or hnNumber == "" or birthDate == "" or sex == "" or bloodType == "" or weight == "" or height == "" or passwordID == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all the required fields.")
            dialog.exec()
            return
        
        if len(weight) > 3 or len(height) > 3 or weight.isnumeric() == False or height.isnumeric() == False:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please enter a valid weight and height.")
            dialog.exec()
            return
        
        if hnNumber.isnumeric() == False:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Invalid HN Number")
            dialog.exec()
            return
        
        if profile == "":
            profile = self.ui.directory.text()
            if profile == "TextLabel":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Please upload a profile picture.")
                dialog.exec()
                return
        
        if blood_pressure[:2].isnumeric() == False or blood_pressure[3] != "/" or blood_pressure[4:6].isnumeric() == False: 
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please enter a valid blood pressure.")
            dialog.exec()
            return

        url = QUrl("http://localhost:5000/create_patient") # api endpoint for creating patient
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "profile": QJsonValue(profile),
            "firstName": QJsonValue(firstName),
            "middleName": QJsonValue(middleName),
            "lastName": QJsonValue(lastName),
            "hnNumber": QJsonValue(hnNumber),
            "birthDate": QJsonValue(birthDate),
            "sex": QJsonValue(sex),
            "bloodType": QJsonValue(bloodType),
            "weight": QJsonValue(weight),
            "height": QJsonValue(height),
            "medicalInfo": QJsonValue(medicalInfo),
            "passwordID": QJsonValue(passwordID),
            "profile": QJsonValue(profile),
            "address": QJsonValue(address),
            "tel": QJsonValue(tel),
            "blood_pressure": QJsonValue(blood_pressure),
            "email": QJsonValue(email)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_create_patient_reply)
    
    def handle_create_patient_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Patient added successfully":
                self.patient_linedit_clear()
                self.reset_table()
                self.profile = ""
                self.manage_patient_list()
                self.ui.stackedWidget_2.setCurrentIndex(0)
                self.ui.scrollArea.verticalScrollBar().setValue(0)
        else:
            print(reply.errorString())

    def get_patient_data(self):  
        profile = self.ui.upload_photo.pixmap()
        firstName = self.ui.firstName_2.text()
        middleName = self.ui.middleName_2.text()
        lastName = self.ui.lastName_2.text()
        hnNumber = self.ui.hn_no.text()
        dob = self.ui.date_of_birth.text()
        sex = self.ui.sex.currentText()
        bloodType = self.ui.blood_type.currentText()
        weight = self.ui.weight.text()
        height = self.ui.height.text()
        passwordID = self.ui.passwordID.text()
        address = self.ui.address.toPlainText()
        tel = self.ui.tel.text()
        blood_pressure = self.ui.blood_pressure.text()
        email = self.ui.patient_email.text()
        return profile, firstName, middleName, lastName, hnNumber, dob, sex, bloodType, weight, height, passwordID, address, tel, blood_pressure, email

    def cancel_add_patient(self):
        url = QUrl("http://localhost:5000/close")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        self.network_manager.get(request)
        self.profile = ""
        self.patient_linedit_clear()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(0)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.reset_table()

############################################ DOCTOR : Profile Picture(upload/capture) For Adding Patient #############################################
 
    def patient_take_picture(self):
        self.camera = Camera(self.ui, "patient")
        self.camera.show()
        
    def patient_finish_upload(self):
        self.patient_display_image()
        self.upload_file_dialog.close()
    
    def patient_display_image(self):
        file = open(self.profile, "rb").read()
        image = QPixmap.fromImage(QImage.fromData(file))
        self.ui.upload_photo.setPixmap(image)
        self.ui.upload_photo.setScaledContents(True)
        self.ui.upload_photo.setFixedSize(100, 100)

    def browse_profile(self):
        self.upload_file_dialog = QDialog()
        self.upload_file_dialog.setWindowTitle("Browse File")
        self.upload_file_dialog.resize(400, 300)
        layout = QVBoxLayout(self.upload_file_dialog)
        file_button = QPushButton("Browse File")
        file_button.clicked.connect(self.image_upload)
        layout.addWidget(file_button)
        self.file_label = QLabel("No file selected")
        layout.addWidget(self.file_label)
        upload_button = QPushButton("Upload File")
        upload_button.clicked.connect(self.patient_finish_upload)
        layout.addWidget(upload_button)
        self.upload_file_dialog.exec() 
    
    def allowed_file(self, filename):
        allowed_extensions = {'png', 'jpg', 'jpeg'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    def image_upload(self):
        fname = QFileDialog.getOpenFileName(self,"Open File", "","All Files(*);;Python Files(*.py)")
        
        if fname:
            pixmap = QPixmap(fname[0])
            self.file_label.setText(str(fname))
            
            self.file_name = fname[0].split("/")[-1]
            if pixmap.isNull():
                self.file_label.setText("No file selected")
            else:
                self.file_label.setPixmap(pixmap)
                self.file_label.setScaledContents(True)
                self.file_label.setFixedSize(100, 100)
                directory = f"upload/{self.file_name}"
                file = QImage(fname[0])
                file.save(directory)
                allowed_file = self.allowed_file(self.file_name)
                if allowed_file:
                    self.profile = directory
                else:
                    dialog = QMessageBox()
                    dialog.setIcon(QMessageBox.Warning)
                    dialog.setWindowTitle("Warning")
                    dialog.setText("Please upload a valid image file.")
                    dialog.exec()

############################################ DOCTOR : Add/Display/Delete Medication For Adding Patient #####################################################################

    def add_medication_page(self):

        self.Medicational_dialog = QDialog(self)
        self.Medicational_dialog.setWindowTitle("Add Medication")
        self.Medicational_dialog.setFixedSize(400, 300)

       
        layout = QVBoxLayout(self.Medicational_dialog)

       
        layout2 = QHBoxLayout()
        layout.addLayout(layout2)
        medication_name_label = QLabel("Medication Name")
        layout2.addWidget(medication_name_label)
        self.medication_name = QLineEdit()
        self.medication_name.setObjectName(u"medication_name")
        self.medication_name.setStyleSheet(u"background-color: white;")
        layout2.addWidget(self.medication_name)

        layout3 = QHBoxLayout()
        layout.addLayout(layout3)
        amount_label = QLabel("Amount")
        layout3.addWidget(amount_label)
        self.amount = QLineEdit()
        self.amount.setObjectName(u"amount")
        self.amount.setStyleSheet(u"background-color: white;")
        layout3.addWidget(self.amount)

        layout4 = QHBoxLayout()
        layout.addLayout(layout4)
        dosage_label = QLabel("Dosage")
        layout4.addWidget(dosage_label)
        self.dosage = QLineEdit()
        self.dosage.setObjectName(u"dosage")
        self.dosage.setStyleSheet(u"background-color: white;")
        layout4.addWidget(self.dosage)

        layout5 = QHBoxLayout()
        layout.addLayout(layout5)
        duration_label = QLabel("Duration")
        layout5.addWidget(duration_label)
        self.duration = QLineEdit()
        self.duration.setObjectName(u"duration")
        self.duration.setStyleSheet(u"background-color: white;")
        layout5.addWidget(self.duration)

        layout6 = QHBoxLayout()
        layout.addLayout(layout6)
        doctor_administered_label = QLabel("Doctor Administered")
        layout6.addWidget(doctor_administered_label)
        self.doctor_administered = QLineEdit()
        self.doctor_administered.setObjectName(u"doctor_administered")
        self.doctor_administered.setStyleSheet(u"background-color: white;")
        layout6.addWidget(self.doctor_administered)

        layout7 = QHBoxLayout()
        layout.addLayout(layout7)
        date_administered_label = QLabel("Date Administered")
        layout7.addWidget(date_administered_label)
        self.date_administered = QDateEdit()
        self.date_administered.setObjectName(u"date_administered")
        self.date_administered.setStyleSheet(u"background-color: white;")
        layout7.addWidget(self.date_administered)

        layout8 = QHBoxLayout()
        layout.addLayout(layout8)
        time_administered_label = QLabel("Time Administered")
        layout8.addWidget(time_administered_label)
        self.time_administered = QTimeEdit()
        self.time_administered.setObjectName(u"time_administered")
        self.time_administered.setStyleSheet(u"background-color: white;")
        layout8.addWidget(self.time_administered)

        layout9 = QHBoxLayout()
        layout.addLayout(layout9)
        sidenote_label = QLabel("Side Note")
        layout9.addWidget(sidenote_label)
        self.sidenote = QLineEdit()
        self.sidenote.setObjectName(u"sidenote")
        self.sidenote.setStyleSheet(u"background-color: white;")
        layout9.addWidget(self.sidenote) 

        confirm_medication_button = QPushButton("Add Medication")
        confirm_medication_button.setObjectName(u"confirm_medication_button")
        confirm_medication_button.setStyleSheet(u"QPushButton#confirm_medication_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_medication_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        confirm_medication_button.clicked.connect(self.add_medication)
        layout.addWidget(confirm_medication_button)
        self.Medicational_dialog.exec()

    def add_medication(self):
        medication_name = self.medication_name.text()
        amount = self.amount.text()
        dosage = self.dosage.text()
        duration = self.duration.text()
        doctor_administered = self.doctor_administered.text()
        date_administered = self.date_administered.text()
        time_administered = self.time_administered.text()
        sidenote = self.sidenote.text()

        if medication_name == "" or amount == "" or dosage == "" or duration == "" or doctor_administered == "" or date_administered == "" or time_administered == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all the required fields.")
            dialog.exec()
            return

        url = QUrl("http://localhost:5000/medication")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "name": QJsonValue(medication_name),
            "amount": QJsonValue(amount),
            "dosage": QJsonValue(dosage),
            "duration": QJsonValue(duration),
            "doctorAdministered": QJsonValue(doctor_administered),
            "dateAdministered": QJsonValue(date_administered),
            "timeAdministered": QJsonValue(time_administered),
            "sideNote": QJsonValue(sidenote)
        })

        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_medication_reply)
    
    def handle_medication_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Medication added successfully":
                self.Medicational_dialog.close()
                self.medication_list = return_message["medication"]
                self.display_medication()
        else:
            print(reply.errorString())
        
    def display_medication(self):
        table = self.ui.medication_list_table
        table.setRowCount(len(self.medication_list))
        for row, medication in enumerate(self.medication_list):
            table.setItem(row, 0, QTableWidgetItem(medication["name"]))
            table.setItem(row, 1, QTableWidgetItem(medication["amount"]))
            table.setItem(row, 2, QTableWidgetItem(medication["dosage"]))
            table.setItem(row, 3, QTableWidgetItem(medication["duration"]))
            table.setItem(row, 4, QTableWidgetItem(medication["doctorAdministered"]))
            table.setItem(row, 5, QTableWidgetItem(medication["dateAdministered"]))
            table.setItem(row, 6, QTableWidgetItem(medication["timeAdministered"]))
            table.setItem(row, 7, QTableWidgetItem(medication["sidenote"]))
            
    def delete_medication(self):
        selected_row = self.ui.medication_list_table.currentRow()
        if selected_row >= 0:
            medication_id = self.medication_list[selected_row]['id']
            url = QUrl(f"http://localhost:5000/medication/{medication_id}")
            request = QNetworkRequest(url)
            reply = self.network_manager.deleteResource(request)
            reply.finished.connect(self.handle_delete_medication_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a medication to delete.")
            dialog.exec()

    def handle_delete_medication_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Medication deleted successfully":
                self.medication_list = return_message["medication"]
                self.display_medication()
        else:
            print(reply.errorString())

############################################ DOCTOR : Add/Display/Delete Allergy For Adding Patient #####################################################################

    def add_allergy_page(self):
        
        self.allergy_dialog = QDialog()
        self.allergy_dialog.setWindowTitle("Add Allergy")
        self.allergy_dialog.setFixedSize(400, 300)
        self.allergy_dialog.setStyleSheet(u"background-color: rgb(240, 249, 255);")
       
        layout = QVBoxLayout()
        self.allergy_dialog.setLayout(layout)
        
        layout2 = QHBoxLayout()
        layout.addLayout(layout2)
        allergy_name_label = QLabel()
        allergy_name_label.setText("Allergy Name")
        layout2.addWidget(allergy_name_label)
        self.allergy_name = QLineEdit()
        self.allergy_name.setPlaceholderText("Allergy Name")
        self.allergy_name.setObjectName(u"allergy_name")
        self.allergy_name.setStyleSheet(u"background-color: white;")
        layout2.addWidget(self.allergy_name)

        verticalSpacer = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer)

        confirm_allergy_button = QPushButton("Add Allergy")
        confirm_allergy_button.setObjectName(u"confirm_allergy_button")
        confirm_allergy_button.setStyleSheet(u"QPushButton#confirm_allergy_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_allergy_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        confirm_allergy_button.clicked.connect(self.add_allergy)
        layout.addWidget(confirm_allergy_button)
        self.allergy_dialog.exec()
        
    def add_allergy(self):
        allergy_name = self.allergy_name.text()
        if allergy_name == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all the required fields.")
            dialog.exec()
            return

        url = QUrl("http://localhost:5000/allergy")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "name": QJsonValue(allergy_name),
        })

        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_allergy_reply)
    
    def handle_allergy_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Allergy added successfully":
                self.allergy_dialog.close()
                self.allergy_list = return_message["allergy"]
                self.display_allergy()
        else:
            print(reply.errorString())
    
    def display_allergy(self):
        table = self.ui.allergy_list_table
        table.setRowCount(len(self.allergy_list))
        for row, allergy in enumerate(self.allergy_list):
            table.setItem(row, 0, QTableWidgetItem(allergy["allergy"]))

    def delete_allergy(self):
        selected_row = self.ui.allergy_list_table.currentRow()
        if selected_row >= 0:
            allergy_id = self.allergy_list[selected_row]['id']
            url = QUrl(f"http://localhost:5000/allergy/{allergy_id}")
            request = QNetworkRequest(url)
            reply = self.network_manager.deleteResource(request)
            reply.finished.connect(self.handle_delete_allergy_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select an allergy to delete.")
            dialog.exec()

    def handle_delete_allergy_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Allergy deleted successfully":
                self.allergy_list = return_message["allergy"]
                self.display_allergy()
        else:
            print(reply.errorString())

############################################ DOCTOR : Add/Display/Delete Vaccine For Adding Patient #####################################################################

    def add_vaccine_page(self):
       
        self.vaccine_dialog = QDialog(self)  
        self.vaccine_dialog.setWindowTitle("Add Vaccine")
        self.vaccine_dialog.resize(300, 200)

        layout = QVBoxLayout(self.vaccine_dialog)

        layout2 = QHBoxLayout()
        layout.addLayout(layout2)  

        layout3 = QHBoxLayout()
        layout.addLayout(layout3)  

        label_vaccine_name = QLabel("Vaccination Name")
        layout2.addWidget(label_vaccine_name)
        self.vaccine_name = QLineEdit()
        self.vaccine_name.setObjectName(u"vaccine_name")
        self.vaccine_name.setStyleSheet(u"background-color: white;")
        layout2.addWidget(self.vaccine_name)

        label_vaccine_date = QLabel("Date Administered")
        layout3.addWidget(label_vaccine_date)
        self.vaccine_date = QDateEdit()
        self.vaccine_date.setObjectName(u"vaccine_date")
        self.vaccine_date.setStyleSheet(u"background-color: white;")
        layout3.addWidget(self.vaccine_date)

        verticalSpacer = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer)

        confirm_vaccine_button = QPushButton("Add Vaccine")
        confirm_vaccine_button.setObjectName(u"confirm_vaccine_button")
        confirm_vaccine_button.clicked.connect(self.add_vaccine)
        confirm_vaccine_button.setStyleSheet(u"QPushButton#confirm_vaccine_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_vaccine_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        layout.addWidget(confirm_vaccine_button)

        self.vaccine_dialog.exec()
        
    def add_vaccine(self):
        vaccine_name = self.vaccine_name.text()
        vaccine_date = self.vaccine_date.text()
        if vaccine_name == "" or vaccine_date == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all the required fields.")
            dialog.exec()
            return

        url = QUrl("http://localhost:5000/vaccine")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "name": QJsonValue(vaccine_name),
            "dateAdministered": QJsonValue(vaccine_date)
        })

        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_vaccine_reply)

    def handle_vaccine_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Vaccine added successfully":
                self.vaccine_dialog.close()
                self.vaccine_list = return_message["vaccine"]
                self.display_vaccine()
        else:
            print(reply.errorString())
            
    def display_vaccine(self):
        table = self.ui.vaccine_list_table
        table.setRowCount(len(self.vaccine_list))
        for row, vaccine in enumerate(self.vaccine_list):
            table.setItem(row, 0, QTableWidgetItem(vaccine["name"]))
            table.setItem(row, 1, QTableWidgetItem(vaccine["dateAdministered"]))

    def delete_vaccine(self):
        selected_row = self.ui.vaccine_list_table.currentRow()
        if selected_row >= 0:
            vaccine_id = self.vaccine_list[selected_row]['id']
            url = QUrl(f"http://localhost:5000/vaccine/{vaccine_id}")
            request = QNetworkRequest(url)
            reply = self.network_manager.deleteResource(request)
            reply.finished.connect(self.handle_delete_vaccine_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a vaccine to delete.")
            dialog.exec()    

    def handle_delete_vaccine_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Vaccine deleted successfully":
                self.vaccine_list = return_message["vaccine"]
                self.display_vaccine()
        else:
            print(reply.errorString())
            
############################################ DOCTOR : Edit Patient Information By Selecting From List Of Patient #####################################################################

    def edit_patient_info(self):
        self.patient_linedit_clear()
        self.reset_table()      
        selected_row = self.ui.patient_list_table.currentRow()
        if selected_row >= 0:
            hnNumber = self.ui.patient_list_table.item(selected_row, 0).text()
            url = QUrl(f"http://localhost:5000/patient_list/{hnNumber}")
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            reply = self.network_manager.post(request, QJsonDocument().toJson())
            reply.finished.connect(self.handle_edit_patient_info_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a patient to edit.")
            dialog.exec()

    def handle_edit_patient_info_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patient_data = QJsonDocument.fromJson(data).object()
            if patient_data:
                self.display_edit_patient_info(patient_data)
            else:
                QMessageBox.warning(self, "Warning", "Patient not found.")
        else:
            QMessageBox.warning(self, "Error", reply.errorString())

    def display_edit_patient_info(self, patient_data):
       
        self.profile = patient_data["profile"]
        file = open(self.profile, "rb").read()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.upload_photo.setPixmap(QPixmap.fromImage(QImage.fromData(file)))
        self.ui.upload_photo.setScaledContents(True)
        self.ui.upload_photo.setFixedSize(100, 100)
        self.ui.firstName_2.setText(patient_data["firstName"])
        self.ui.middleName_2.setText(patient_data["middleName"])
        self.ui.lastName_2.setText(patient_data["lastName"])
        self.ui.hn_no.setText(patient_data["hnNumber"])
        self.ui.date_of_birth.setDate(QDate.fromString(patient_data["dob"], "yyyy-MM-dd"))
        self.ui.sex.setCurrentText(patient_data["sex"])
        self.ui.blood_type.setCurrentText(patient_data["bloodType"])
        self.ui.weight.setText(patient_data["weight"])
        self.ui.height.setText(patient_data["height"])
        self.ui.passwordID.setText(patient_data["passwordID"])
        self.ui.address.setText(patient_data["address"])
        self.ui.tel.setText(patient_data["tel"])
        self.ui.patient_email.setText(patient_data["email"])
        self.ui.blood_pressure.setText(patient_data["blood_pressure"])
        self.vaccine_list = patient_data["vaccines"]
        self.medication_list = patient_data["medications"]
        self.allergy_list = patient_data["allergies"]
        self.display_vaccine()
        self.display_medication()
        self.display_allergy()        

############################################ DOCTOR : Edit Patient Information From Their Profile ###########################################################

    def edit_patient_info_from_profile(self):
        hnNumber = self.ui.patient_hn_no.text()
        url = QUrl(f"http://localhost:5000/patient_list/{hnNumber}")
        request = QNetworkRequest(url)
        reply = self.network_manager.post(request, QJsonDocument().toJson())
        reply.finished.connect(self.handle_edit_patient_info_from_profile_reply)

    def handle_edit_patient_info_from_profile_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patient_info = QJsonDocument.fromJson(data).object()
            self.display_edit_patient_info_from_profile(patient_info)
        else:
            print(reply.errorString())

    def display_edit_patient_info_from_profile(self, patient_info):
        self.profile = patient_info["profile"]
        file = open(self.profile, "rb").read()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(1)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.upload_photo.setPixmap(QPixmap.fromImage(QImage.fromData(file)))
        self.ui.upload_photo.setScaledContents(True)
        self.ui.upload_photo.setFixedSize(100, 100)
        self.ui.firstName_2.setText(patient_info["firstName"])
        self.ui.middleName_2.setText(patient_info["middleName"])
        self.ui.lastName_2.setText(patient_info["lastName"])
        self.ui.hn_no.setText(patient_info["hnNumber"])
        self.ui.date_of_birth.setDate(QDate.fromString(patient_info["dob"], "dd-MM-yyyy"))
        self.ui.sex.setCurrentText(patient_info["sex"])
        self.ui.blood_type.setCurrentText(patient_info["bloodType"])
        self.ui.weight.setText(patient_info["weight"])
        self.ui.height.setText(patient_info["height"])
        self.ui.passwordID.setText(patient_info["passwordID"])
        self.ui.address.setText(patient_info["address"])
        self.ui.tel.setText(patient_info["tel"])
        self.ui.blood_pressure.setText(patient_info["blood_pressure"])
        self.vaccine_list = patient_info["vaccines"]
        self.medication_list = patient_info["medications"]
        self.allergy_list = patient_info["allergies"]
        self.display_vaccine()
        self.display_medication()
        self.display_allergy()

############################################ DOCTOR : Reset A Page #####################################################################

    def closeEvent(self, event):
        url = QUrl("http://localhost:5000/close")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        self.network_manager.get(request)
        event.accept()
    
    def reset_table(self):
        self.vaccine_list = []
        self.medication_list = []
        self.allergy_list = []
        self.other_list = []
        self.display_allergy()
        self.display_medication()
        self.display_vaccine()
        self.display_other()
        url = QUrl("http://localhost:5000/close")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        self.network_manager.get(request)

    def patient_linedit_clear(self):
        self.ui.firstName_2.clear()
        self.ui.middleName_2.clear()
        self.ui.lastName_2.clear()
        self.ui.hn_no.clear()
        self.ui.date_of_birth.clear()
        self.ui.weight.clear()
        self.ui.height.clear()
        self.ui.passwordID.clear()
        self.ui.address.clear()
        self.ui.tel.clear()
        self.ui.blood_pressure.clear()
        self.ui.patient_email.clear()

    def report_linedit_clear(self):
        self.ui.report_summary.clear()

############################################ DOCTOR : Individual Patient Information Viewed #############################################
   
    def view_patient_info(self):
        selected_row = self.ui.patient_list_table.currentRow()
        if selected_row >= 0:
            hnNumber = self.ui.patient_list_table.item(selected_row, 0).text()
            url = QUrl(f"http://localhost:5000/patient_list/{hnNumber}")
            request = QNetworkRequest(url)
            reply = self.network_manager.post(request, QJsonDocument().toJson())
            reply.finished.connect(self.handle_view_patient_info_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a patient to view.")
            dialog.exec()

    def handle_view_patient_info_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patient_info = QJsonDocument.fromJson(data).object()
            self.display_patient_info(patient_info)
        else:
            print(reply.errorString())
            
    def display_patient_info(self, patient_info):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(5)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.patient_photo.setPixmap(QPixmap(patient_info["profile"]))
        self.ui.patient_photo.setScaledContents(True)
        self.ui.patient_photo.setFixedSize(100, 100)
        if patient_info["middleName"] != "":
            name = f"{patient_info['firstName']} {patient_info['middleName']} {patient_info['lastName']}"
        else:
            name = f"{patient_info['firstName']} {patient_info['lastName']}"
        self.ui.patient_name.setText(name)
        self.ui.patient_email_display.setText(patient_info["email"])
        self.ui.patient_hn_no.setText(patient_info["hnNumber"])
        self.ui.patient_dob.setText(patient_info["dob"])
        self.ui.patient_sex.setText(patient_info["sex"])
        
        dob = patient_info["dob"]
        dob_date = datetime.strptime(dob, "%m/%d/%Y")
        current_date = datetime.now()
        if current_date.month < dob_date.month or (current_date.month == dob_date.month and current_date.day < dob_date.day):
            age = current_date.year - dob_date.year - 1
        else:
            age = current_date.year - dob_date.year

        self.ui.patient_age.setText(str(age))
        self.ui.patient_weight.setText(patient_info["weight"])
        self.ui.patient_height.setText(patient_info["height"])
        self.ui.patient_address_2.setText(patient_info["address"])
        self.ui.patient_tel.setText(patient_info["tel"])
        self.ui.patient_blood_type.setText(patient_info["bloodType"])
        self.ui.patient_blood_pressure.setText(patient_info["blood_pressure"])
        blood_pressure = patient_info["blood_pressure"].split("/")
        if int(blood_pressure[0]) > 120 or int(blood_pressure[1]) > 80:
            self.ui.patient_blood_warning.setStyleSheet("color: red;")
            self.ui.patient_blood_warning.setText("You have high blood pressure")
        elif int(blood_pressure[0]) < 90 or int(blood_pressure[1]) < 60:
            self.ui.patient_blood_warning.setStyleSheet("color: red;")
            self.ui.patient_blood_warning.setText("You have low blood pressure")
        else:
            self.ui.patient_blood_warning.setStyleSheet("color: green;")
            self.ui.patient_blood_warning.setText("Normal blood pressure")
        
        self.vaccine_list = patient_info["vaccines"]
        self.medication_list = patient_info["medications"]
        self.allergy_list = patient_info["allergies"]
        self.labtest_list = patient_info["lab_tests"]
        self.display_patient_vaccine()
        self.display_patient_medication()
        self.display_patient_allergy()
        self.display_patient_labtest()

    def display_patient_vaccine(self):
        table = self.ui.vaccine_list_table_2
        table.setRowCount(len(self.vaccine_list))
        for row, vaccine in enumerate(self.vaccine_list):
            table.setItem(row, 0, QTableWidgetItem(vaccine["name"]))
            table.setItem(row, 1, QTableWidgetItem(vaccine["dateAdministered"]))

    def display_patient_medication(self):
        table = self.ui.medication_list_table_2
        table.setRowCount(len(self.medication_list))
        for row, medication in enumerate(self.medication_list):
            table.setItem(row, 0, QTableWidgetItem(medication["name"]))
            table.setItem(row, 1, QTableWidgetItem(medication["amount"]))
            table.setItem(row, 2, QTableWidgetItem(medication["dosage"]))
            table.setItem(row, 3, QTableWidgetItem(medication["duration"]))
            table.setItem(row, 4, QTableWidgetItem(medication["doctorAdministered"]))
            table.setItem(row, 5, QTableWidgetItem(medication["dateAdministered"]))
            table.setItem(row, 6, QTableWidgetItem(medication["timeAdministered"]))
            table.setItem(row, 7, QTableWidgetItem(medication["sidenote"]))
                          
    def display_patient_allergy(self):
        table = self.ui.allergy_list_table_2
        table.setRowCount(len(self.allergy_list))
        for row, allergy in enumerate(self.allergy_list):
            table.setItem(row, 0, QTableWidgetItem(allergy["allergy"]))

    def display_patient_labtest(self):
        table = self.ui.lab_test_list_table_2
        table.setRowCount(len(self.labtest_list))
        for row, labtest in enumerate(self.labtest_list):
            labresult = labtest["reply"]
            if labresult == None:
                status = "Pending"
            elif labresult["notes"] == None and labresult["file"] == None:
                status = "Rejected"
            else:
                status = "Completed"
            table.setItem(row, 0, QTableWidgetItem(labtest["labType"]))
            table.setItem(row, 1, QTableWidgetItem(labtest["requesting_doctor"]))
            table.setItem(row, 2, QTableWidgetItem(status))
            table.setItem(row, 3, QTableWidgetItem(labtest["date"]))
            table.setItem(row, 4, QTableWidgetItem(labtest["time"]))
        
############################################ DOCTOR : Lab Request Page #####################################################################

    def get_lab_request(self):
        url = QUrl("http://localhost:5000/get_lab_requests")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        data = QJsonDocument({
            "department": QJsonValue(self.current_user["speciality"])
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_get_lab_request_reply)
    
    def handle_get_lab_request_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            lab_request_data = QJsonDocument.fromJson(data).object()
            self.lab_request_list = lab_request_data["lab_requests"]
            self.lab_request_page()
        else:
            print(reply.errorString())
    
    def lab_request_page(self):
        table = self.ui.lab_requests_table
        table.setRowCount(len(self.lab_request_list))
        for row, lab_request in enumerate(self.lab_request_list):
            table.setItem(row, 0, QTableWidgetItem(lab_request["urgency"]))
            table.setItem(row, 1, QTableWidgetItem(lab_request["requestType"]))
            table.setItem(row, 2, QTableWidgetItem(lab_request["patientName"]))
            table.setItem(row, 3, QTableWidgetItem(lab_request["hnNumber"]))
            table.setItem(row, 4, QTableWidgetItem(lab_request["doctorName"]))
            table.setItem(row, 5, QTableWidgetItem(lab_request["date"]))
            table.setItem(row, 6, QTableWidgetItem(lab_request["time"]))
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(2)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.check_sidebars()
    
    def get_department(self):
        url = QUrl("http://localhost:5000/department")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_department_reply)
        
    def handle_department_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            department_data = QJsonDocument.fromJson(data).object()
            self.ui.faculty.clear()
            for department in department_data["department"]:
                self.ui.faculty.addItem(department)
                self.make_lab_request_page()
        else:
            print(reply.errorString())
        
    def make_lab_request_page(self):
        self.clear_lab_request()
        date = datetime.now().strftime("%Y-%m-%d")
        time = datetime.now().strftime("%H:%M:%S")
        self.ui.dat_request_2.setText("Time Requested: " + time)
        self.ui.date_request.setText("Date Requested: " + date)
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(8)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
    
    def make_lab_request(self):
        url = QUrl("http://localhost:5000/lab_request")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        date = self.ui.date_request.text()
        time = self.ui.dat_request_2.text()
        requestType = self.ui.case_type.currentText()
        urgency = self.ui.urgency.currentText()
        faculty = self.ui.faculty.currentText()
        hnNumber = self.ui.lab_request_hn_no.text()
        patientName = self.ui.lab_request_patient_name.text()
        reason = self.ui.reason.toPlainText()
        if self.current_user["middleName"] != "":
            doctorName = f"Dr.{self.current_user['firstName']} {self.current_user['middleName']} {self.current_user['lastName']}"
        else:
            doctorName = f"Dr.{self.current_user['firstName']} {self.current_user['lastName']}"
            
        if hnNumber == "" or patientName == "" or reason == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all the required fields.")
            dialog.exec()
            return
            
        data = QJsonDocument({
            "date": QJsonValue(date),
            "time": QJsonValue(time),
            "requestType": QJsonValue(requestType),
            "urgency": QJsonValue(urgency),
            "faculty": QJsonValue(faculty),
            "hnNumber": QJsonValue(hnNumber),
            "patientName": QJsonValue(patientName),
            "doctorName": QJsonValue(doctorName),
            "reason": QJsonValue(reason)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_lab_request_reply)
    
    def handle_lab_request_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Lab request added successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Lab request added successfully.")
                dialog.exec()
                self.get_lab_request()
        else:
            print(reply.errorString())
            
    def cancel_lab_request(self):
        self.clear_lab_request()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(2)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        
    def clear_lab_request(self):
        self.ui.lab_request_hn_no.clear()
        self.ui.lab_request_patient_name.clear()
        self.ui.case_type.setCurrentIndex(0)
        self.ui.urgency.setCurrentIndex(0)
        self.ui.faculty.setCurrentIndex(0)
        self.ui.reason.clear()

############################################ DOCTOR : Lab Reply Page #####################################################################
        
    def lab_reply_page(self):
        self.clear_lab_reply()
        selected_row = self.ui.lab_requests_table.currentRow()
        if selected_row >= 0:
            hnNumber = self.ui.lab_requests_table.item(selected_row, 3).text()
            date = self.ui.lab_requests_table.item(selected_row, 5).text() 
            time = self.ui.lab_requests_table.item(selected_row, 6).text()
            url = QUrl(f"http://localhost:5000/lab_reply/{hnNumber}/{date}/{time}")
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            reply = self.network_manager.post(request, QJsonDocument().toJson())
            reply.finished.connect(self.handle_lab_reply_reply)
    
    def handle_lab_reply_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            lab_reply_data = QJsonDocument.fromJson(data).object()
            self.lab_reply_list = lab_reply_data["lab_request"]
            self.ui.dat_request_3.setText("Time Requested: " + self.lab_reply_list["time"])
            self.ui.date_request_2.setText("Date Requested: " + self.lab_reply_list["date"])
            self.ui.case_type_2.setText(self.lab_reply_list["requestType"])
            self.ui.urgency_2.setText(self.lab_reply_list["urgency"])
            self.ui.faculty_2.setText(self.lab_reply_list["faculty"])
            self.ui.lab_request_hn_no_2.setText(self.lab_reply_list["hnNumber"])
            self.ui.lab_request_patient_name_2.setText(self.lab_reply_list["patientName"])
            self.ui.reason_2.setText(self.lab_reply_list["reason"])
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.stackedWidget_2.setCurrentIndex(9)
            self.ui.scrollArea.verticalScrollBar().setValue(0)
        else:
            print(reply.errorString())
    
    def allowed_file_2(self, filename):
        allowed_extensions = {'png', 'jpg', 'jpeg', 'pdf'}
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_extensions

    def file_upload(self):
        fname = QFileDialog.getOpenFileName(self,"Open File", "","All Files(*);;Python Files(*.py)")
        
        if fname:
            self.ui.display_file_name.setText(str(fname[0]))
            self.file_name = fname[0].split("/")[-1]
            directory = f"upload/labs/{self.file_name}"

            allowed_file = self.allowed_file_2(self.file_name)
            if allowed_file:
                shutil.copy(fname[0], directory)
                self.file = directory
            else:
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Please upload a valid file.")
                dialog.exec()

    def submit_lab_reply(self):
        url = QUrl("http://localhost:5000/make_lab_reply")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        note = self.ui.note_2.toPlainText()
        file = self.file
        hnNumber = self.ui.lab_request_hn_no_2.text()
        date = self.ui.date_request_2.text().split(": ")[-1]
        time = self.ui.dat_request_3.text().split(": ")[-1]
        
        if note == "":
            if file == "":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Please fill in all the required fields.")
                dialog.exec()
                return
            
        data = QJsonDocument({
            "note": QJsonValue(note),
            "file": QJsonValue(file),
            "hnNumber": QJsonValue(hnNumber),
            "date": QJsonValue(date),
            "time": QJsonValue(time)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_submit_lab_reply_reply)
    
    def handle_submit_lab_reply_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Lab reply added successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Lab reply added successfully.")
                dialog.exec()
                self.get_lab_request()
        else:
            print(reply.errorString())
            
    def cancel_lab_reply(self):
        self.get_lab_request()
        
    def clear_lab_reply(self):
        self.ui.note_2.clear()
        self.ui.display_file_name.clear()   
        if self.file != "":
            os.remove(self.file) 
        self.file = ""
        
    def reject_lab_request(self):
        url = QUrl("http://localhost:5000/reject_lab_request")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        hnNumber = self.ui.lab_request_hn_no_2.text()
        date = self.ui.date_request_2.text().split(": ")[-1]
        time = self.ui.dat_request_3.text().split(": ")[-1]
        
        data = QJsonDocument({
            "hnNumber": QJsonValue(hnNumber),
            "date": QJsonValue(date),
            "time": QJsonValue(time)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_reject_lab_request_reply)
        
    def handle_reject_lab_request_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Lab request rejected successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Lab request rejected.")
                dialog.exec()
                self.get_lab_request()
        else:
            print(reply.errorString())
            
############################################ DOCTOR : View Individual Lab Reply #####################################################################
            
    def view_received_replies(self):
        url = QUrl("http://localhost:5000/view_received_replies")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        if self.current_user["middleName"] != "":
            doctorName = f"Dr.{self.current_user['firstName']} {self.current_user['middleName']} {self.current_user['lastName']}"
        else:
            doctorName = f"Dr.{self.current_user['firstName']} {self.current_user['lastName']}"
        data = QJsonDocument({
            "name": QJsonValue(doctorName)
        })
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_view_received_replies_reply)
    
    def handle_view_received_replies_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            lab_reply_data = QJsonDocument.fromJson(data).object()
            lab_reply_list = lab_reply_data["lab_replies"]
            self.view_lab_reply_page(lab_reply_list)
        else:
            print(reply.errorString())
    
    def view_lab_reply_page(self, lab_reply_list):
        table = self.ui.lab_requests_table_2
        table.setRowCount(len(lab_reply_list))
        for row, lab_reply in enumerate(lab_reply_list):
            table.setItem(row, 0, QTableWidgetItem(lab_reply["requestType"]))
            table.setItem(row, 1, QTableWidgetItem(lab_reply["hnNumber"]))
            table.setItem(row, 2, QTableWidgetItem(lab_reply["patientName"]))
            table.setItem(row, 3, QTableWidgetItem(lab_reply["date"]))
            table.setItem(row, 4, QTableWidgetItem(lab_reply["time"]))
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(10)
        self.ui.scrollArea.verticalScrollBar().setValue(0)

    def back_from_view_lab_reply(self):
        self.get_lab_request()

    def view_lab_reply(self):
        selected_row = self.ui.lab_requests_table_2.currentRow()
        if selected_row >= 0:
            hnNumber = self.ui.lab_requests_table_2.item(selected_row, 1).text()
            date = self.ui.lab_requests_table_2.item(selected_row, 3).text()
            time = self.ui.lab_requests_table_2.item(selected_row, 4).text()
            url = QUrl(f"http://localhost:5000/view_lab_reply/{hnNumber}/{date}/{time}")
            request = QNetworkRequest(url)
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            reply = self.network_manager.post(request, QJsonDocument().toJson())
            reply.finished.connect(self.handle_view_lab_reply_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a lab reply to view.")
            dialog.exec()

    def handle_view_lab_reply_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            lab_reply_data = QJsonDocument.fromJson(data).object()
            self.lab_reply_data = lab_reply_data["lab_reply"]
            self.display_lab_reply()
        else:
            print(reply.errorString())

    def display_lab_reply(self):
        if self.lab_reply_data["file"] == None and self.lab_reply_data["note"] == None:
            self.ui.dat_request_6.setText("Time Requested: " + self.lab_reply_data["time"])
            self.ui.date_request_5.setText("Date Requested: " + self.lab_reply_data["date"])
            self.ui.case_type_5.setText(self.lab_reply_data["requestType"])
            self.ui.lab_request_hn_no_5.setText(self.lab_reply_data["hnNumber"])
            self.ui.lab_request_patient_name_5.setText(self.lab_reply_data["patientName"])
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.stackedWidget_2.setCurrentIndex(12)
            self.ui.scrollArea.verticalScrollBar().setValue(0)
        else:
            self.ui.dat_request_4.setText("Time Requested: " + self.lab_reply_data["time"])
            self.ui.date_request_3.setText("Date Requested: " + self.lab_reply_data["date"])
            self.ui.case_type_3.setText(self.lab_reply_data["requestType"])
            self.ui.lab_request_hn_no_3.setText(self.lab_reply_data["hnNumber"])
            self.ui.lab_request_patient_name_3.setText(self.lab_reply_data["patientName"])
            self.ui.textEdit.setText(self.lab_reply_data["note"])
            if self.lab_reply_data["file"] == None:
                self.ui.label_90.setText("No file uploaded.")
                self.ui.download_button.setEnabled(False)
            else:
                self.ui.label_91.setText(self.lab_reply_data["file"])
            self.ui.download_button.clicked.connect(self.download_lab_reply)
            self.ui.stackedWidget.setCurrentIndex(4)
            self.ui.stackedWidget_2.setCurrentIndex(11)
            self.ui.scrollArea.verticalScrollBar().setValue(0)

    def download_lab_reply(self):
        file = self.lab_reply_data["file"]
        filename = file.split("/")[-1]
        dialog = QFileDialog()
        dialog.setFileMode(QFileDialog.AnyFile)
        dialog.setAcceptMode(QFileDialog.AcceptSave)
        dialog.setDirectory("download")
        dialog.selectFile(filename)
        if dialog.exec_():
            path = dialog.selectedFiles()[0]
            shutil.copy(file, path)

############################################ DOCTOR : List Of Patient Reports #####################################################################

    def view_patients_report(self):
        url = QUrl("http://localhost:5000/patient_report")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_patients_report_reply)

    def handle_patients_report_reply(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(6)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.check_sidebars()
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patients_report = QJsonDocument.fromJson(data).object()
            self.display_patients_report(patients_report["patients"])
        else:
            print(reply.errorString())
        
    def display_patients_report(self, patients_report):
        table = self.ui.report_patient_table
        table.setRowCount(len(patients_report))
        for row, patient in enumerate(patients_report):
            table.setItem(row, 0, QTableWidgetItem(patient["hnNumber"]))
            table.setItem(row, 1, QTableWidgetItem(patient["name"]))


############################################ DOCTOR : View Individual Report Page #########################################################################

    def get_lab_test_list(self):
        url = QUrl("http://localhost:5000/lab_test_list")
        request = QNetworkRequest(url)
        date = datetime.now().strftime("%Y-%m-%d")
        data = QJsonDocument({
            "hnNumber": QJsonValue(self.reportRowHnNumber),
            "date": QJsonValue(date)
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_get_lab_test_list_reply)
    
    def handle_get_lab_test_list_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            lab_test_list = QJsonDocument.fromJson(data).object()
            self.lab_test_list = lab_test_list["lab_tests"]
            self.diplay_report_lab_test()
        else:
            print(reply.errorString())

    def report_page(self):
        selected_row = self.ui.report_patient_table.currentRow()
        if selected_row >= 0:
            self.reportRowHnNumber = self.ui.report_patient_table.item(selected_row, 0).text()
            hnNumber = self.reportRowHnNumber
            url = QUrl(f"http://localhost:5000/patient_report/{hnNumber}")
            request = QNetworkRequest(url)
            reply = self.network_manager.get(request)
            reply.finished.connect(self.handle_report_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a patient to write a report.")
            dialog.exec()

    def handle_report_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            patient_report = QJsonDocument.fromJson(data).object()
            self.display_report(patient_report)
        else:
            print(reply.errorString())

    def display_report(self, patient_report):
        self.clear_report()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(7)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.report_hn_no.setText(patient_report["hnNumber"])
        if patient_report["middleName"] != "":
            name = f"{patient_report['firstName']} {patient_report['middleName']} {patient_report['lastName']}"
        else:
            name = f"{patient_report['firstName']} {patient_report['lastName']}"
        self.ui.report_patient_name.setText(name)
        current_date = datetime.now()
        self.ui.report_date.setText("Date: " + current_date.strftime("%d/%m/%Y"))
        self.vaccine_list = patient_report["vaccines"]
        self.medication_list = patient_report["medications"]
        if patient_report["message"] == "No report found":
            self.display_report_vaccine()
            self.display_report_medication()
            self.get_lab_test_list()
        else:
            self.ui.report_summary.setPlainText(patient_report["summary"])
            self.lab_test_list = patient_report["lab_tests"]
            self.other_list = patient_report["others"]
            self.display_draft_report_vaccine()
            self.display_draft_report_medication()
            self.display_draft_report_lab_test()
            self.display_draft_report_other()
            
    def display_report_vaccine(self):
        table = self.ui.report_vaccine_table
        table.setRowCount(len(self.vaccine_list))
        for row, vaccine in enumerate(self.vaccine_list):
            table.setItem(row, 0, QTableWidgetItem(vaccine["name"]))

    def display_draft_report_vaccine(self):
        table = self.ui.report_vaccine_table
        table.setRowCount(len(self.vaccine_list))
        for row, vaccine in enumerate(self.vaccine_list):
            table.setItem(row, 0, QTableWidgetItem(vaccine["name"]))
            table.setItem(row, 1, QTableWidgetItem(vaccine["price"]))

    def display_report_medication(self):
        table = self.ui.report_medication_table
        table.setRowCount(len(self.medication_list))
        for row, medication in enumerate(self.medication_list):
            table.setItem(row, 0, QTableWidgetItem(medication["name"]))
            table.setItem(row, 1, QTableWidgetItem(medication["amount"]))
            table.setItem(row, 2, QTableWidgetItem(medication["dosage"]))
            table.setItem(row, 3, QTableWidgetItem(medication["duration"]))
            table.setItem(row, 4, QTableWidgetItem(medication["doctorAdministered"]))

    def display_draft_report_medication(self):
        table = self.ui.report_medication_table
        table.setRowCount(len(self.medication_list))
        for row, medication in enumerate(self.medication_list):
            table.setItem(row, 0, QTableWidgetItem(medication["name"]))
            table.setItem(row, 1, QTableWidgetItem(medication["amount"]))
            table.setItem(row, 2, QTableWidgetItem(medication["dosage"]))
            table.setItem(row, 3, QTableWidgetItem(medication["duration"]))
            table.setItem(row, 4, QTableWidgetItem(medication["doctorAdministered"]))
            table.setItem(row, 5, QTableWidgetItem(medication["price"]))

    def diplay_report_lab_test(self):
        table = self.ui.report_lab_test_table
        table.setRowCount(len(self.lab_test_list))
        for row, lab_test in enumerate(self.lab_test_list):
            table.setItem(row, 0, QTableWidgetItem(lab_test["labType"]))

    def display_draft_report_lab_test(self):
        table = self.ui.report_lab_test_table
        table.setRowCount(len(self.lab_test_list))
        for row, lab_test in enumerate(self.lab_test_list):
            table.setItem(row, 0, QTableWidgetItem(lab_test["labType"]))
            table.setItem(row, 1, QTableWidgetItem(lab_test["price"]))

    def display_draft_report_other(self):
        table = self.ui.report_other_table
        table.setRowCount(len(self.other_list))
        for row, other in enumerate(self.other_list):
            table.setItem(row, 0, QTableWidgetItem(other["name"]))
            table.setItem(row, 1, QTableWidgetItem(other["price"]))
         
    def cancel_report(self):
        url = QUrl("http://localhost:5000/close")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        self.network_manager.get(request)
        self.report_linedit_clear()
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(6)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.reset_table()

    def clear_report(self):
        self.ui.report_summary.clear()
        self.ui.report_vaccine_table.clearContents()
        self.ui.report_medication_table.clearContents()
        self.ui.report_lab_test_table.clearContents()
        self.ui.report_other_table.clearContents()

############################################ DOCTOR : Add/Display/Delete Other for Adding Patient Report #########################################################################
    def add_other_dialog(self):
        self.other_dialog = QDialog(self)
        self.other_dialog.setWindowTitle("Add Other")
        self.other_dialog.resize(300, 200)

        layout = QVBoxLayout(self.other_dialog)

        layout2 = QHBoxLayout()
        layout.addLayout(layout2)

        label_other = QLabel("Other")
        layout2.addWidget(label_other)
        self.other = QLineEdit()
        self.other.setObjectName(u"other")
        self.other.setStyleSheet(u"background-color: white;")
        layout2.addWidget(self.other)

        layout3 = QHBoxLayout()
        layout.addLayout(layout3)
        label_other_price = QLabel("Price")
        layout3.addWidget(label_other_price)
        self.other_price = QLineEdit()
        self.other_price.setObjectName(u"other_price")
        self.other_price.setStyleSheet(u"background-color: white;")
        layout3.addWidget(self.other_price)


        verticalSpacer = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer)

        confirm_other_button = QPushButton("Add Other")
        confirm_other_button.setObjectName(u"confirm_other_button")
        confirm_other_button.clicked.connect(self.add_other)
        confirm_other_button.setStyleSheet(u"QPushButton#confirm_other_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_other_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        layout.addWidget(confirm_other_button)
        self.other_dialog.exec()

    def add_other(self):
        other_name = self.other.text()
        other_price = self.other_price.text()
        if other_name == "" or other_price == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all fields.")
            dialog.exec()
            return
        
        url = QUrl("http://localhost:5000/other")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "name": QJsonValue(other_name),
            "price": QJsonValue(other_price)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_add_other_reply)

    def handle_add_other_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Other added successfully":
                self.other_dialog.close()
                self.other_list = return_message["other"]
                self.display_other()
        else:
            print(reply.errorString())

    def display_other(self):
        table = self.ui.report_other_table
        table.setRowCount(len(self.other_list))
        for row, other in enumerate(self.other_list):
            table.setItem(row, 0, QTableWidgetItem(other["name"]))
            table.setItem(row, 1, QTableWidgetItem(other["price"]))

    def delete_other(self):
        selected_row = self.ui.report_other_table.currentRow()
        if selected_row >= 0:
            other_id = self.other_list[selected_row]['id']
            url = QUrl(f"http://localhost:5000/other/{other_id}")
            request = QNetworkRequest(url)
            reply = self.network_manager.deleteResource(request)
            reply.finished.connect(self.handle_delete_other_reply)
        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select an other to delete.")
            dialog.exec()

    def handle_delete_other_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Other deleted successfully":
                self.other_list = return_message["other"]
                self.display_other()
        else:
            print(reply.errorString())

############################################ DOCTOR : Draft Report #########################################################################

    def draft_report(self): 
       
        url = QUrl("http://localhost:5000/draft_report")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        vaccine_table = self.ui.report_vaccine_table
        vaccine_prices = []
        for row in range(vaccine_table.rowCount()):
            for vaccine in self.vaccine_list:
               if vaccine["name"] == vaccine_table.item(row, 0).text():
                    vaccine_price = {}
                    vaccine_price["name"] = vaccine_table.item(row, 0).text()
                    vaccine_price["price"] = vaccine_table.item(row, 1).text()
                    vaccine_prices.append(vaccine_price)
            self.vaccine_list.append(vaccine)
            
        medication_table = self.ui.report_medication_table
        medication_prices = []
        for row in range(medication_table.rowCount()):
            for medication in self.medication_list:
                if medication["name"] == medication_table.item(row, 0).text():
                    medication_price = {}
                    medication_price["name"] = medication_table.item(row, 0).text()
                    medication_price["amount"] = medication_table.item(row, 1).text()
                    medication_price["dosage"] = medication_table.item(row, 2).text()
                    medication_price["duration"] = medication_table.item(row, 3).text()
                    medication_price["doctorAdministered"] = medication_table.item(row, 4).text()
                    medication_price["price"] = medication_table.item(row, 5).text()
                    medication_prices.append(medication_price)

        self.get_lab_test_list()
        lab_test_prices = self.get_lab_test_price()
        
        vaccine_prices_list = {"vaccine": vaccine_prices}
        medication_prices_list = {"medication": medication_prices}
        lab_test_prices_list = {"lab_test": lab_test_prices}
        
        summary = self.ui.report_summary.toPlainText()
        
        other = {"other": self.other_list}
        data = QJsonDocument({
            "hnNumber": QJsonValue(self.ui.report_hn_no.text()),
            "summary": QJsonValue(summary),
            "price_vaccine": QJsonValue(vaccine_prices_list),
            "price_medication": QJsonValue(medication_prices_list),
            "price_lab_tests": QJsonValue(lab_test_prices_list),
            "other": QJsonValue(other)
        })
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_draft_report_reply)
    
    def handle_draft_report_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            draft_report = QJsonDocument.fromJson(data).object()
            if draft_report["message"] == "Report drafted successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Report drafted successfully.")
                dialog.exec()
                self.clear_report()
                self.ui.stackedWidget.setCurrentIndex(4)
                self.ui.stackedWidget_2.setCurrentIndex(6)
                self.ui.scrollArea.verticalScrollBar().setValue(0)
                self.reset_table()
        else:
            print(reply.errorString())

    def get_lab_test_price(self):
        lab_test_table = self.ui.report_lab_test_table
        lab_test_prices = []
        for row in range(lab_test_table.rowCount()):
            for lab_test in self.lab_test_list:
                if lab_test["labType"] == lab_test_table.item(row, 0).text():
                    lab_test_price = {}
                    lab_test_price["labType"] = lab_test_table.item(row, 0).text()
                    lab_test_price["price"] = lab_test_table.item(row, 1).text()
                    lab_test_prices.append(lab_test_price)
        return lab_test_prices

############################################ DOCTOR : Confirm Report #########################################################################

    def confirm_report(self):
        url = QUrl("http://localhost:5000/confirm_report")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        vaccine_table = self.ui.report_vaccine_table
        vaccine_prices = []
        for row in range(vaccine_table.rowCount()):
            for vaccine in self.vaccine_list:
               if vaccine["name"] == vaccine_table.item(row, 0).text():
                    vaccine_price = {}
                    vaccine_price["name"] = vaccine_table.item(row, 0).text()
                    vaccine_price["price"] = vaccine_table.item(row, 1).text()
                    vaccine_prices.append(vaccine_price)
            self.vaccine_list.append(vaccine)
            
        medication_table = self.ui.report_medication_table
        medication_prices = []
        for row in range(medication_table.rowCount()):
            for medication in self.medication_list:
                if medication["name"] == medication_table.item(row, 0).text():
                    medication_price = {}
                    medication_price["name"] = medication_table.item(row, 0).text()
                    medication_price["amount"] = medication_table.item(row, 1).text()
                    medication_price["dosage"] = medication_table.item(row, 2).text()
                    medication_price["duration"] = medication_table.item(row, 3).text()
                    medication_price["doctorAdministered"] = medication_table.item(row, 4).text()
                    medication_price["price"] = medication_table.item(row, 5).text()
                    medication_prices.append(medication_price)

        lab_test_prices = self.get_lab_test_price()
        
        vaccine_prices_list = {"vaccine": vaccine_prices}
        medication_prices_list = {"medication": medication_prices}
        lab_test_prices_list = {"lab_test": lab_test_prices}
        
        summary = self.ui.report_summary.toPlainText()
        
        other = {"other": self.other_list}
        
        date = self.ui.report_date.text()
        
        data = QJsonDocument({
            "hnNumber": QJsonValue(self.ui.report_hn_no.text()),
            "summary": QJsonValue(summary),
            "price_vaccine": QJsonValue(vaccine_prices_list),
            "price_medication": QJsonValue(medication_prices_list),
            "price_lab_tests": QJsonValue(lab_test_prices_list),
            "date": QJsonValue(date),
            "other": QJsonValue(other)
        })
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_confirm_report_reply)

    def handle_confirm_report_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            confirm_report = QJsonDocument.fromJson(data).object()
            if confirm_report["message"] == "Bill confirmed successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Bill confirmed successfully")
                dialog.exec()
                self.clear_report()
                self.ui.stackedWidget.setCurrentIndex(4)
                self.ui.stackedWidget_2.setCurrentIndex(6)
                self.ui.scrollArea.verticalScrollBar().setValue(0)
                self.reset_table()
        else:
            print(reply.errorString())
      
############################################ DOCTOR : Reset Report At The Start Of A New Day #####################################################################

    def reset_report(self):
        url = QUrl("http://localhost:5000/reset_report")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_reset_report_reply)
            
    def handle_reset_report_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Report reset successfully":
                return
        print(reply.errorString())

############################################ DOCTOR : List Of Bills #####################################################################

    def doctor_view_bill_list(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(13)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.check_sidebars()
        self.display_bill_list_for_doctor()
        pass

    def display_bill_list_for_doctor(self):
        url = QUrl("http://localhost:5000/doctor_get_bills")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_display_bill_list_for_doctor_reply)

    def handle_display_bill_list_for_doctor_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            bills = QJsonDocument.fromJson(data).object()
            self.display_bill_list_table_for_doctor(bills["bills"])
        else:
            print(reply.errorString())

    def display_bill_list_table_for_doctor(self, bills):
        table = self.ui.doctor_bill_list_table
        table.setRowCount(len(bills))
        for row, bill in enumerate(bills):
            table.setItem(row, 0, QTableWidgetItem(str(bill["patientName"]))),
            table.setItem(row, 1, QTableWidgetItem(str(bill["hnNumber"]))),
            table.setItem(row, 2, QTableWidgetItem(str(bill["id"]))),
            table.setItem(row, 3, QTableWidgetItem(str(bill["date"]))),
            table.setItem(row, 4, QTableWidgetItem(str(bill["totalPrice"]))),
            table.setItem(row, 5, QTableWidgetItem(str(bill["status"])))
            
############################################ DOCTOR : View Individual Bill #########################################################################

    def doctor_view_bill(self):
        selected_row = self.ui.doctor_bill_list_table.currentRow()
        if selected_row >= 0:
            url = QUrl("http://localhost:5000/view_bill")
            request = QNetworkRequest(url)
            data = QJsonDocument({
                "bill_id": QJsonValue(self.ui.doctor_bill_list_table.item(selected_row, 2).text())
            })
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            reply = self.network_manager.post(request, data.toJson())
            reply.finished.connect(self.handle_doctor_view_bill_reply)

        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a bill to view.")
            dialog.exec()

    def handle_doctor_view_bill_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            bill = QJsonDocument.fromJson(data).object()
            self.doctor_view_bill_page(bill["bill"])
        else:
            print(reply.errorString())

    def doctor_view_bill_page(self, bill):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(14)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.ui.bill_number_2.setText(str(bill["id"]))
        self.ui.bill_date_2.setText(bill["date"])
        self.ui.bill_patient_name_2.setText(bill["patientName"])
        self.ui.bill_patient_hn_no_2.setText(bill["hnNumber"])
        self.ui.bill_total_charge_2.setText(str(bill["totalPrice"]))
        self.ui.bill_status_2.setText(bill["status"])
        table = self.ui.bill_table_2
        table.setRowCount(len(bill["items"]))
        for row, item in enumerate(bill["items"]):
            table.setItem(row, 0, QTableWidgetItem(item["name"]))
            table.setItem(row, 1, QTableWidgetItem(item["price"]))
        
    def display_bill_payment_table(self, bill):
        table = self.ui.bill_list_table
        table.setRowCount(len(bill))
        for row, bill in enumerate(bill):
            table.setItem(row, 0, QTableWidgetItem(str(bill["id"])))
            table.setItem(row, 1, QTableWidgetItem(bill["date"]))
            table.setItem(row, 2, QTableWidgetItem(str(bill["totalPrice"])))
            table.setItem(row, 3, QTableWidgetItem(bill["status"]))
       
    def change_status(self):
        url = QUrl("http://localhost:5000/change_status")
        request = QNetworkRequest(url)
        data = QJsonDocument({
            "bill_id": QJsonValue(self.ui.bill_number_2.text())
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_change_status_reply)
    
    def handle_change_status_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            bill = QJsonDocument.fromJson(data).object()
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Information)
            dialog.setWindowTitle("Success")
            dialog.setText("Bill status changed successfully.")
            dialog.exec()
            self.doctor_view_bill_page(bill["bill"])
        else:
            print(reply.errorString())

############################################ DOCTOR : List Of Doctor Schedule ######################################################################
    def manage_doctor_schedule(self):
        self.ui.stackedWidget.setCurrentIndex(4)
        self.ui.stackedWidget_2.setCurrentIndex(4)
        self.ui.scrollArea.verticalScrollBar().setValue(0)
        self.check_sidebars()
        self.display_doctor_schedule()
        
    def display_doctor_schedule(self):
        url = QUrl("http://localhost:5000/doctor_schedule")
        request = QNetworkRequest(url)
        if self.current_user["middleName"] != "":
            name = f"Dr.{self.current_user['firstName']} {self.current_user['middleName']} {self.current_user['lastName']}"
        else:
            name = f"Dr.{self.current_user['firstName']} {self.current_user['lastName']}"
        data = QJsonDocument({
            "doctor": QJsonValue(name)
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, QJsonDocument(data).toJson())
        reply.finished.connect(self.handle_display_doctor_schedule_reply)
        
    def handle_display_doctor_schedule_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            schedule = QJsonDocument.fromJson(data).object()
            self.display_doctor_schedule_table(schedule["appointments"])
        else:
            print(reply.errorString())
            
    def display_doctor_schedule_table(self, schedule):
        table = self.ui.doctor_schedule_table
        table.setRowCount(len(schedule))
        for row, appointment in enumerate(schedule):
            table.setItem(row, 0, QTableWidgetItem(appointment["date"]))
            table.setItem(row, 1, QTableWidgetItem(appointment["time"]))
            table.setItem(row, 2, QTableWidgetItem(appointment["patientHN"]))
            table.setItem(row, 3, QTableWidgetItem(appointment["patientName"]))

    def search_schedule(self):
        search_date = self.ui.date_search_button.date().toString("MM-dd-yyyy")
        search_hn = self.ui.search_hnNo_button.text()
        url = QUrl(f"http://localhost:5000/doctor_schedule/{search_date}/{search_hn}")
        request = QNetworkRequest(url)
        if self.current_user["middleName"] != "":
            name = f"Dr.{self.current_user['firstName']} {self.current_user['middleName']} {self.current_user['lastName']}"
        else:
            name = f"Dr.{self.current_user['firstName']} {self.current_user['lastName']}"
        data = QJsonDocument({
            "doctor": QJsonValue(name)
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, QJsonDocument(data).toJson())
        reply.finished.connect(self.handle_search_schedule_reply)

    def handle_search_schedule_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            schedule = QJsonDocument.fromJson(data).object()
            self.display_doctor_search_schedule_table(schedule["appointments"])
        else:
            print(reply.errorString())

    def display_doctor_search_schedule_table(self, schedule):
        table = self.ui.doctor_schedule_table
        table.setRowCount(len(schedule))
        for row, appointment in enumerate(schedule):
            table.setItem(row, 0, QTableWidgetItem(appointment["date"]))
            table.setItem(row, 1, QTableWidgetItem(appointment["time"]))
            table.setItem(row, 2, QTableWidgetItem(appointment["patientHN"]))
            table.setItem(row, 3, QTableWidgetItem(appointment["patientName"]))

############################################ DOCTOR : View Individual Schedule Page #####################################################################

    def display_schedule(self):
        url = QUrl("http://localhost:5000/appointment_list")
        request = QNetworkRequest(url)
        data = QJsonDocument({
            "patient": QJsonValue(self.current_user["hnNumber"])
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, QJsonDocument(data).toJson())
        reply.finished.connect(self.handle_display_schedule_reply)
        
    def handle_display_schedule_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            schedule = QJsonDocument.fromJson(data).object()
            self.display_schedule_table(schedule["appointments"])
        else:
            print(reply.errorString())
            
    def display_schedule_table(self, schedule):
        table = self.ui.patient_schedule_table
        table.setRowCount(len(schedule))
        for row, appointment in enumerate(schedule):
            table.setItem(row, 0, QTableWidgetItem(appointment["date"]))
            table.setItem(row, 1, QTableWidgetItem(appointment["time"]))
            table.setItem(row, 2, QTableWidgetItem(appointment["doctor"]))

    def search_appointment(self):
        search_date = self.ui.appointment_date.date().toString("MM-dd-yyyy")
        url = QUrl(f"http://localhost:5000/appointment_list/{search_date}")
        request = QNetworkRequest(url)
        data = QJsonDocument({
            "patient": QJsonValue(self.current_user["hnNumber"])
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, QJsonDocument(data).toJson())
        reply.finished.connect(self.handle_search_appointment_reply)
        
    def handle_search_appointment_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            schedule = QJsonDocument.fromJson(data).object()
            self.display_search_schedule_table(schedule["appointments"])
        else:
            print(reply.errorString())
            
    def display_search_schedule_table(self, schedule):
        table = self.ui.patient_schedule_table
        table.setRowCount(len(schedule))
        for row, appointment in enumerate(schedule):
            table.setItem(row, 0, QTableWidgetItem(appointment["date"]))
            table.setItem(row, 1, QTableWidgetItem(appointment["time"]))
            table.setItem(row, 2, QTableWidgetItem(appointment["doctor"]))

############################################ PATIENT : View Medical Record ########################################################################
    def get_lab_result(self):
        url = QUrl("http://localhost:5000/get_lab_result")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        
        data = QJsonDocument({
            "hnNumber": QJsonValue(self.current_user["hnNumber"])
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_get_lab_result_reply)
    
    def handle_get_lab_result_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            lab_result = QJsonDocument.fromJson(data).object()
            self.display_lab_result(lab_result["lab_replies"])
        else:
            print(reply.errorString())
    
    def display_lab_result(self, lab_result):
        table = self.ui.lab_test_list_table_3
        table.setRowCount(len(lab_result))
        for row, labtest in enumerate(lab_result):
            labresult = labtest["lab_test"]
            if labresult == None:
                status = "Pending"
            elif labresult["notes"] == None and labresult["file"] == None:
                status = "Rejected"
            else:
                status = "Completed"
            table.setItem(row, 0, QTableWidgetItem(labtest["labType"]))
            table.setItem(row, 1, QTableWidgetItem(labtest["requesting_doctor"]))
            table.setItem(row, 2, QTableWidgetItem(status))
            table.setItem(row, 3, QTableWidgetItem(labtest["date"]))
            table.setItem(row, 4, QTableWidgetItem(labtest["time"]))
    
    def display_medical_record(self):
        medical_record = self.current_user["medicalRecord"]
        user = self.current_user
        
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.stackedWidget_3.setCurrentIndex(0)
        self.ui.scrollArea_2.verticalScrollBar().setValue(0)
        self.check_sidebars()
        self.ui.med_record_photo.setPixmap(QPixmap(user["profile"]))
        self.ui.med_record_photo.setScaledContents(True)
        self.ui.med_record_photo.setFixedSize(100, 100)
        if medical_record["middleName"] != "":
            name = f"{user['firstName']} {user['middleName']} {user['lastName']}"
        else:
            name = f"{user['firstName']} {user['lastName']}"
        self.ui.med_record_name.setText(name)
        self.ui.patient_email_display_2.setText(user["email"])
        self.ui.med_record_hn_no.setText(medical_record["hnNumber"])
        self.ui.med_record_dob.setText(medical_record["birthDate"])
        self.ui.med_record_sex.setText(medical_record["sex"])
        dob = medical_record["birthDate"]
        dob_date = datetime.strptime(dob, "%m/%d/%Y")
        current_date = datetime.now()
        if current_date.month < dob_date.month or (current_date.month == dob_date.month and current_date.day < dob_date.day):
            age = current_date.year - dob_date.year - 1
        else:
            age = current_date.year - dob_date.year
        self.ui.med_record_age.setText(str(age))
        self.ui.med_record_weight.setText(medical_record["weight"])
        self.ui.med_record_height.setText(medical_record["height"])
        self.ui.med_record_address.setText(medical_record["address"])
        self.ui.med_record_tel.setText(medical_record["tel"])
        self.ui.med_record_blood_type.setText(medical_record["bloodType"])
        self.ui.med_record_blood_pressure.setText(medical_record["bloodPressure"])
        blood_pressure = medical_record["bloodPressure"].split("/")
        if int(blood_pressure[0]) > 120 or int(blood_pressure[1]) > 80:
            self.ui.med_record_blood_warning.setStyleSheet("color: red;")
            self.ui.med_record_blood_warning.setText("You have high blood pressure")
        elif int(blood_pressure[0]) < 90 or int(blood_pressure[1]) < 60:
            self.ui.med_record_blood_warning.setStyleSheet("color: red;")
            self.ui.med_record_blood_warning.setText("You have low blood pressure")
        else:
            self.ui.med_record_blood_warning.setStyleSheet("color: green;")
            self.ui.med_record_blood_warning.setText("Normal blood pressure")

        self.vaccine_list = medical_record["vaccineHistory"]
        self.medication_list = medical_record["medicationHistory"]
        self.allergy_list = medical_record["allergy"]
        self.display_med_record_vaccine()
        self.display_med_record_medication()
        self.display_med_record_allergy()
        self.get_lab_result()

    def display_med_record_vaccine(self):
        table = self.ui.vaccine_list_table_3
        table.setRowCount(len(self.vaccine_list))
        for row, vaccine in enumerate(self.vaccine_list):
            table.setItem(row, 0, QTableWidgetItem(vaccine["name"]))
            table.setItem(row, 1, QTableWidgetItem(vaccine["dateAdministered"]))

    def display_med_record_medication(self):
        table = self.ui.medication_list_table_3
        table.setRowCount(len(self.medication_list))
        for row, medication in enumerate(self.medication_list):
            table.setItem(row, 0, QTableWidgetItem(medication["name"]))
            table.setItem(row, 1, QTableWidgetItem(medication["amount"]))
            table.setItem(row, 2, QTableWidgetItem(medication["dosage"]))
            table.setItem(row, 3, QTableWidgetItem(medication["duration"]))
            table.setItem(row, 4, QTableWidgetItem(medication["doctorAdministered"]))
            table.setItem(row, 5, QTableWidgetItem(medication["dateAdministered"]))
            table.setItem(row, 6, QTableWidgetItem(medication["timeAdministered"]))
            table.setItem(row, 7, QTableWidgetItem(medication["sidenote"]))
                          
    def display_med_record_allergy(self):
        table = self.ui.allergy_list_table_3
        table.setRowCount(len(self.allergy_list))
        for row, allergy in enumerate(self.allergy_list):
            table.setItem(row, 0, QTableWidgetItem(allergy["allergy"]))

############################################ PATIENT : List Of Bills #####################################################################
            
    def manage_bill_payment(self):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.stackedWidget_3.setCurrentIndex(3)
        self.ui.scrollArea_2.verticalScrollBar().setValue(0)
        self.check_sidebars()
        self.display_bill_payment()

    def display_bill_payment(self):
        url = QUrl("http://localhost:5000/get_bills")
        request = QNetworkRequest(url)
        data = QJsonDocument({
            "hnNumber": QJsonValue(self.current_user["hnNumber"])
        })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_display_bill_payments_reply)

    def handle_display_bill_payments_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            bills = QJsonDocument.fromJson(data).object()
            self.display_bill_payment_table(bills["bills"])
        else:
            print(reply.errorString())
        
############################################ PATIENT : View Individual Bill #########################################################################

    def view_bill(self):
        selected_row = self.ui.bill_list_table.currentRow()
        if selected_row >= 0:
            url = QUrl("http://localhost:5000/view_bill")
            request = QNetworkRequest(url)
            data = QJsonDocument({
                "bill_id": QJsonValue(self.ui.bill_list_table.item(selected_row, 0).text())
            })
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            reply = self.network_manager.post(request, data.toJson())
            reply.finished.connect(self.handle_view_bill_reply)

        else:
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please select a bill to view.")
            dialog.exec()

    def handle_view_bill_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            bill = QJsonDocument.fromJson(data).object()
            self.display_bill(bill["bill"])
        else:
            print(reply.errorString())

    def display_bill(self, bill):
        self.ui.stackedWidget.setCurrentIndex(5)
        self.ui.stackedWidget_3.setCurrentIndex(2)
        self.ui.scrollArea_2.verticalScrollBar().setValue(0)
        self.ui.bill_number.setText(str(bill["id"]))
        self.ui.bill_date.setText(bill["date"])
        self.ui.bill_patient_name.setText(bill["patientName"])
        self.ui.bill_patient_hn_no.setText(bill["hnNumber"])
        self.ui.bill_total_charge.setText(str(bill["totalPrice"]))
        self.ui.bill_status.setText(bill["status"])
        table = self.ui.bill_table
        table.setRowCount(len(bill["items"]))
        for row, item in enumerate(bill["items"]):
            table.setItem(row, 0, QTableWidgetItem(item["name"]))
            table.setItem(row, 1, QTableWidgetItem(item["price"]))

    def toggle_discount(self):
        if self.ui.select_discount.currentText() == 'Health Insurance Card':
            self.ui.insurance.setVisible(True)
        else:
            self.ui.insurance.setVisible(False)

    def apply_discount(self):
        bill_id = self.ui.bill_number.text()
        discount = self.ui.select_discount.currentText()
        insurance = self.ui.insurance_value.text()
        url = QUrl("http://localhost:5000/apply_discount")
        request = QNetworkRequest(url)
        if discount == "Medical Golden Card" or discount == "Clinic Member Card":
            data = QJsonDocument({
                "bill_id": QJsonValue(bill_id),
                "discount": QJsonValue(discount),
            })
        elif discount == "Health Insurance Card":
            data = QJsonDocument({
                "bill_id": QJsonValue(bill_id),
                "discount": QJsonValue(discount),
                "insurance": QJsonValue(insurance),
            })
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_apply_discount_reply)

    def handle_apply_discount_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            bill = QJsonDocument.fromJson(data).object()
            if bill["message"] == "Discount applied successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Discount applied successfully.")
                dialog.exec()
                self.display_bill(bill["bill"])
        else:
            print(reply.errorString())
            
############################################ PATIENT : Make New Appointment #####################################################################

    def get_specialty_list(self):
        url = QUrl("http://localhost:5000/doctor_speciality")
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_get_specialty_list_reply)

    def handle_get_specialty_list_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            specialty_list = QJsonDocument.fromJson(data).object()
            self.add_appointment(specialty_list["speciality"])

    def get_doctor_from_specialty(self):
        specialty = self.specialty_list.currentText()
        url = QUrl(f"http://localhost:5000/doctor_speciality/{specialty}")
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_get_doctor_from_specialty_reply)

    def handle_get_doctor_from_specialty_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            doctor_list = QJsonDocument.fromJson(data).object()
            self.doctor_list.clear()
            for doctor in doctor_list["doctors"]:
                self.doctor_list.addItem(doctor["name"])
        else:
            print(reply.errorString())

    def add_appointment(self, list_of_specialties):
        self.appointment_dialog = QDialog(self)
        self.appointment_dialog.setWindowTitle("Add Appointment")
        self.appointment_dialog.resize(300, 200)

        layout = QVBoxLayout(self.appointment_dialog)

        layout2 = QHBoxLayout()
        layout.addLayout(layout2)

        label_appointment_date = QLabel("Appointment Date")
        layout2.addWidget(label_appointment_date)
        self.appointment_date = QDateEdit()
        self.appointment_date.setObjectName(u"appointment_date")
        self.appointment_date.setStyleSheet(u"background-color: white;")
        layout2.addWidget(self.appointment_date)

        layout3 = QHBoxLayout()
        layout.addLayout(layout3)

        label_appointment_time = QLabel("Appointment Time")
        layout3.addWidget(label_appointment_time)
        self.appointment_time = QTimeEdit()
        self.appointment_time.setObjectName(u"appointment_time")
        self.appointment_time.setStyleSheet(u"background-color: white;")
        layout3.addWidget(self.appointment_time)

        layout4 = QHBoxLayout()
        layout.addLayout(layout4)

        label_specialty = QLabel("Department")
        layout4.addWidget(label_specialty)
        self.specialty_list = QComboBox()
        self.specialty_list.setObjectName(u"specialty_list")
        self.specialty_list.setStyleSheet(u"background-color: white;")
        self.specialty_list.addItem("Please select a department") 
        for specialty in list_of_specialties:
            self.specialty_list.addItem(specialty["speciality"])
        layout4.addWidget(self.specialty_list)
        self.specialty_list.currentIndexChanged.connect(self.get_doctor_from_specialty)

        layout5 = QHBoxLayout()
        layout.addLayout(layout5)

        label_doctor = QLabel("Doctor")
        list_of_doctors = [] 
        layout5.addWidget(label_doctor)
        self.doctor_list = QComboBox()
        self.doctor_list.setObjectName(u"doctor_list")
        self.doctor_list.setStyleSheet(u"background-color: white;")
        for doctor in list_of_doctors:
            self.doctor_list.addItem(doctor["name"])
        layout5.addWidget(self.doctor_list)
        for doctor in list_of_doctors:
            self.doctor_list.addItem(doctor["name"])
            

        verticalSpacer = QSpacerItem(20, 105, QSizePolicy.Minimum, QSizePolicy.Expanding)
        layout.addItem(verticalSpacer)

        confirm_appointment_button = QPushButton("Add Appointment")
        confirm_appointment_button.setObjectName(u"confirm_appointment_button")
        confirm_appointment_button.clicked.connect(self.add_appointment_to_schedule)
        confirm_appointment_button.setStyleSheet(u"QPushButton#confirm_appointment_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_appointment_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        layout.addWidget(confirm_appointment_button)
        self.appointment_dialog.exec()

    def add_appointment_to_schedule(self):
        date = self.appointment_date.date().toString("dd/MM/yyyy")
        time = self.appointment_time.time().toString("HH:mm")
        doctor = self.doctor_list.currentText()
        if not doctor:
            QMessageBox.warning(self, "Warning", "Please select a doctor.")
            return
        url = QUrl("http://localhost:5000/appointment")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "date": QJsonValue(date),
            "time": QJsonValue(time),
            "doctor": QJsonValue(doctor),
            "patient": QJsonValue(self.current_user["hnNumber"])
        })

        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_add_appointment_reply)

    def handle_add_appointment_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            appointment_data = QJsonDocument.fromJson(data).object()
            if appointment_data["message"] == "Doctor is not available at this time":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Time slot alredy booked. Please choose another time.")
                dialog.exec()
            if appointment_data["message"] == "Appointment added successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Appointment added successfully.")
                dialog.exec()
                self.appointment_dialog.close()
                self.display_schedule()
        else:
            print(reply.errorString())

############################################ PATIENT : Cancel Appointment #####################################################################
    
    def cancel_appointment(self):
        selected_row = self.ui.patient_schedule_table.currentRow()
        if selected_row >= 0:
            url = QUrl("http://localhost:5000/cancel_appointment")
            request = QNetworkRequest(url)
            
            data = QJsonDocument({
                "patient": QJsonValue(self.current_user["hnNumber"]),
                "date": QJsonValue(self.ui.patient_schedule_table.item(selected_row, 0).text()),
                "time": QJsonValue(self.ui.patient_schedule_table.item(selected_row, 1).text()),
                "doctor": QJsonValue(self.ui.patient_schedule_table.item(selected_row, 2).text())
            })
            
            request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
            reply = self.network_manager.post(request, data.toJson())
            reply.finished.connect(self.handle_cancel_appointment_reply)
            
    def handle_cancel_appointment_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            appointment_data = QJsonDocument.fromJson(data).object()
            if appointment_data["message"] == "Appointment cancelled successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Appointment cancelled successfully.")
                dialog.exec()
                self.display_schedule()
        else:
            print(reply.errorString())
         
############################################ ADMIN : Add Doctor ##########################################################################
      
    def add_doctor(self):
        firstName, middleName, lastName, speciality, userName_doctor, password_doctor, email = self.get_doctor_data()
        profile = self.profile
        if firstName == "" or lastName == "" or speciality == "" or userName_doctor == "" or password_doctor == "":
            dialog = QMessageBox()
            dialog.setIcon(QMessageBox.Warning)
            dialog.setWindowTitle("Warning")
            dialog.setText("Please fill in all the required fields.")
            dialog.exec()
            return
        
        if profile == "":
            profile = self.ui.directory.text()
            if profile == "TextLabel":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Please upload a profile picture.")
                dialog.exec()
                return
        
        url = QUrl("http://localhost:5000/admin")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")

        data = QJsonDocument({
            "firstName": QJsonValue(firstName),
            "middleName": QJsonValue(middleName),
            "lastName": QJsonValue(lastName),
            "speciality": QJsonValue(speciality),
            "username": QJsonValue(userName_doctor),
            "password": QJsonValue(password_doctor),
            "profile": QJsonValue(profile),
            "email": QJsonValue(email)
        })
        
        reply = self.network_manager.post(request, data.toJson())
        reply.finished.connect(self.handle_admin_reply)

    def handle_admin_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            return_message = QJsonDocument.fromJson(data).object()
            if return_message["message"] == "Username already exists":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Warning)
                dialog.setWindowTitle("Warning")
                dialog.setText("Username already exists. Please choose another username.")
                dialog.exec()
                return
            if return_message["message"] == "Doctor added successfully":
                dialog = QMessageBox()
                dialog.setIcon(QMessageBox.Information)
                dialog.setWindowTitle("Success")
                dialog.setText("Doctor added successfully.")
                dialog.exec()
                self.ui.doctor_profile.clear()
                self.ui.userName_2.clear()
                self.ui.password_doctor.clear()
                self.ui.firstName.clear()
                self.ui.middleName.clear()
                self.ui.lastName.clear()
                self.ui.speciality.clear()
                self.ui.doctor_email_input.clear()
        else:
            print(reply.errorString())

    def get_doctor_data(self):
        firstName = self.ui.firstName.text()
        middleName = self.ui.middleName.text()
        lastName = self.ui.lastName.text()
        speciality = self.ui.speciality.text()
        username = self.ui.userName_2.text()
        password = self.ui.password_doctor.text()
        email = self.ui.doctor_email_input.text()
        return firstName, middleName, lastName, speciality, username, password, email
    
############################################ ADMIN : Profile Picture(upload/capture) For Adding Doctor #############################################

    def doctor_take_picture(self):
        self.camera2 = Camera(self.ui, "doctor")
        self.camera2.show()
        
    def doctor_finish_upload(self):
        self.doctor_display_image()
        self.upload_file_dialog.close()
    
    def doctor_display_image(self):
        file = open(self.profile, "rb").read()
        image = QPixmap.fromImage(QImage.fromData(file))
        self.ui.doctor_profile.setPixmap(image)
        self.ui.doctor_profile.setScaledContents(True)
        self.ui.doctor_profile.setFixedSize(100, 100)
        
    def browse_profile2(self):
        self.upload_file_dialog = QDialog()
        self.upload_file_dialog.setWindowTitle("Browse File")
        self.upload_file_dialog.resize(400, 300)
        layout = QVBoxLayout(self.upload_file_dialog)
        file_button = QPushButton("Browse File")
        file_button.clicked.connect(self.image_upload2)
        layout.addWidget(file_button)
        self.file_label = QLabel("No file selected")
        layout.addWidget(self.file_label)
        upload_button = QPushButton("Upload File")
        upload_button.clicked.connect(self.doctor_finish_upload)
        layout.addWidget(upload_button)
        self.upload_file_dialog.exec() 

    def image_upload2(self):
        fname = QFileDialog.getOpenFileName(self,"Open File", "","All Files(*);;Python Files(*.py)")
        
        if fname:
            pixmap = QPixmap(fname[0])
            self.file_label.setText(str(fname))
            self.file_name = fname[0].split("/")[-1]
            if pixmap.isNull():
                self.file_label.setText("No file selected")
            else:
                self.file_label.setPixmap(pixmap)
                self.file_label.setScaledContents(True)
                self.file_label.setFixedSize(100, 100)
                directory = f"upload/{self.file_name}"
                file = QImage(fname[0])
                file.save(directory)
                allowed_file = self.allowed_file(self.file_name)
                if allowed_file:
                    self.profile = directory

############################################ ADMIN : Display List Of Doctors #########################################################################
    
    def view_doctor_list(self):
        url = QUrl("http://localhost:5000/doctor_list")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_doctor_list_reply)
        self.ui.stackedWidget.setCurrentIndex(7)

    def handle_doctor_list_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            doctor_list = QJsonDocument.fromJson(data).object()
            self.display_doctor_list(doctor_list["doctors"])
        else:
            print(reply.errorString())

    def display_doctor_list(self, doctor_list):
        table = self.ui.doctor_list_table
        table.setRowCount(len(doctor_list))
        for row, current_doctor in enumerate(doctor_list):
            table.setItem(row, 0, QTableWidgetItem(current_doctor["username"]))
            table.setItem(row, 1, QTableWidgetItem(current_doctor["passwordID"]))
            table.setItem(row, 2, QTableWidgetItem(current_doctor["name"]))
            table.setItem(row, 3, QTableWidgetItem(current_doctor["speciality"]))

    def search_doctor(self):
        print("searching")
        search_username = self.ui.search_username.text()
        url = QUrl(f"http://localhost:5000/doctor_list/{search_username}")
        request = QNetworkRequest(url)
        reply = self.network_manager.get(request)
        reply.finished.connect(self.handle_search_doctor_reply)
        
    def handle_search_doctor_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            doctor_list = QJsonDocument.fromJson(data).object()
            self.display_search_doctor_list(doctor_list["doctors"])
        else:
            print(reply.errorString())

    def display_search_doctor_list(self, doctor_list):
        table = self.ui.doctor_list_table
        table.setRowCount(len(doctor_list))
        for row, current_doctor in enumerate(doctor_list):
            table.setItem(row, 0, QTableWidgetItem(current_doctor["username"]))
            table.setItem(row, 1, QTableWidgetItem(current_doctor["passwordID"]))
            table.setItem(row, 2, QTableWidgetItem(current_doctor["name"]))
            table.setItem(row, 3, QTableWidgetItem(current_doctor["speciality"]))

############################################ Show / Hide Password ##############################################################
    
    def show_password(self):
        if self.ui.password.echoMode() == QLineEdit.Password:
            self.ui.password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.password.setEchoMode(QLineEdit.Password)
 
    def show_old_password(self):
        if self.ui.old_password.echoMode() == QLineEdit.Password:
            self.ui.old_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.old_password.setEchoMode(QLineEdit.Password)

    def show_confirm_password(self):
        if self.ui.confirm_new_password.echoMode() == QLineEdit.Password:
            self.ui.confirm_new_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.confirm_new_password.setEchoMode(QLineEdit.Password)

    def show_new_password(self):
        if self.ui.new_password.echoMode() == QLineEdit.Password:
            self.ui.new_password.setEchoMode(QLineEdit.Normal)
        else:
            self.ui.new_password.setEchoMode(QLineEdit.Password)
                          
############################################ LOG OUT ###############################################################################

    def logout(self):
        url = QUrl("http://localhost:5000/logout")
        request = QNetworkRequest(url)
        request.setHeader(QNetworkRequest.ContentTypeHeader, "application/json")
        reply = self.network_manager.post(request, QJsonDocument().toJson())
        reply.finished.connect(self.handle_logout_reply)
    
    def handle_logout_reply(self):
        reply: QNetworkReply = self.sender()
        if reply.error() == QNetworkReply.NoError:
            data = reply.readAll()
            logout_data = QJsonDocument.fromJson(data).object()
            if logout_data["message"] == "Logged out successfully":
                self.ui.stackedWidget.setCurrentIndex(1)
                self.ui.username.clear()
                self.ui.password.clear()
        else:
            print(reply.errorString())
            
############################################ Main Function #####################################################################

def main():
    app = QApplication(sys.argv)
        
    window = MainWindow()  
    window.show()
    app.exec()

    app.lastWindowClosed.connect(window.close)
        
if __name__ == "__main__":
    main()