# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableView,
    QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 488)
        MainWindow.setMinimumSize(QSize(720, 360))
        MainWindow.setMaximumSize(QSize(1280, 720))
        MainWindow.setStyleSheet(u"background-color: rgb(240, 249, 255);\n"
"\n"
"QPushButton {\n"
"	font.pointSize: 100;\n"
"	minimumPointSize: 10;\n"
"	fontSizeMode: Text.Fit;	\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"border: 0;")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.centralwidget)
        self.icon_name_widget.setObjectName(u"icon_name_widget")
        self.icon_name_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(39, 86, 193);\n"
"}\n"
"\n"
"QPushButton{\n"
"	color: white;\n"
"	text-align: left;\n"
"	height: 30px;\n"
"	border: none;\n"
"	padding-left: 10px;\n"
"	border-radius: 10px;\n"
"	font: 20pt \"Microsoft Sans Serif\";\n"
"}\n"
"\n"
"QPushButton:checked{\n"
"	background-color: rgb(144, 194, 255);\n"
"	font-weight: bold;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.icon_name_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(12, 12, 12, 12)
        self.Menu_icon = QPushButton(self.icon_name_widget)
        self.Menu_icon.setObjectName(u"Menu_icon")
        self.Menu_icon.setEnabled(True)
        self.Menu_icon.setMinimumSize(QSize(50, 50))
        icon = QIcon()
        icon.addFile(u":/images/medical-team.png", QSize(), QIcon.Normal, QIcon.Off)
        self.Menu_icon.setIcon(icon)
        self.Menu_icon.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.Menu_icon)

        self.home_Button = QPushButton(self.icon_name_widget)
        self.home_Button.setObjectName(u"home_Button")
        self.home_Button.setMinimumSize(QSize(40, 40))
        icon1 = QIcon()
        icon1.addFile(u":/images/icons8-home-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_Button.setIcon(icon1)
        self.home_Button.setIconSize(QSize(40, 40))
        self.home_Button.setCheckable(True)
        self.home_Button.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.home_Button)

        self.patientListButton = QPushButton(self.icon_name_widget)
        self.patientListButton.setObjectName(u"patientListButton")
        self.patientListButton.setMinimumSize(QSize(40, 40))
        icon2 = QIcon()
        icon2.addFile(u":/images/icons8-list-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patientListButton.setIcon(icon2)
        self.patientListButton.setIconSize(QSize(40, 40))
        self.patientListButton.setCheckable(True)
        self.patientListButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.patientListButton)

        self.scheduleButton = QPushButton(self.icon_name_widget)
        self.scheduleButton.setObjectName(u"scheduleButton")
        self.scheduleButton.setMinimumSize(QSize(40, 40))
        icon3 = QIcon()
        icon3.addFile(u":/images/icons8-schedule-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scheduleButton.setIcon(icon3)
        self.scheduleButton.setIconSize(QSize(40, 40))
        self.scheduleButton.setCheckable(True)
        self.scheduleButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.scheduleButton)

        self.verticalSpacer_2 = QSpacerItem(20, 111, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.icon_name_widget)

        self.main_widget = QWidget(self.centralwidget)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.main_widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget)
#ifndef Q_OS_MAC
        self.horizontalLayout_3.setSpacing(-1)
