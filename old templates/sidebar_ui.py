# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sidebar.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableView, QTextEdit, QVBoxLayout,
    QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(720, 360)
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
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
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


        self.gridLayout.addWidget(self.icon_name_widget, 0, 0, 1, 1)

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
        self.horizontalLayout_3.setSpacing(6)
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
        self.scrollArea.setMaximumSize(QSize(1280, 10000))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 738))
        self.scrollAreaWidgetContents.setMaximumSize(QSize(1280, 16777215))
        self.verticalLayout_3 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.stackedWidget.setMaximumSize(QSize(1280, 720))
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setMaximumSize(QSize(10000, 10000))
        self.verticalLayout_13 = QVBoxLayout(self.home_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.home_label = QLabel(self.home_page)
        self.home_label.setObjectName(u"home_label")

        self.verticalLayout_13.addWidget(self.home_label)

        self.stackedWidget.addWidget(self.home_page)
        self.lab_page = QWidget()
        self.lab_page.setObjectName(u"lab_page")
        self.verticalLayout_11 = QVBoxLayout(self.lab_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget = QWidget(self.lab_page)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_18 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)

        self.lab_title = QLabel(self.widget)
        self.lab_title.setObjectName(u"lab_title")
        self.lab_title.setStyleSheet(u"font: 20pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_16.addWidget(self.lab_title)

        self.horizontalSpacer_19 = QSpacerItem(188, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_19)


        self.verticalLayout_10.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_20 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_20)

        self.dat_request_2 = QLabel(self.widget)
        self.dat_request_2.setObjectName(u"dat_request_2")
        self.dat_request_2.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_17.addWidget(self.dat_request_2)

        self.horizontalSpacer_21 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)

        self.date_request = QLabel(self.widget)
        self.date_request.setObjectName(u"date_request")
        self.date_request.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_17.addWidget(self.date_request)

        self.horizontalSpacer_22 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_18.addWidget(self.label_5)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_18.addWidget(self.comboBox)

        self.horizontalSpacer_23 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_23)

        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_18.addWidget(self.label_7)

        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_18.addWidget(self.comboBox_2)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";")

        self.verticalLayout_10.addWidget(self.label_6)

        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid black;")

        self.verticalLayout_10.addWidget(self.textEdit)

        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"font: 10pt \"Microsoft Sans Serif\";\n"
"color: white;\n"
"background-color: rgb(39, 86, 193);\n"
"padding: 5%;")

        self.verticalLayout_10.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"background-color: white;\n"