#endif
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 12, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.Username = QLabel(self.header_widget)
        self.Username.setObjectName(u"Username")

        self.horizontalLayout_3.addWidget(self.Username)

        self.userprofile_pic = QPushButton(self.header_widget)
        self.userprofile_pic.setObjectName(u"userprofile_pic")
        icon4 = QIcon()
        icon4.addFile(u":/images/icons8-user-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.userprofile_pic.setIcon(icon4)
        self.userprofile_pic.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.userprofile_pic)


        self.verticalLayout_2.addWidget(self.header_widget)

        self.scrollArea = QScrollArea(self.main_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMaximumSize(QSize(1280, 16777215))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 1280, 1000024))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1280, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(1280, 1000000))
        self.stackedWidget.setMaximumSize(QSize(1280, 16777215))
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_label = QLabel(self.home_page)
        self.home_label.setObjectName(u"home_label")
        self.home_label.setGeometry(QRect(160, 130, 58, 16))
        self.stackedWidget.addWidget(self.home_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.label_4 = QLabel(self.schedule_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(260, 150, 58, 16))
        self.stackedWidget.addWidget(self.schedule_page)
        self.patientList_page = QWidget()
        self.patientList_page.setObjectName(u"patientList_page")
        self.label_3 = QLabel(self.patientList_page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 130, 58, 16))
        self.AddPatientButton = QPushButton(self.patientList_page)
        self.AddPatientButton.setObjectName(u"AddPatientButton")
        self.AddPatientButton.setGeometry(QRect(450, 30, 100, 32))
        self.AddPatientButton.setStyleSheet(u"background-color: rgb(39, 86, 193);\n"
"color: white;\n"
"border-radius: 10px;\n"
"")
        self.layoutWidget = QWidget(self.patientList_page)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(30, 20, 231, 41))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_search = QLineEdit(self.layoutWidget)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.lineEdit_search)

        self.searchButton = QPushButton(self.layoutWidget)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"border-radius: 10px;")
        icon5 = QIcon()
        icon5.addFile(u":/images/icons8-search-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon5)
        self.searchButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.searchButton)

        self.stackedWidget.addWidget(self.patientList_page)
        self.medical_record_page = QWidget()
        self.medical_record_page.setObjectName(u"medical_record_page")
        self.medical_record_page.setMinimumSize(QSize(0, 1000000))
        self.medical_record_widget = QWidget(self.medical_record_page)
        self.medical_record_widget.setObjectName(u"medical_record_widget")
        self.medical_record_widget.setGeometry(QRect(10, 0, 1280, 1000000))
        self.medical_record_widget.setMinimumSize(QSize(1280, 1000000))
        self.label_patient_info = QLabel(self.medical_record_widget)
        self.label_patient_info.setObjectName(u"label_patient_info")
        self.label_patient_info.setGeometry(QRect(10, 10, 200, 40))
        self.label_patient_info.setStyleSheet(u"font: 20pt \"Microsoft Sans Serif\";")
        self.layoutWidget1 = QWidget(self.medical_record_widget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 70, 771, 291))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.patient_info1_widget = QWidget(self.layoutWidget1)
        self.patient_info1_widget.setObjectName(u"patient_info1_widget")
        self.patient_info1_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.patient_info1_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(130, 60, 50, 50))
        self.label_9.setPixmap(QPixmap(u":/images/icons8-user-48.png"))
        self.lineEdit_4 = QLineEdit(self.patient_info1_widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(110, 140, 113, 21))
        self.lineEdit_4.setStyleSheet(u"font: 15pt \"Microsoft Sans Serif\";\n"
"color: rgb(255, 184, 255);")
        self.layoutWidget2 = QWidget(self.patient_info1_widget)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 170, 281, 20))
        self.horizontalLayout_4 = QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.layoutWidget2)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.layoutWidget2)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color: grey;")

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.label_14 = QLabel(self.layoutWidget2)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.lineEdit_10 = QLineEdit(self.layoutWidget2)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"color: grey;\n"
"")

        self.horizontalLayout_4.addWidget(self.lineEdit_10)

        self.layoutWidget3 = QWidget(self.patient_info1_widget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 200, 229, 22))
        self.horizontalLayout_6 = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_11 = QLabel(self.layoutWidget3)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.lineEdit_6 = QLineEdit(self.layoutWidget3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"color: grey;")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)

        self.layoutWidget4 = QWidget(self.patient_info1_widget)
        self.layoutWidget4.setObjectName(u"layoutWidget4")
        self.layoutWidget4.setGeometry(QRect(20, 240, 227, 22))
        self.horizontalLayout_7 = QHBoxLayout(self.layoutWidget4)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.layoutWidget4)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.lineEdit_7 = QLineEdit(self.layoutWidget4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"color: grey;")

        self.horizontalLayout_7.addWidget(self.lineEdit_7)


        self.horizontalLayout_5.addWidget(self.patient_info1_widget)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.patient_info2_widget = QWidget(self.layoutWidget1)
        self.patient_info2_widget.setObjectName(u"patient_info2_widget")
        self.patient_info2_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit_address = QLineEdit(self.patient_info2_widget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setGeometry(QRect(110, 40, 141, 21))
        self.lineEdit_address.setStyleSheet(u"color: grey;")
        self.lineEdit_tel_no = QLineEdit(self.patient_info2_widget)
        self.lineEdit_tel_no.setObjectName(u"lineEdit_tel_no")
        self.lineEdit_tel_no.setGeometry(QRect(110, 90, 101, 21))
        self.lineEdit_tel_no.setStyleSheet(u"color: grey;")
        self.label_address = QLabel(self.patient_info2_widget)
        self.label_address.setObjectName(u"label_address")
        self.label_address.setGeometry(QRect(20, 40, 58, 16))
        self.label_tel_no = QLabel(self.patient_info2_widget)
        self.label_tel_no.setObjectName(u"label_tel_no")
        self.label_tel_no.setGeometry(QRect(30, 90, 58, 16))

        self.verticalLayout_5.addWidget(self.patient_info2_widget)

        self.patient_info3_widget = QWidget(self.layoutWidget1)
        self.patient_info3_widget.setObjectName(u"patient_info3_widget")
        self.patient_info3_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_blood_status = QLabel(self.patient_info3_widget)
        self.label_blood_status.setObjectName(u"label_blood_status")
        self.label_blood_status.setGeometry(QRect(110, 10, 91, 20))
        self.label_blood_status.setStyleSheet(u"font: 15pt \"Microsoft Sans Serif\";\n"
"color: grey;")
        self.blood_icon = QLabel(self.patient_info3_widget)
        self.blood_icon.setObjectName(u"blood_icon")
        self.blood_icon.setGeometry(QRect(130, 40, 50, 51))
        self.blood_icon.setBaseSize(QSize(0, 0))
        self.blood_icon.setPixmap(QPixmap(u":/images/icons8-blood-50.png"))
        self.lineEdit_blood_pressure = QLineEdit(self.patient_info3_widget)
        self.lineEdit_blood_pressure.setObjectName(u"lineEdit_blood_pressure")
        self.lineEdit_blood_pressure.setGeometry(QRect(130, 90, 51, 21))
        self.lineEdit_blood_warning = QLineEdit(self.patient_info3_widget)
        self.lineEdit_blood_warning.setObjectName(u"lineEdit_blood_warning")
        self.lineEdit_blood_warning.setGeometry(QRect(100, 110, 121, 21))
        self.lineEdit_blood_warning.setStyleSheet(u"color: red;")

        self.verticalLayout_5.addWidget(self.patient_info3_widget)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)

        self.medical_history_widget = QWidget(self.medical_record_widget)
        self.medical_history_widget.setObjectName(u"medical_history_widget")
        self.medical_history_widget.setGeometry(QRect(20, 380, 771, 791))
        self.medical_history_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_medical_history = QLabel(self.medical_history_widget)
        self.label_medical_history.setObjectName(u"label_medical_history")
        self.label_medical_history.setGeometry(QRect(20, 20, 101, 16))
        self.label_medical_history.setStyleSheet(u"")
        self.label_allergies = QLabel(self.medical_history_widget)
        self.label_allergies.setObjectName(u"label_allergies")
        self.label_allergies.setGeometry(QRect(25, 50, 58, 16))
        self.label_past_treatment = QLabel(self.medical_history_widget)
        self.label_past_treatment.setObjectName(u"label_past_treatment")
        self.label_past_treatment.setGeometry(QRect(25, 200, 101, 16))
        self.tableView_past_treatment = QTableView(self.medical_history_widget)
        self.tableView_past_treatment.setObjectName(u"tableView_past_treatment")
        self.tableView_past_treatment.setGeometry(QRect(40, 230, 500, 100))
        self.tableView_past_treatment.setStyleSheet(u"background-color: grey;")
        self.tableView_allergies = QTableView(self.medical_history_widget)
        self.tableView_allergies.setObjectName(u"tableView_allergies")
        self.tableView_allergies.setGeometry(QRect(40, 70, 500, 100))
        self.tableView_allergies.setStyleSheet(u"background-color: grey;")
        self.label_past_treatment_2 = QLabel(self.medical_history_widget)
        self.label_past_treatment_2.setObjectName(u"label_past_treatment_2")
        self.label_past_treatment_2.setGeometry(QRect(25, 350, 101, 16))
        self.tableView_lab_test = QTableView(self.medical_history_widget)
        self.tableView_lab_test.setObjectName(u"tableView_lab_test")
        self.tableView_lab_test.setGeometry(QRect(40, 380, 500, 100))
        self.tableView_lab_test.setStyleSheet(u"background-color: grey;")
        self.label_past_treatment_3 = QLabel(self.medical_history_widget)
        self.label_past_treatment_3.setObjectName(u"label_past_treatment_3")
        self.label_past_treatment_3.setGeometry(QRect(25, 500, 101, 16))
        self.label_past_treatment_4 = QLabel(self.medical_history_widget)
        self.label_past_treatment_4.setObjectName(u"label_past_treatment_4")
        self.label_past_treatment_4.setGeometry(QRect(25, 650, 101, 16))
        self.tableView_vaccination = QTableView(self.medical_history_widget)
        self.tableView_vaccination.setObjectName(u"tableView_vaccination")
        self.tableView_vaccination.setGeometry(QRect(40, 530, 500, 100))
        self.tableView_vaccination.setStyleSheet(u"background-color: grey;")
        self.tableView_medication = QTableView(self.medical_history_widget)
        self.tableView_medication.setObjectName(u"tableView_medication")
        self.tableView_medication.setGeometry(QRect(40, 680, 500, 100))
        self.tableView_medication.setStyleSheet(u"background-color: grey;")
        self.stackedWidget.addWidget(self.medical_record_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout.addWidget(self.main_widget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.Menu_icon.setText("")
        self.home_Button.setText("")
        self.patientListButton.setText("")
        self.scheduleButton.setText("")
        self.Username.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.userprofile_pic.setText("")
        self.home_label.setText(QCoreApplication.translate("MainWindow", u"home", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"schedule", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"patient", None))
        self.AddPatientButton.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))
        self.searchButton.setText("")
        self.label_patient_info.setText(QCoreApplication.translate("MainWindow", u"Patient Informations", None))
        self.label_9.setText("")
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Name Lastname", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"f/m", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.lineEdit_10.setText(QCoreApplication.translate("MainWindow", u"xx ", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"xx kg.", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.lineEdit_7.setText(QCoreApplication.translate("MainWindow", u"xxx cm.", None))
        self.lineEdit_address.setText(QCoreApplication.translate("MainWindow", u"xxx xxx xxxxxxxxx xxx", None))
        self.lineEdit_tel_no.setText(QCoreApplication.translate("MainWindow", u"xxxx xxxx xxxx ", None))
        self.label_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.label_tel_no.setText(QCoreApplication.translate("MainWindow", u"Tel:", None))
        self.label_blood_status.setText(QCoreApplication.translate("MainWindow", u"Blood Status", None))
        self.blood_icon.setText("")
        self.lineEdit_blood_pressure.setText(QCoreApplication.translate("MainWindow", u"xxxx /xx", None))
        self.lineEdit_blood_warning.setText(QCoreApplication.translate("MainWindow", u"Lower than average", None))
        self.label_medical_history.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.label_allergies.setText(QCoreApplication.translate("MainWindow", u"Allergies:", None))
        self.label_past_treatment.setText(QCoreApplication.translate("MainWindow", u"Past Treatment:", None))
        self.label_past_treatment_2.setText(QCoreApplication.translate("MainWindow", u"Lab Test Result:", None))
        self.label_past_treatment_3.setText(QCoreApplication.translate("MainWindow", u"Vaccination:", None))
        self.label_past_treatment_4.setText(QCoreApplication.translate("MainWindow", u"Medication:", None))
    # retranslateUi