"padding: 5%;\n"
"border: 0.5px solid black;")

        self.verticalLayout_10.addWidget(self.pushButton_5)


        self.verticalLayout_11.addWidget(self.widget)

        self.stackedWidget.addWidget(self.lab_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.verticalLayout_15 = QVBoxLayout(self.schedule_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_4 = QLabel(self.schedule_page)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_15.addWidget(self.label_4)

        self.stackedWidget.addWidget(self.schedule_page)
        self.patientList_page = QWidget()
        self.patientList_page.setObjectName(u"patientList_page")
        self.verticalLayout_14 = QVBoxLayout(self.patientList_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lineEdit_search = QLineEdit(self.patientList_page)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout_2.addWidget(self.lineEdit_search)

        self.searchButton = QPushButton(self.patientList_page)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"border-radius: 10px;")
        icon5 = QIcon()
        icon5.addFile(u":/images/icons8-search-24.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon5)
        self.searchButton.setIconSize(QSize(20, 20))

        self.horizontalLayout_2.addWidget(self.searchButton)


        self.verticalLayout_14.addLayout(self.horizontalLayout_2)

        self.AddPatientButton = QPushButton(self.patientList_page)
        self.AddPatientButton.setObjectName(u"AddPatientButton")
        self.AddPatientButton.setStyleSheet(u"background-color: rgb(39, 86, 193);\n"
"color: white;\n"
"border-radius: 10px;\n"
"")

        self.verticalLayout_14.addWidget(self.AddPatientButton)

        self.label_3 = QLabel(self.patientList_page)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout_14.addWidget(self.label_3)

        self.stackedWidget.addWidget(self.patientList_page)
        self.medical_record_page = QWidget()
        self.medical_record_page.setObjectName(u"medical_record_page")
        self.medical_record_page.setMinimumSize(QSize(0, 720))
        self.medical_record_page.setMaximumSize(QSize(1280, 720))
        self.verticalLayout_12 = QVBoxLayout(self.medical_record_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.medical_record_widget = QWidget(self.medical_record_page)
        self.medical_record_widget.setObjectName(u"medical_record_widget")
        self.medical_record_widget.setMinimumSize(QSize(0, 0))
        self.medical_record_widget.setMaximumSize(QSize(1280, 720))
        self.verticalLayout_9 = QVBoxLayout(self.medical_record_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_patient_info = QLabel(self.medical_record_widget)
        self.label_patient_info.setObjectName(u"label_patient_info")
        self.label_patient_info.setStyleSheet(u"font: 20pt \"Microsoft Sans Serif\";")

        self.verticalLayout_9.addWidget(self.label_patient_info)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.patient_info1_widget = QWidget(self.medical_record_widget)
        self.patient_info1_widget.setObjectName(u"patient_info1_widget")
        self.patient_info1_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.patient_info1_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.label_9 = QLabel(self.patient_info1_widget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setPixmap(QPixmap(u":/images/icons8-user-48.png"))

        self.horizontalLayout_11.addWidget(self.label_9)

        self.horizontalSpacer_7 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_8 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.lineEdit_4 = QLineEdit(self.patient_info1_widget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setStyleSheet(u"font: 15pt \"Microsoft Sans Serif\";\n"
"color: rgb(255, 184, 255);")

        self.horizontalLayout_10.addWidget(self.lineEdit_4)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_13 = QLabel(self.patient_info1_widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_4.addWidget(self.label_13)

        self.lineEdit_5 = QLineEdit(self.patient_info1_widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setStyleSheet(u"color: grey;")

        self.horizontalLayout_4.addWidget(self.lineEdit_5)

        self.label_14 = QLabel(self.patient_info1_widget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.lineEdit_10 = QLineEdit(self.patient_info1_widget)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        self.lineEdit_10.setStyleSheet(u"color: grey;\n"
"")

        self.horizontalLayout_4.addWidget(self.lineEdit_10)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.patient_info1_widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer)

        self.lineEdit_6 = QLineEdit(self.patient_info1_widget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setStyleSheet(u"color: grey;")

        self.horizontalLayout_6.addWidget(self.lineEdit_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.patient_info1_widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.lineEdit_7 = QLineEdit(self.patient_info1_widget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setStyleSheet(u"color: grey;")

        self.horizontalLayout_7.addWidget(self.lineEdit_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_5.addWidget(self.patient_info1_widget)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.patient_info2_widget = QWidget(self.medical_record_widget)
        self.patient_info2_widget.setObjectName(u"patient_info2_widget")
        self.patient_info2_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_4 = QVBoxLayout(self.patient_info2_widget)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_address = QLabel(self.patient_info2_widget)
        self.label_address.setObjectName(u"label_address")

        self.horizontalLayout_8.addWidget(self.label_address)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.lineEdit_address = QLineEdit(self.patient_info2_widget)
        self.lineEdit_address.setObjectName(u"lineEdit_address")
        self.lineEdit_address.setStyleSheet(u"color: grey;")

        self.horizontalLayout_8.addWidget(self.lineEdit_address)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_tel_no = QLabel(self.patient_info2_widget)
        self.label_tel_no.setObjectName(u"label_tel_no")

        self.horizontalLayout_9.addWidget(self.label_tel_no)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_5)

        self.lineEdit_tel_no = QLineEdit(self.patient_info2_widget)
        self.lineEdit_tel_no.setObjectName(u"lineEdit_tel_no")
        self.lineEdit_tel_no.setStyleSheet(u"color: grey;")

        self.horizontalLayout_9.addWidget(self.lineEdit_tel_no)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)


        self.verticalLayout_5.addWidget(self.patient_info2_widget)

        self.patient_info3_widget = QWidget(self.medical_record_widget)
        self.patient_info3_widget.setObjectName(u"patient_info3_widget")
        self.patient_info3_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_7 = QVBoxLayout(self.patient_info3_widget)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalSpacer_10 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_10)

        self.label_blood_status = QLabel(self.patient_info3_widget)
        self.label_blood_status.setObjectName(u"label_blood_status")
        self.label_blood_status.setStyleSheet(u"font: 15pt \"Microsoft Sans Serif\";\n"
"color: grey;")

        self.horizontalLayout_12.addWidget(self.label_blood_status)

        self.horizontalSpacer_11 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_11)


        self.verticalLayout_7.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalSpacer_12 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_12)

        self.blood_icon = QLabel(self.patient_info3_widget)
        self.blood_icon.setObjectName(u"blood_icon")
        self.blood_icon.setBaseSize(QSize(0, 0))
        self.blood_icon.setPixmap(QPixmap(u":/images/icons8-blood-50.png"))

        self.horizontalLayout_13.addWidget(self.blood_icon)

        self.horizontalSpacer_13 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_14 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.lineEdit_blood_pressure = QLineEdit(self.patient_info3_widget)
        self.lineEdit_blood_pressure.setObjectName(u"lineEdit_blood_pressure")

        self.horizontalLayout_14.addWidget(self.lineEdit_blood_pressure)

        self.horizontalSpacer_15 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.lineEdit_blood_warning = QLineEdit(self.patient_info3_widget)
        self.lineEdit_blood_warning.setObjectName(u"lineEdit_blood_warning")
        self.lineEdit_blood_warning.setStyleSheet(u"color: red;")

        self.horizontalLayout_15.addWidget(self.lineEdit_blood_warning)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)


        self.verticalLayout_5.addWidget(self.patient_info3_widget)


        self.horizontalLayout_5.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_5)

        self.medical_history_widget = QWidget(self.medical_record_widget)
        self.medical_history_widget.setObjectName(u"medical_history_widget")
        self.medical_history_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.medical_history_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_medical_history = QLabel(self.medical_history_widget)
        self.label_medical_history.setObjectName(u"label_medical_history")
        self.label_medical_history.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_medical_history)

        self.label_allergies = QLabel(self.medical_history_widget)
        self.label_allergies.setObjectName(u"label_allergies")

        self.verticalLayout_8.addWidget(self.label_allergies)

        self.tableView_allergies = QTableView(self.medical_history_widget)
        self.tableView_allergies.setObjectName(u"tableView_allergies")
        self.tableView_allergies.setStyleSheet(u"background-color: grey;")

        self.verticalLayout_8.addWidget(self.tableView_allergies)

        self.label_past_treatment = QLabel(self.medical_history_widget)
        self.label_past_treatment.setObjectName(u"label_past_treatment")

        self.verticalLayout_8.addWidget(self.label_past_treatment)

        self.tableView_past_treatment = QTableView(self.medical_history_widget)
        self.tableView_past_treatment.setObjectName(u"tableView_past_treatment")
        self.tableView_past_treatment.setStyleSheet(u"background-color: grey;")

        self.verticalLayout_8.addWidget(self.tableView_past_treatment)

        self.label_past_treatment_2 = QLabel(self.medical_history_widget)
        self.label_past_treatment_2.setObjectName(u"label_past_treatment_2")

        self.verticalLayout_8.addWidget(self.label_past_treatment_2)

        self.tableView_lab_test = QTableView(self.medical_history_widget)
        self.tableView_lab_test.setObjectName(u"tableView_lab_test")
        self.tableView_lab_test.setStyleSheet(u"background-color: grey;")

        self.verticalLayout_8.addWidget(self.tableView_lab_test)

        self.label_past_treatment_3 = QLabel(self.medical_history_widget)
        self.label_past_treatment_3.setObjectName(u"label_past_treatment_3")

        self.verticalLayout_8.addWidget(self.label_past_treatment_3)

        self.tableView_vaccination = QTableView(self.medical_history_widget)
        self.tableView_vaccination.setObjectName(u"tableView_vaccination")
        self.tableView_vaccination.setStyleSheet(u"background-color: grey;")

        self.verticalLayout_8.addWidget(self.tableView_vaccination)

        self.label_past_treatment_4 = QLabel(self.medical_history_widget)
        self.label_past_treatment_4.setObjectName(u"label_past_treatment_4")

        self.verticalLayout_8.addWidget(self.label_past_treatment_4)

        self.tableView_medication = QTableView(self.medical_history_widget)
        self.tableView_medication.setObjectName(u"tableView_medication")
        self.tableView_medication.setStyleSheet(u"background-color: grey;")

        self.verticalLayout_8.addWidget(self.tableView_medication)


        self.verticalLayout_9.addWidget(self.medical_history_widget)


        self.verticalLayout_12.addWidget(self.medical_record_widget)

        self.stackedWidget.addWidget(self.medical_record_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.gridLayout.addWidget(self.main_widget, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(3)


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
        self.lab_title.setText(QCoreApplication.translate("MainWindow", u"Lab Request Form", None))
        self.dat_request_2.setText(QCoreApplication.translate("MainWindow", u"Time Requested: xx:xx:xx", None))
        self.date_request.setText(QCoreApplication.translate("MainWindow", u"Date Requested: xx/xx/xxxx", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Requested Tests:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Complete Blood Count (CBC)", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic Metabolic Panel (BMP)", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Liver Function Tests (LFTs)", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Lipid Profile", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("MainWindow", u"Thyroid Function Tests", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("MainWindow", u"Blood Glucose Test", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("MainWindow", u"Coagulation Profile", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("MainWindow", u"Urinalysis", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("MainWindow", u"Cancer Markers", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("MainWindow", u"Infectious Disease Tests", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Urgency:", None))
        self.comboBox_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Routine", None))
        self.comboBox_2.setItemText(1, QCoreApplication.translate("MainWindow", u"Urgent", None))
        self.comboBox_2.setItemText(2, QCoreApplication.translate("MainWindow", u"Immediately Necessary", None))

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Reason For Request:", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"schedule", None))
        self.searchButton.setText("")
        self.AddPatientButton.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"patient", None))
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
        self.label_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.lineEdit_address.setText(QCoreApplication.translate("MainWindow", u"xxx xxx xxxxxxxxx xxx", None))
        self.label_tel_no.setText(QCoreApplication.translate("MainWindow", u"Tel:", None))
        self.lineEdit_tel_no.setText(QCoreApplication.translate("MainWindow", u"xxxx xxxx xxxx ", None))
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

