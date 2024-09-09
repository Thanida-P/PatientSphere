# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QComboBox, QDateEdit,
    QGridLayout, QHBoxLayout, QHeaderView, QLabel,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QTextEdit, QVBoxLayout, QWidget)
import images_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(825, 500)
        MainWindow.setMinimumSize(QSize(800, 500))
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
        self.verticalLayout_65 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_65.setSpacing(0)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setLineWidth(1)
        self.loading = QWidget()
        self.loading.setObjectName(u"loading")
        self.verticalLayout_18 = QVBoxLayout(self.loading)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalSpacer_13 = QSpacerItem(20, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_13)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalSpacer_48 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_48)

        self.app_title_2 = QLabel(self.loading)
        self.app_title_2.setObjectName(u"app_title_2")
        self.app_title_2.setStyleSheet(u"color: #EE99F3; font-size: 100px\n"
"px; font-weight: bold; font-family: Monospace;")

        self.horizontalLayout_27.addWidget(self.app_title_2)

        self.horizontalSpacer_49 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_49)


        self.verticalLayout_18.addLayout(self.horizontalLayout_27)

        self.verticalSpacer_14 = QSpacerItem(20, 97, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_18.addItem(self.verticalSpacer_14)

        self.stackedWidget.addWidget(self.loading)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.login.setStyleSheet(u"")
        self.verticalLayout_16 = QVBoxLayout(self.login)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalSpacer = QSpacerItem(20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalSpacer_25 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_25)

        self.app_title = QLabel(self.login)
        self.app_title.setObjectName(u"app_title")
        self.app_title.setStyleSheet(u"color: #EE99F3; font-size: 100px\n"
"px; font-weight: bold; font-family: Monospace;")

        self.horizontalLayout_20.addWidget(self.app_title)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_26)


        self.verticalLayout_16.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_27)

        self.label_2 = QLabel(self.login)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: black; font-size: 30px; font-family: Monospace; font-weight: bold; padding-top: 20px;")

        self.horizontalLayout_25.addWidget(self.label_2)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_28)


        self.verticalLayout_16.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_29)

        self.label_3 = QLabel(self.login)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: black; font-size: 30px; font-family: Monospace;")

        self.horizontalLayout_24.addWidget(self.label_3)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_30)


        self.verticalLayout_16.addLayout(self.horizontalLayout_24)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_31)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.username = QLineEdit(self.login)
        self.username.setObjectName(u"username")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.username.sizePolicy().hasHeightForWidth())
        self.username.setSizePolicy(sizePolicy)
        self.username.setMinimumSize(QSize(0, 0))
        self.username.setStyleSheet(u"font-size: 20px; background-color: white; ")

        self.gridLayout_4.addWidget(self.username, 0, 0, 1, 1)

        self.verticalSpacer_15 = QSpacerItem(18, 28, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_15, 0, 1, 1, 1)

        self.password = QLineEdit(self.login)
        self.password.setObjectName(u"password")
        sizePolicy.setHeightForWidth(self.password.sizePolicy().hasHeightForWidth())
        self.password.setSizePolicy(sizePolicy)
        self.password.setStyleSheet(u"font-size: 20px; background-color: white;")
        self.password.setEchoMode(QLineEdit.Password)

        self.gridLayout_4.addWidget(self.password, 1, 0, 1, 1)

        self.show_password_button = QPushButton(self.login)
        self.show_password_button.setObjectName(u"show_password_button")
        icon = QIcon()
        icon.addFile(u":/static/eye.png", QSize(), QIcon.Normal, QIcon.Off)
        self.show_password_button.setIcon(icon)
        self.show_password_button.setIconSize(QSize(25, 25))

        self.gridLayout_4.addWidget(self.show_password_button, 1, 1, 1, 1)


        self.horizontalLayout_22.addLayout(self.gridLayout_4)

        self.horizontalSpacer_32 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_32)


        self.verticalLayout_16.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalSpacer_35 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_35)

        self.loginButton = QPushButton(self.login)
        self.loginButton.setObjectName(u"loginButton")
        self.loginButton.setStyleSheet(u"QPushButton#loginButton {\n"
"	background-color: #EE99F3; \n"
"	color: black;\n"
"	padding: 10px; 	\n"
"	border-radius: 10px; \n"
"    border-style: outset;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#loginButton:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_21.addWidget(self.loginButton)

        self.horizontalSpacer_36 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_21.addItem(self.horizontalSpacer_36)


        self.verticalLayout_16.addLayout(self.horizontalLayout_21)

        self.verticalSpacer_3 = QSpacerItem(20, 103, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_16.addItem(self.verticalSpacer_3)

        self.stackedWidget.addWidget(self.login)
        self.Home_Page_Doctor = QWidget()
        self.Home_Page_Doctor.setObjectName(u"Home_Page_Doctor")
        self.verticalLayout_87 = QVBoxLayout(self.Home_Page_Doctor)
        self.verticalLayout_87.setSpacing(0)
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.verticalLayout_87.setContentsMargins(0, 0, 0, 0)
        self.widget_17 = QWidget(self.Home_Page_Doctor)
        self.widget_17.setObjectName(u"widget_17")
        self.verticalLayout_86 = QVBoxLayout(self.widget_17)
        self.verticalLayout_86.setSpacing(0)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_86.setContentsMargins(0, 0, 0, 0)
        self.main_widget_3 = QWidget(self.widget_17)
        self.main_widget_3.setObjectName(u"main_widget_3")
        self.verticalLayout_85 = QVBoxLayout(self.main_widget_3)
        self.verticalLayout_85.setSpacing(7)
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.verticalLayout_85.setContentsMargins(0, 0, 0, 0)
        self.header_widget_6 = QWidget(self.main_widget_3)
        self.header_widget_6.setObjectName(u"header_widget_6")
        self.header_widget_6.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"}")
        self.horizontalLayout_112 = QHBoxLayout(self.header_widget_6)
        self.horizontalLayout_112.setSpacing(7)
        self.horizontalLayout_112.setObjectName(u"horizontalLayout_112")
        self.horizontalLayout_112.setContentsMargins(12, 12, 12, -1)
        self.horizontalSpacer_152 = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_112.addItem(self.horizontalSpacer_152)

        self.Username_6 = QLabel(self.header_widget_6)
        self.Username_6.setObjectName(u"Username_6")

        self.horizontalLayout_112.addWidget(self.Username_6)

        self.doctor_setting_button = QPushButton(self.header_widget_6)
        self.doctor_setting_button.setObjectName(u"doctor_setting_button")
        icon1 = QIcon()
        icon1.addFile(u":/static/icons8-user-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.doctor_setting_button.setIcon(icon1)
        self.doctor_setting_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_112.addWidget(self.doctor_setting_button)


        self.verticalLayout_85.addWidget(self.header_widget_6)

        self.scrollArea_6 = QScrollArea(self.main_widget_3)
        self.scrollArea_6.setObjectName(u"scrollArea_6")
        self.scrollArea_6.setMaximumSize(QSize(1280, 10000))
        self.scrollArea_6.setWidgetResizable(True)
        self.scrollAreaWidgetContents_6 = QWidget()
        self.scrollAreaWidgetContents_6.setObjectName(u"scrollAreaWidgetContents_6")
        self.scrollAreaWidgetContents_6.setGeometry(QRect(0, 0, 825, 432))
        self.scrollAreaWidgetContents_6.setMaximumSize(QSize(1280, 16777215))
        self.verticalLayout_72 = QVBoxLayout(self.scrollAreaWidgetContents_6)
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_6)

        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalSpacer_38 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_38)

        self.label_8 = QLabel(self.scrollAreaWidgetContents_6)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(48)
        self.label_8.setFont(font)

        self.horizontalLayout_28.addWidget(self.label_8)

        self.horizontalSpacer_39 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_28.addItem(self.horizontalSpacer_39)


        self.verticalLayout_72.addLayout(self.horizontalLayout_28)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_4)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.widget_3 = QWidget(self.scrollAreaWidgetContents_6)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_33 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.home_patient_icon = QPushButton(self.widget_3)
        self.home_patient_icon.setObjectName(u"home_patient_icon")
        icon2 = QIcon()
        icon2.addFile(u":/static/Patient_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_patient_icon.setIcon(icon2)
        self.home_patient_icon.setIconSize(QSize(130, 130))

        self.verticalLayout_21.addWidget(self.home_patient_icon)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        font1 = QFont()
        font1.setBold(False)
        font1.setItalic(False)
        self.label_10.setFont(font1)
        self.label_10.setStyleSheet(u"font: 14px;")

        self.verticalLayout_21.addWidget(self.label_10, 0, Qt.AlignHCenter)


        self.horizontalLayout_33.addLayout(self.verticalLayout_21)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.home_lab_icon = QPushButton(self.widget_3)
        self.home_lab_icon.setObjectName(u"home_lab_icon")
        icon3 = QIcon()
        icon3.addFile(u":/static/report_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_lab_icon.setIcon(icon3)
        self.home_lab_icon.setIconSize(QSize(130, 130))

        self.verticalLayout_64.addWidget(self.home_lab_icon)

        self.label_72 = QLabel(self.widget_3)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setStyleSheet(u"font: 14px;")
        self.label_72.setAlignment(Qt.AlignCenter)

        self.verticalLayout_64.addWidget(self.label_72)


        self.horizontalLayout_33.addLayout(self.verticalLayout_64)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.home_report_icon = QPushButton(self.widget_3)
        self.home_report_icon.setObjectName(u"home_report_icon")
        icon4 = QIcon()
        icon4.addFile(u":/static/Report_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_report_icon.setIcon(icon4)
        self.home_report_icon.setIconSize(QSize(130, 130))

        self.verticalLayout_27.addWidget(self.home_report_icon)

        self.label_16 = QLabel(self.widget_3)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font1)
        self.label_16.setStyleSheet(u"font: 14px;")

        self.verticalLayout_27.addWidget(self.label_16, 0, Qt.AlignHCenter)


        self.horizontalLayout_33.addLayout(self.verticalLayout_27)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.bill_list_icon = QPushButton(self.widget_3)
        self.bill_list_icon.setObjectName(u"bill_list_icon")
        icon5 = QIcon()
        icon5.addFile(u":/static/bill_black.png", QSize(), QIcon.Normal, QIcon.Off)
        self.bill_list_icon.setIcon(icon5)
        self.bill_list_icon.setIconSize(QSize(130, 130))

        self.verticalLayout_19.addWidget(self.bill_list_icon)

        self.label_108 = QLabel(self.widget_3)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setStyleSheet(u"font: 14px;")
        self.label_108.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_108)


        self.horizontalLayout_33.addLayout(self.verticalLayout_19)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.home_schedule_icon = QPushButton(self.widget_3)
        self.home_schedule_icon.setObjectName(u"home_schedule_icon")
        icon6 = QIcon()
        icon6.addFile(u":/static/Schedule_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_schedule_icon.setIcon(icon6)
        self.home_schedule_icon.setIconSize(QSize(130, 130))

        self.verticalLayout_26.addWidget(self.home_schedule_icon)

        self.label_15 = QLabel(self.widget_3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"font: 14px;")

        self.verticalLayout_26.addWidget(self.label_15, 0, Qt.AlignHCenter)


        self.horizontalLayout_33.addLayout(self.verticalLayout_26)


        self.horizontalLayout_29.addWidget(self.widget_3)


        self.verticalLayout_72.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalSpacer_86 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_86)

        self.logout_button_4 = QPushButton(self.scrollAreaWidgetContents_6)
        self.logout_button_4.setObjectName(u"logout_button_4")
        self.logout_button_4.setStyleSheet(u"QPushButton#logout_button_4 {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#logout_button_4:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_31.addWidget(self.logout_button_4)

        self.horizontalSpacer_87 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_31.addItem(self.horizontalSpacer_87)


        self.verticalLayout_72.addLayout(self.horizontalLayout_31)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_72.addItem(self.verticalSpacer_5)

        self.scrollArea_6.setWidget(self.scrollAreaWidgetContents_6)

        self.verticalLayout_85.addWidget(self.scrollArea_6)


        self.verticalLayout_86.addWidget(self.main_widget_3)


        self.verticalLayout_87.addWidget(self.widget_17)

        self.stackedWidget.addWidget(self.Home_Page_Doctor)
        self.Home_Page_Patient = QWidget()
        self.Home_Page_Patient.setObjectName(u"Home_Page_Patient")
        self.verticalLayout_17 = QVBoxLayout(self.Home_Page_Patient)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.Home_Page_Patient)
        self.widget_2.setObjectName(u"widget_2")
        self.verticalLayout_24 = QVBoxLayout(self.widget_2)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.header_widget_7 = QWidget(self.widget_2)
        self.header_widget_7.setObjectName(u"header_widget_7")
        self.header_widget_7.setMinimumSize(QSize(0, 65))
        self.header_widget_7.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"}")
        self.horizontalLayout_113 = QHBoxLayout(self.header_widget_7)
        self.horizontalLayout_113.setSpacing(10)
        self.horizontalLayout_113.setObjectName(u"horizontalLayout_113")
        self.horizontalLayout_113.setContentsMargins(0, 0, 10, 0)
        self.horizontalSpacer_153 = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_113.addItem(self.horizontalSpacer_153)

        self.Username_7 = QLabel(self.header_widget_7)
        self.Username_7.setObjectName(u"Username_7")

        self.horizontalLayout_113.addWidget(self.Username_7)

        self.userprofile_pic_7 = QPushButton(self.header_widget_7)
        self.userprofile_pic_7.setObjectName(u"userprofile_pic_7")
        self.userprofile_pic_7.setIcon(icon1)
        self.userprofile_pic_7.setIconSize(QSize(40, 40))

        self.horizontalLayout_113.addWidget(self.userprofile_pic_7)


        self.verticalLayout_24.addWidget(self.header_widget_7)

        self.scrollArea_7 = QScrollArea(self.widget_2)
        self.scrollArea_7.setObjectName(u"scrollArea_7")
        self.scrollArea_7.setMaximumSize(QSize(1280, 10000))
        self.scrollArea_7.setWidgetResizable(True)
        self.scrollAreaWidgetContents_7 = QWidget()
        self.scrollAreaWidgetContents_7.setObjectName(u"scrollAreaWidgetContents_7")
        self.scrollAreaWidgetContents_7.setGeometry(QRect(0, 0, 825, 435))
        self.scrollAreaWidgetContents_7.setMaximumSize(QSize(1280, 16777215))
        self.verticalLayout_20 = QVBoxLayout(self.scrollAreaWidgetContents_7)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalSpacer_7 = QSpacerItem(779, 66, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_7)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalSpacer_40 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_40)

        self.label_18 = QLabel(self.scrollAreaWidgetContents_7)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font)

        self.horizontalLayout_30.addWidget(self.label_18)

        self.horizontalSpacer_41 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_41)


        self.verticalLayout_20.addLayout(self.horizontalLayout_30)

        self.verticalSpacer_8 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_8)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.widget_4 = QWidget(self.scrollAreaWidgetContents_7)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_35 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.patient_record_icon = QPushButton(self.widget_4)
        self.patient_record_icon.setObjectName(u"patient_record_icon")
        icon7 = QIcon()
        icon7.addFile(u":/static/Record_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patient_record_icon.setIcon(icon7)
        self.patient_record_icon.setIconSize(QSize(150, 150))

        self.verticalLayout_23.addWidget(self.patient_record_icon)

        self.label_19 = QLabel(self.widget_4)
        self.label_19.setObjectName(u"label_19")
        font2 = QFont()
        font2.setPointSize(14)
        self.label_19.setFont(font2)
        self.label_19.setStyleSheet(u"")

        self.verticalLayout_23.addWidget(self.label_19, 0, Qt.AlignHCenter)


        self.horizontalLayout_35.addLayout(self.verticalLayout_23)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.patient_appointment_icon = QPushButton(self.widget_4)
        self.patient_appointment_icon.setObjectName(u"patient_appointment_icon")
        self.patient_appointment_icon.setIcon(icon6)
        self.patient_appointment_icon.setIconSize(QSize(150, 150))

        self.verticalLayout_29.addWidget(self.patient_appointment_icon)

        self.label_20 = QLabel(self.widget_4)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.verticalLayout_29.addWidget(self.label_20, 0, Qt.AlignHCenter)


        self.horizontalLayout_35.addLayout(self.verticalLayout_29)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.patient_payment_icon = QPushButton(self.widget_4)
        self.patient_payment_icon.setObjectName(u"patient_payment_icon")
        icon8 = QIcon()
        icon8.addFile(u":/static/Payment_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patient_payment_icon.setIcon(icon8)
        self.patient_payment_icon.setIconSize(QSize(150, 150))

        self.verticalLayout_30.addWidget(self.patient_payment_icon)

        self.label_21 = QLabel(self.widget_4)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font2)

        self.verticalLayout_30.addWidget(self.label_21, 0, Qt.AlignHCenter)


        self.horizontalLayout_35.addLayout(self.verticalLayout_30)


        self.horizontalLayout_34.addWidget(self.widget_4)


        self.verticalLayout_20.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalSpacer_88 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_88)

        self.logout_button_3 = QPushButton(self.scrollAreaWidgetContents_7)
        self.logout_button_3.setObjectName(u"logout_button_3")
        self.logout_button_3.setStyleSheet(u"QPushButton#logout_button_3 {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#logout_button_3:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_32.addWidget(self.logout_button_3)

        self.horizontalSpacer_89 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_32.addItem(self.horizontalSpacer_89)


        self.verticalLayout_20.addLayout(self.horizontalLayout_32)

        self.verticalSpacer_9 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_20.addItem(self.verticalSpacer_9)

        self.scrollArea_7.setWidget(self.scrollAreaWidgetContents_7)

        self.verticalLayout_24.addWidget(self.scrollArea_7)


        self.verticalLayout_17.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.Home_Page_Patient)
        self.doctor_sidebar = QWidget()
        self.doctor_sidebar.setObjectName(u"doctor_sidebar")
        self.horizontalLayout_19 = QHBoxLayout(self.doctor_sidebar)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.icon_name_widget = QWidget(self.doctor_sidebar)
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
        self.verticalLayout.setSpacing(7)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 12, 0, 12)
        self.menu_icon = QPushButton(self.icon_name_widget)
        self.menu_icon.setObjectName(u"menu_icon")
        self.menu_icon.setMinimumSize(QSize(50, 50))
        icon9 = QIcon()
        icon9.addFile(u":/static/medical-team.png", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_icon.setIcon(icon9)
        self.menu_icon.setIconSize(QSize(50, 50))

        self.verticalLayout.addWidget(self.menu_icon)

        self.home_Button = QPushButton(self.icon_name_widget)
        self.home_Button.setObjectName(u"home_Button")
        self.home_Button.setMinimumSize(QSize(40, 40))
        icon10 = QIcon()
        icon10.addFile(u":/static/icons8-home-48.png", QSize(), QIcon.Normal, QIcon.Off)
        self.home_Button.setIcon(icon10)
        self.home_Button.setIconSize(QSize(40, 40))
        self.home_Button.setCheckable(False)
        self.home_Button.setAutoExclusive(False)

        self.verticalLayout.addWidget(self.home_Button)

        self.patientListButton = QPushButton(self.icon_name_widget)
        self.patientListButton.setObjectName(u"patientListButton")
        self.patientListButton.setMinimumSize(QSize(40, 40))
        icon11 = QIcon()
        icon11.addFile(u":/static/icons8-list-64.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patientListButton.setIcon(icon11)
        self.patientListButton.setIconSize(QSize(40, 40))
        self.patientListButton.setCheckable(True)
        self.patientListButton.setChecked(True)
        self.patientListButton.setAutoRepeat(False)
        self.patientListButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.patientListButton)

        self.labButton = QPushButton(self.icon_name_widget)
        self.labButton.setObjectName(u"labButton")
        self.labButton.setMinimumSize(QSize(40, 40))
        icon12 = QIcon()
        icon12.addFile(u":/static/lab_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.labButton.setIcon(icon12)
        self.labButton.setIconSize(QSize(40, 40))
        self.labButton.setCheckable(True)
        self.labButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.labButton)

        self.reportButton = QPushButton(self.icon_name_widget)
        self.reportButton.setObjectName(u"reportButton")
        self.reportButton.setMinimumSize(QSize(40, 40))
        icon13 = QIcon()
        icon13.addFile(u":/static/White_Report.png", QSize(), QIcon.Normal, QIcon.Off)
        self.reportButton.setIcon(icon13)
        self.reportButton.setIconSize(QSize(40, 40))
        self.reportButton.setCheckable(True)
        self.reportButton.setChecked(False)
        self.reportButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.reportButton)

        self.billButton = QPushButton(self.icon_name_widget)
        self.billButton.setObjectName(u"billButton")
        self.billButton.setMinimumSize(QSize(40, 40))
        icon14 = QIcon()
        icon14.addFile(u":/static/bill_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.billButton.setIcon(icon14)
        self.billButton.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.billButton)

        self.scheduleButton = QPushButton(self.icon_name_widget)
        self.scheduleButton.setObjectName(u"scheduleButton")
        self.scheduleButton.setMinimumSize(QSize(40, 40))
        icon15 = QIcon()
        icon15.addFile(u":/static/icons8-schedule-100.png", QSize(), QIcon.Normal, QIcon.Off)
        self.scheduleButton.setIcon(icon15)
        self.scheduleButton.setIconSize(QSize(40, 40))
        self.scheduleButton.setCheckable(True)
        self.scheduleButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.scheduleButton)

        self.verticalSpacer_2 = QSpacerItem(20, 111, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.logout_button = QPushButton(self.icon_name_widget)
        self.logout_button.setObjectName(u"logout_button")
        self.logout_button.setMinimumSize(QSize(40, 40))
        icon16 = QIcon()
        icon16.addFile(u":/static/log_out.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_button.setIcon(icon16)
        self.logout_button.setIconSize(QSize(40, 40))

        self.verticalLayout.addWidget(self.logout_button)


        self.horizontalLayout_19.addWidget(self.icon_name_widget)

        self.main_widget = QWidget(self.doctor_sidebar)
        self.main_widget.setObjectName(u"main_widget")
        self.verticalLayout_2 = QVBoxLayout(self.main_widget)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.header_widget = QWidget(self.main_widget)
        self.header_widget.setObjectName(u"header_widget")
        self.header_widget.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"}")
        self.horizontalLayout_3 = QHBoxLayout(self.header_widget)
        self.horizontalLayout_3.setSpacing(7)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(12, 12, 12, -1)
        self.horizontalSpacer_2 = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.Username = QLabel(self.header_widget)
        self.Username.setObjectName(u"Username")

        self.horizontalLayout_3.addWidget(self.Username)

        self.doctor_setting_button_2 = QPushButton(self.header_widget)
        self.doctor_setting_button_2.setObjectName(u"doctor_setting_button_2")
        self.doctor_setting_button_2.setIcon(icon1)
        self.doctor_setting_button_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_3.addWidget(self.doctor_setting_button_2)


        self.verticalLayout_2.addWidget(self.header_widget)

        self.scrollArea = QScrollArea(self.main_widget)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"\n"
"\n"
"")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 744, 1724))
        self.horizontalLayout_2 = QHBoxLayout(self.scrollAreaWidgetContents)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_2 = QStackedWidget(self.scrollAreaWidgetContents)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setMinimumSize(QSize(0, 0))
        self.patientList_page = QWidget()
        self.patientList_page.setObjectName(u"patientList_page")
        self.verticalLayout_3 = QVBoxLayout(self.patientList_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_79 = QLabel(self.patientList_page)
        self.label_79.setObjectName(u"label_79")

        self.horizontalLayout.addWidget(self.label_79)

        self.lineEdit_search = QLineEdit(self.patientList_page)
        self.lineEdit_search.setObjectName(u"lineEdit_search")
        self.lineEdit_search.setMinimumSize(QSize(200, 0))
        self.lineEdit_search.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")

        self.horizontalLayout.addWidget(self.lineEdit_search)

        self.searchButton = QPushButton(self.patientList_page)
        self.searchButton.setObjectName(u"searchButton")
        self.searchButton.setStyleSheet(u"background-color: transparent;\n"
"border: none;\n"
"border-radius: 10px;")
        icon17 = QIcon()
        icon17.addFile(u":/static/19.png", QSize(), QIcon.Normal, QIcon.Off)
        self.searchButton.setIcon(icon17)
        self.searchButton.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.searchButton)

        self.horizontalSpacer_24 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_24)

        self.AddPatientButton = QPushButton(self.patientList_page)
        self.AddPatientButton.setObjectName(u"AddPatientButton")
        self.AddPatientButton.setStyleSheet(u"QPushButton#AddPatientButton {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#AddPatientButton:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.AddPatientButton)

        self.view_patient_info_button = QPushButton(self.patientList_page)
        self.view_patient_info_button.setObjectName(u"view_patient_info_button")
        self.view_patient_info_button.setStyleSheet(u"QPushButton#view_patient_info_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#view_patient_info_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.view_patient_info_button)

        self.edit_patient_info_button = QPushButton(self.patientList_page)
        self.edit_patient_info_button.setObjectName(u"edit_patient_info_button")
        self.edit_patient_info_button.setStyleSheet(u"QPushButton#edit_patient_info_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#edit_patient_info_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout.addWidget(self.edit_patient_info_button)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.patient_list_table = QTableWidget(self.patientList_page)
        if (self.patient_list_table.columnCount() < 2):
            self.patient_list_table.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.patient_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.patient_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        self.patient_list_table.setObjectName(u"patient_list_table")
        self.patient_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.patient_list_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.patient_list_table.horizontalHeader().setDefaultSectionSize(150)
        self.patient_list_table.horizontalHeader().setStretchLastSection(True)
        self.patient_list_table.verticalHeader().setVisible(False)
        self.patient_list_table.verticalHeader().setMinimumSectionSize(30)
        self.patient_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_3.addWidget(self.patient_list_table)

        self.stackedWidget_2.addWidget(self.patientList_page)
        self.add_patient_page = QWidget()
        self.add_patient_page.setObjectName(u"add_patient_page")
        self.verticalLayout_59 = QVBoxLayout(self.add_patient_page)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.horizontalSpacer_52 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_52)

        self.label_41 = QLabel(self.add_patient_page)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_66.addWidget(self.label_41)

        self.horizontalSpacer_74 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_66.addItem(self.horizontalSpacer_74)


        self.verticalLayout_59.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_81 = QHBoxLayout()
        self.horizontalLayout_81.setObjectName(u"horizontalLayout_81")
        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.upload_photo = QLabel(self.add_patient_page)
        self.upload_photo.setObjectName(u"upload_photo")
        self.upload_photo.setMinimumSize(QSize(100, 100))
        self.upload_photo.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_54.addWidget(self.upload_photo)

        self.take_pic_button = QPushButton(self.add_patient_page)
        self.take_pic_button.setObjectName(u"take_pic_button")
        self.take_pic_button.setStyleSheet(u"QPushButton#take_pic_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#take_pic_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_54.addWidget(self.take_pic_button)

        self.browse_page = QPushButton(self.add_patient_page)
        self.browse_page.setObjectName(u"browse_page")
        self.browse_page.setStyleSheet(u"QPushButton#browse_page {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#browse_page:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_54.addWidget(self.browse_page)


        self.horizontalLayout_81.addLayout(self.verticalLayout_54)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.label_42 = QLabel(self.add_patient_page)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_67.addWidget(self.label_42)

        self.firstName_2 = QLineEdit(self.add_patient_page)
        self.firstName_2.setObjectName(u"firstName_2")
        self.firstName_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_67.addWidget(self.firstName_2)


        self.verticalLayout_36.addLayout(self.horizontalLayout_67)

        self.horizontalLayout_76 = QHBoxLayout()
        self.horizontalLayout_76.setObjectName(u"horizontalLayout_76")
        self.label_55 = QLabel(self.add_patient_page)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_76.addWidget(self.label_55)

        self.middleName_2 = QLineEdit(self.add_patient_page)
        self.middleName_2.setObjectName(u"middleName_2")
        self.middleName_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_76.addWidget(self.middleName_2)


        self.verticalLayout_36.addLayout(self.horizontalLayout_76)

        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_43 = QLabel(self.add_patient_page)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_68.addWidget(self.label_43)

        self.lastName_2 = QLineEdit(self.add_patient_page)
        self.lastName_2.setObjectName(u"lastName_2")
        self.lastName_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_68.addWidget(self.lastName_2)


        self.verticalLayout_36.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_160 = QHBoxLayout()
        self.horizontalLayout_160.setObjectName(u"horizontalLayout_160")
        self.label_111 = QLabel(self.add_patient_page)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_160.addWidget(self.label_111)

        self.patient_email = QLineEdit(self.add_patient_page)
        self.patient_email.setObjectName(u"patient_email")
        self.patient_email.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_160.addWidget(self.patient_email)


        self.verticalLayout_36.addLayout(self.horizontalLayout_160)

        self.horizontalLayout_77 = QHBoxLayout()
        self.horizontalLayout_77.setObjectName(u"horizontalLayout_77")
        self.label_56 = QLabel(self.add_patient_page)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_77.addWidget(self.label_56)

        self.passwordID = QLineEdit(self.add_patient_page)
        self.passwordID.setObjectName(u"passwordID")
        self.passwordID.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_77.addWidget(self.passwordID)


        self.verticalLayout_36.addLayout(self.horizontalLayout_77)


        self.horizontalLayout_81.addLayout(self.verticalLayout_36)


        self.verticalLayout_59.addLayout(self.horizontalLayout_81)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_44 = QLabel(self.add_patient_page)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setStyleSheet(u"font:18pt;")

        self.verticalLayout_13.addWidget(self.label_44)

        self.label_46 = QLabel(self.add_patient_page)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setStyleSheet(u"font:18pt;")

        self.verticalLayout_13.addWidget(self.label_46)


        self.horizontalLayout_69.addLayout(self.verticalLayout_13)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.date_of_birth = QDateEdit(self.add_patient_page)
        self.date_of_birth.setObjectName(u"date_of_birth")
        self.date_of_birth.setMinimumSize(QSize(100, 0))
        self.date_of_birth.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_51.addWidget(self.date_of_birth)

        self.weight = QLineEdit(self.add_patient_page)
        self.weight.setObjectName(u"weight")
        self.weight.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_51.addWidget(self.weight)


        self.horizontalLayout_69.addLayout(self.verticalLayout_51)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_45 = QLabel(self.add_patient_page)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setStyleSheet(u"font:18pt;\n"
"")

        self.verticalLayout_52.addWidget(self.label_45)

        self.label_47 = QLabel(self.add_patient_page)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setStyleSheet(u"font:18pt;")

        self.verticalLayout_52.addWidget(self.label_47)


        self.horizontalLayout_69.addLayout(self.verticalLayout_52)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.sex = QComboBox(self.add_patient_page)
        self.sex.addItem("")
        self.sex.addItem("")
        self.sex.setObjectName(u"sex")
        self.sex.setMinimumSize(QSize(100, 0))
        self.sex.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.sex)

        self.height = QLineEdit(self.add_patient_page)
        self.height.setObjectName(u"height")
        self.height.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_53.addWidget(self.height)


        self.horizontalLayout_69.addLayout(self.verticalLayout_53)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.label_54 = QLabel(self.add_patient_page)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setStyleSheet(u"font:18pt;")

        self.verticalLayout_55.addWidget(self.label_54)

        self.label_59 = QLabel(self.add_patient_page)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"font:18pt;")

        self.verticalLayout_55.addWidget(self.label_59)


        self.horizontalLayout_69.addLayout(self.verticalLayout_55)

        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.blood_type = QComboBox(self.add_patient_page)
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.addItem("")
        self.blood_type.setObjectName(u"blood_type")
        self.blood_type.setMinimumSize(QSize(100, 0))
        self.blood_type.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_58.addWidget(self.blood_type)

        self.blood_pressure = QLineEdit(self.add_patient_page)
        self.blood_pressure.setObjectName(u"blood_pressure")
        self.blood_pressure.setMinimumSize(QSize(0, 0))
        self.blood_pressure.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_58.addWidget(self.blood_pressure)


        self.horizontalLayout_69.addLayout(self.verticalLayout_58)


        self.verticalLayout_59.addLayout(self.horizontalLayout_69)

        self.horizontalLayout_85 = QHBoxLayout()
        self.horizontalLayout_85.setObjectName(u"horizontalLayout_85")
        self.horizontalLayout_83 = QHBoxLayout()
        self.horizontalLayout_83.setObjectName(u"horizontalLayout_83")
        self.horizontalLayout_84 = QHBoxLayout()
        self.horizontalLayout_84.setObjectName(u"horizontalLayout_84")
        self.label_48 = QLabel(self.add_patient_page)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_84.addWidget(self.label_48)

        self.hn_no = QLineEdit(self.add_patient_page)
        self.hn_no.setObjectName(u"hn_no")
        self.hn_no.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_84.addWidget(self.hn_no)


        self.horizontalLayout_83.addLayout(self.horizontalLayout_84)

        self.label_9 = QLabel(self.add_patient_page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_83.addWidget(self.label_9)

        self.tel = QLineEdit(self.add_patient_page)
        self.tel.setObjectName(u"tel")
        self.tel.setMinimumSize(QSize(0, 0))
        self.tel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_83.addWidget(self.tel)


        self.horizontalLayout_85.addLayout(self.horizontalLayout_83)


        self.verticalLayout_59.addLayout(self.horizontalLayout_85)

        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_17 = QLabel(self.add_patient_page)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setStyleSheet(u"font:18pt;")

        self.verticalLayout_60.addWidget(self.label_17)

        self.address = QTextEdit(self.add_patient_page)
        self.address.setObjectName(u"address")
        self.address.setMinimumSize(QSize(0, 50))
        self.address.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_60.addWidget(self.address)


        self.verticalLayout_59.addLayout(self.verticalLayout_60)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.label_49 = QLabel(self.add_patient_page)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_70.addWidget(self.label_49)

        self.horizontalSpacer_79 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_79)


        self.verticalLayout_59.addLayout(self.horizontalLayout_70)

        self.vaccine_list_table = QTableWidget(self.add_patient_page)
        if (self.vaccine_list_table.columnCount() < 2):
            self.vaccine_list_table.setColumnCount(2)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.vaccine_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.vaccine_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem3)
        self.vaccine_list_table.setObjectName(u"vaccine_list_table")
        self.vaccine_list_table.setMinimumSize(QSize(0, 300))
        self.vaccine_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.vaccine_list_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.vaccine_list_table.setShowGrid(True)
        self.vaccine_list_table.setGridStyle(Qt.SolidLine)
        self.vaccine_list_table.horizontalHeader().setVisible(True)
        self.vaccine_list_table.horizontalHeader().setCascadingSectionResizes(False)
        self.vaccine_list_table.horizontalHeader().setDefaultSectionSize(300)
        self.vaccine_list_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.vaccine_list_table.horizontalHeader().setStretchLastSection(True)
        self.vaccine_list_table.verticalHeader().setVisible(False)
        self.vaccine_list_table.verticalHeader().setCascadingSectionResizes(False)
        self.vaccine_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_59.addWidget(self.vaccine_list_table)

        self.horizontalLayout_71 = QHBoxLayout()
        self.horizontalLayout_71.setObjectName(u"horizontalLayout_71")
        self.horizontalSpacer_77 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_77)

        self.add_vaccine_button = QPushButton(self.add_patient_page)
        self.add_vaccine_button.setObjectName(u"add_vaccine_button")
        self.add_vaccine_button.setStyleSheet(u"QPushButton#add_vaccine_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#add_vaccine_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_71.addWidget(self.add_vaccine_button)

        self.delete_vaccine_button = QPushButton(self.add_patient_page)
        self.delete_vaccine_button.setObjectName(u"delete_vaccine_button")
        self.delete_vaccine_button.setStyleSheet(u"QPushButton#delete_vaccine_button {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#delete_vaccine_button:hover {\n"
"    background-color:white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_71.addWidget(self.delete_vaccine_button)

        self.horizontalSpacer_78 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_71.addItem(self.horizontalSpacer_78)


        self.verticalLayout_59.addLayout(self.horizontalLayout_71)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.label_50 = QLabel(self.add_patient_page)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_73.addWidget(self.label_50)

        self.horizontalSpacer_80 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_80)


        self.verticalLayout_59.addLayout(self.horizontalLayout_73)

        self.medication_list_table = QTableWidget(self.add_patient_page)
        if (self.medication_list_table.columnCount() < 8):
            self.medication_list_table.setColumnCount(8)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.medication_list_table.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        self.medication_list_table.setObjectName(u"medication_list_table")
        self.medication_list_table.setMinimumSize(QSize(0, 300))
        self.medication_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.medication_list_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.medication_list_table.horizontalHeader().setCascadingSectionResizes(False)
        self.medication_list_table.horizontalHeader().setDefaultSectionSize(200)
        self.medication_list_table.horizontalHeader().setStretchLastSection(True)
        self.medication_list_table.verticalHeader().setVisible(False)
        self.medication_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_59.addWidget(self.medication_list_table)

        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.horizontalSpacer_81 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_81)

        self.add_medication_button = QPushButton(self.add_patient_page)
        self.add_medication_button.setObjectName(u"add_medication_button")
        self.add_medication_button.setStyleSheet(u"QPushButton#add_medication_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#add_medication_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_72.addWidget(self.add_medication_button)

        self.delete_medication_button = QPushButton(self.add_patient_page)
        self.delete_medication_button.setObjectName(u"delete_medication_button")
        self.delete_medication_button.setStyleSheet(u"QPushButton#delete_medication_button {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#delete_medication_button:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_72.addWidget(self.delete_medication_button)

        self.horizontalSpacer_82 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_82)


        self.verticalLayout_59.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_75 = QHBoxLayout()
        self.horizontalLayout_75.setObjectName(u"horizontalLayout_75")
        self.label_51 = QLabel(self.add_patient_page)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setStyleSheet(u"font:18pt;")

        self.horizontalLayout_75.addWidget(self.label_51)

        self.horizontalSpacer_83 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_75.addItem(self.horizontalSpacer_83)


        self.verticalLayout_59.addLayout(self.horizontalLayout_75)

        self.allergy_list_table = QTableWidget(self.add_patient_page)
        if (self.allergy_list_table.columnCount() < 1):
            self.allergy_list_table.setColumnCount(1)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.allergy_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem12)
        self.allergy_list_table.setObjectName(u"allergy_list_table")
        self.allergy_list_table.setMinimumSize(QSize(0, 300))
        self.allergy_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.allergy_list_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.allergy_list_table.horizontalHeader().setStretchLastSection(True)
        self.allergy_list_table.verticalHeader().setVisible(False)
        self.allergy_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_59.addWidget(self.allergy_list_table)

        self.horizontalLayout_74 = QHBoxLayout()
        self.horizontalLayout_74.setObjectName(u"horizontalLayout_74")
        self.horizontalSpacer_84 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_84)

        self.add_allergy_button = QPushButton(self.add_patient_page)
        self.add_allergy_button.setObjectName(u"add_allergy_button")
        self.add_allergy_button.setStyleSheet(u"QPushButton#add_allergy_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#add_allergy_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_74.addWidget(self.add_allergy_button)

        self.delete_allergy_button = QPushButton(self.add_patient_page)
        self.delete_allergy_button.setObjectName(u"delete_allergy_button")
        self.delete_allergy_button.setStyleSheet(u"QPushButton#delete_allergy_button {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#delete_allergy_button:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_74.addWidget(self.delete_allergy_button)

        self.horizontalSpacer_85 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_74.addItem(self.horizontalSpacer_85)


        self.verticalLayout_59.addLayout(self.horizontalLayout_74)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalSpacer_33 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_33)

        self.confirm_button_2 = QPushButton(self.add_patient_page)
        self.confirm_button_2.setObjectName(u"confirm_button_2")
        self.confirm_button_2.setStyleSheet(u"QPushButton#confirm_button_2 {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_button_2:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_23.addWidget(self.confirm_button_2)

        self.cancel_button_2 = QPushButton(self.add_patient_page)
        self.cancel_button_2.setObjectName(u"cancel_button_2")
        self.cancel_button_2.setMouseTracking(True)
        self.cancel_button_2.setStyleSheet(u"QPushButton#cancel_button_2 {\n"
"	background-color:black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#cancel_button_2:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_23.addWidget(self.cancel_button_2)

        self.horizontalSpacer_34 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_34)


        self.verticalLayout_59.addLayout(self.horizontalLayout_23)

        self.stackedWidget_2.addWidget(self.add_patient_page)
        self.lab_page = QWidget()
        self.lab_page.setObjectName(u"lab_page")
        self.verticalLayout_63 = QVBoxLayout(self.lab_page)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.horizontalLayout_107 = QHBoxLayout()
        self.horizontalLayout_107.setObjectName(u"horizontalLayout_107")
        self.horizontalSpacer_120 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_120)

        self.label_74 = QLabel(self.lab_page)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_107.addWidget(self.label_74)

        self.horizontalSpacer_121 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_107.addItem(self.horizontalSpacer_121)


        self.verticalLayout_63.addLayout(self.horizontalLayout_107)

        self.horizontalLayout_105 = QHBoxLayout()
        self.horizontalLayout_105.setObjectName(u"horizontalLayout_105")
        self.view_received_replies = QPushButton(self.lab_page)
        self.view_received_replies.setObjectName(u"view_received_replies")
        self.view_received_replies.setStyleSheet(u"QPushButton#view_received_replies {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#view_received_replies:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_105.addWidget(self.view_received_replies)

        self.horizontalSpacer_119 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_105.addItem(self.horizontalSpacer_119)

        self.make_lab_request_button = QPushButton(self.lab_page)
        self.make_lab_request_button.setObjectName(u"make_lab_request_button")
        self.make_lab_request_button.setStyleSheet(u"QPushButton#make_lab_request_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#make_lab_request_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_105.addWidget(self.make_lab_request_button)

        self.make_lab_reply_button = QPushButton(self.lab_page)
        self.make_lab_reply_button.setObjectName(u"make_lab_reply_button")
        self.make_lab_reply_button.setStyleSheet(u"QPushButton#make_lab_reply_button {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#make_lab_reply_button:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_105.addWidget(self.make_lab_reply_button)


        self.verticalLayout_63.addLayout(self.horizontalLayout_105)

        self.lab_requests_table = QTableWidget(self.lab_page)
        if (self.lab_requests_table.columnCount() < 7):
            self.lab_requests_table.setColumnCount(7)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.lab_requests_table.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        self.lab_requests_table.setObjectName(u"lab_requests_table")
        self.lab_requests_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.lab_requests_table.horizontalHeader().setDefaultSectionSize(120)
        self.lab_requests_table.horizontalHeader().setStretchLastSection(True)
        self.lab_requests_table.verticalHeader().setVisible(False)

        self.verticalLayout_63.addWidget(self.lab_requests_table)

        self.stackedWidget_2.addWidget(self.lab_page)
        self.profile_page = QWidget()
        self.profile_page.setObjectName(u"profile_page")
        self.verticalLayout_42 = QVBoxLayout(self.profile_page)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.horizontalLayout_78 = QHBoxLayout()
        self.horizontalLayout_78.setObjectName(u"horizontalLayout_78")
        self.horizontalSpacer_97 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_97)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.doctor_profile_2 = QLabel(self.profile_page)
        self.doctor_profile_2.setObjectName(u"doctor_profile_2")
        self.doctor_profile_2.setPixmap(QPixmap(u":/static/icons8-user-48.png"))

        self.horizontalLayout_62.addWidget(self.doctor_profile_2)

        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.fullName_profile = QLabel(self.profile_page)
        self.fullName_profile.setObjectName(u"fullName_profile")

        self.horizontalLayout_44.addWidget(self.fullName_profile)

        self.horizontalSpacer_101 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_44.addItem(self.horizontalSpacer_101)


        self.verticalLayout_22.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.speciality_profile = QLabel(self.profile_page)
        self.speciality_profile.setObjectName(u"speciality_profile")

        self.horizontalLayout_58.addWidget(self.speciality_profile)

        self.horizontalSpacer_90 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_58.addItem(self.horizontalSpacer_90)


        self.verticalLayout_22.addLayout(self.horizontalLayout_58)


        self.horizontalLayout_62.addLayout(self.verticalLayout_22)


        self.horizontalLayout_78.addLayout(self.horizontalLayout_62)

        self.horizontalSpacer_98 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_78.addItem(self.horizontalSpacer_98)


        self.verticalLayout_42.addLayout(self.horizontalLayout_78)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.horizontalSpacer_93 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_93)

        self.label_57 = QLabel(self.profile_page)
        self.label_57.setObjectName(u"label_57")

        self.horizontalLayout_60.addWidget(self.label_57)

        self.old_password = QLineEdit(self.profile_page)
        self.old_password.setObjectName(u"old_password")
        self.old_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.old_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_60.addWidget(self.old_password)

        self.show_old_password = QPushButton(self.profile_page)
        self.show_old_password.setObjectName(u"show_old_password")
        self.show_old_password.setIcon(icon)
        self.show_old_password.setIconSize(QSize(20, 20))

        self.horizontalLayout_60.addWidget(self.show_old_password)

        self.horizontalSpacer_94 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_60.addItem(self.horizontalSpacer_94)


        self.verticalLayout_42.addLayout(self.horizontalLayout_60)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalSpacer_95 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_95)

        self.label_58 = QLabel(self.profile_page)
        self.label_58.setObjectName(u"label_58")

        self.horizontalLayout_59.addWidget(self.label_58)

        self.new_password = QLineEdit(self.profile_page)
        self.new_password.setObjectName(u"new_password")
        self.new_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.new_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_59.addWidget(self.new_password)

        self.show_new_password = QPushButton(self.profile_page)
        self.show_new_password.setObjectName(u"show_new_password")
        self.show_new_password.setIcon(icon)
        self.show_new_password.setIconSize(QSize(20, 20))

        self.horizontalLayout_59.addWidget(self.show_new_password)

        self.horizontalSpacer_96 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_59.addItem(self.horizontalSpacer_96)


        self.verticalLayout_42.addLayout(self.horizontalLayout_59)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.horizontalSpacer_57 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_57)

        self.label_62 = QLabel(self.profile_page)
        self.label_62.setObjectName(u"label_62")

        self.horizontalLayout_94.addWidget(self.label_62)

        self.confirm_new_password = QLineEdit(self.profile_page)
        self.confirm_new_password.setObjectName(u"confirm_new_password")
        self.confirm_new_password.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.confirm_new_password.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_94.addWidget(self.confirm_new_password)

        self.show_confirm_password = QPushButton(self.profile_page)
        self.show_confirm_password.setObjectName(u"show_confirm_password")
        self.show_confirm_password.setIcon(icon)
        self.show_confirm_password.setIconSize(QSize(20, 20))

        self.horizontalLayout_94.addWidget(self.show_confirm_password)

        self.horizontalSpacer_58 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_94.addItem(self.horizontalSpacer_58)


        self.verticalLayout_42.addLayout(self.horizontalLayout_94)

        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.horizontalSpacer_91 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_91)

        self.confirm_button = QPushButton(self.profile_page)
        self.confirm_button.setObjectName(u"confirm_button")
        self.confirm_button.setStyleSheet(u"QPushButton#confirm_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"	border-radius: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_61.addWidget(self.confirm_button)

        self.cancel_button = QPushButton(self.profile_page)
        self.cancel_button.setObjectName(u"cancel_button")
        self.cancel_button.setStyleSheet(u"QPushButton#cancel_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"	border-radius: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#cancel_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_61.addWidget(self.cancel_button)

        self.horizontalSpacer_92 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_92)


        self.verticalLayout_42.addLayout(self.horizontalLayout_61)

        self.verticalSpacer_16 = QSpacerItem(20, 525, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_42.addItem(self.verticalSpacer_16)

        self.stackedWidget_2.addWidget(self.profile_page)
        self.schedule_page = QWidget()
        self.schedule_page.setObjectName(u"schedule_page")
        self.verticalLayout_15 = QVBoxLayout(self.schedule_page)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_23 = QLabel(self.schedule_page)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setStyleSheet(u"font: 20pt;\n"
"font-weight: bold;")

        self.horizontalLayout_41.addWidget(self.label_23)

        self.horizontalSpacer_46 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_41.addItem(self.horizontalSpacer_46)


        self.verticalLayout_15.addLayout(self.horizontalLayout_41)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_4 = QLabel(self.schedule_page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_42.addWidget(self.label_4)

        self.date_search_button = QDateEdit(self.schedule_page)
        self.date_search_button.setObjectName(u"date_search_button")
        self.date_search_button.setStyleSheet(u"background-color: white;")
        self.date_search_button.setDate(QDate(2024, 1, 1))

        self.horizontalLayout_42.addWidget(self.date_search_button)

        self.label_24 = QLabel(self.schedule_page)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_42.addWidget(self.label_24)

        self.search_hnNo_button = QLineEdit(self.schedule_page)
        self.search_hnNo_button.setObjectName(u"search_hnNo_button")
        self.search_hnNo_button.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_42.addWidget(self.search_hnNo_button)

        self.search_button = QPushButton(self.schedule_page)
        self.search_button.setObjectName(u"search_button")
        self.search_button.setStyleSheet(u"")
        icon18 = QIcon()
        icon18.addFile(u"static/19.png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_button.setIcon(icon18)
        self.search_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_42.addWidget(self.search_button)

        self.horizontalSpacer_47 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_47)


        self.verticalLayout_15.addLayout(self.horizontalLayout_42)

        self.doctor_schedule_table = QTableWidget(self.schedule_page)
        if (self.doctor_schedule_table.columnCount() < 4):
            self.doctor_schedule_table.setColumnCount(4)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.doctor_schedule_table.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.doctor_schedule_table.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.doctor_schedule_table.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.doctor_schedule_table.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        self.doctor_schedule_table.setObjectName(u"doctor_schedule_table")
        self.doctor_schedule_table.setMinimumSize(QSize(0, 400))
        self.doctor_schedule_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.doctor_schedule_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.doctor_schedule_table.horizontalHeader().setDefaultSectionSize(150)
        self.doctor_schedule_table.horizontalHeader().setStretchLastSection(True)
        self.doctor_schedule_table.verticalHeader().setVisible(False)
        self.doctor_schedule_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.doctor_schedule_table)

        self.pushButton = QPushButton(self.schedule_page)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_15.addWidget(self.pushButton)

        self.stackedWidget_2.addWidget(self.schedule_page)
        self.medical_record_page = QWidget()
        self.medical_record_page.setObjectName(u"medical_record_page")
        self.medical_record_page.setMinimumSize(QSize(0, 0))
        self.verticalLayout_12 = QVBoxLayout(self.medical_record_page)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.medical_record_widget = QWidget(self.medical_record_page)
        self.medical_record_widget.setObjectName(u"medical_record_widget")
        self.medical_record_widget.setMinimumSize(QSize(0, 0))
        self.verticalLayout_9 = QVBoxLayout(self.medical_record_widget)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout_82 = QHBoxLayout()
        self.horizontalLayout_82.setObjectName(u"horizontalLayout_82")
        self.label_patient_info = QLabel(self.medical_record_widget)
        self.label_patient_info.setObjectName(u"label_patient_info")
        self.label_patient_info.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_82.addWidget(self.label_patient_info)

        self.horizontalSpacer_100 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_82.addItem(self.horizontalSpacer_100)

        self.edit_patient_info = QPushButton(self.medical_record_widget)
        self.edit_patient_info.setObjectName(u"edit_patient_info")
        self.edit_patient_info.setStyleSheet(u"QPushButton#edit_patient_info {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#edit_patient_info:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_82.addWidget(self.edit_patient_info)

        self.back_button_2 = QPushButton(self.medical_record_widget)
        self.back_button_2.setObjectName(u"back_button_2")
        self.back_button_2.setStyleSheet(u"QPushButton#back_button_2 {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#back_button_2:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_82.addWidget(self.back_button_2)


        self.verticalLayout_9.addLayout(self.horizontalLayout_82)

        self.horizontalLayout_161 = QHBoxLayout()
        self.horizontalLayout_161.setObjectName(u"horizontalLayout_161")
        self.patient_info1_widget = QWidget(self.medical_record_widget)
        self.patient_info1_widget.setObjectName(u"patient_info1_widget")
        self.patient_info1_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_6 = QVBoxLayout(self.patient_info1_widget)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalSpacer_6 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)

        self.patient_photo = QLabel(self.patient_info1_widget)
        self.patient_photo.setObjectName(u"patient_photo")
        self.patient_photo.setPixmap(QPixmap(u":/static/icons8-user-48.png"))

        self.horizontalLayout_11.addWidget(self.patient_photo)

        self.horizontalSpacer_7 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_7)


        self.verticalLayout_6.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_8 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_8)

        self.patient_name = QLabel(self.patient_info1_widget)
        self.patient_name.setObjectName(u"patient_name")

        self.horizontalLayout_10.addWidget(self.patient_name)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_9)


        self.verticalLayout_6.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_60 = QLabel(self.patient_info1_widget)
        self.label_60.setObjectName(u"label_60")

        self.horizontalLayout_4.addWidget(self.label_60)

        self.patient_hn_no = QLabel(self.patient_info1_widget)
        self.patient_hn_no.setObjectName(u"patient_hn_no")

        self.horizontalLayout_4.addWidget(self.patient_hn_no)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_89 = QHBoxLayout()
        self.horizontalLayout_89.setObjectName(u"horizontalLayout_89")
        self.label_112 = QLabel(self.patient_info1_widget)
        self.label_112.setObjectName(u"label_112")

        self.horizontalLayout_89.addWidget(self.label_112)

        self.patient_email_display = QLabel(self.patient_info1_widget)
        self.patient_email_display.setObjectName(u"patient_email_display")

        self.horizontalLayout_89.addWidget(self.patient_email_display)


        self.verticalLayout_6.addLayout(self.horizontalLayout_89)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_61 = QLabel(self.patient_info1_widget)
        self.label_61.setObjectName(u"label_61")

        self.horizontalLayout_5.addWidget(self.label_61)

        self.patient_dob = QLabel(self.patient_info1_widget)
        self.patient_dob.setObjectName(u"patient_dob")

        self.horizontalLayout_5.addWidget(self.patient_dob)


        self.verticalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_86 = QHBoxLayout()
        self.horizontalLayout_86.setObjectName(u"horizontalLayout_86")
        self.label_13 = QLabel(self.patient_info1_widget)
        self.label_13.setObjectName(u"label_13")

        self.horizontalLayout_86.addWidget(self.label_13)

        self.patient_sex = QLabel(self.patient_info1_widget)
        self.patient_sex.setObjectName(u"patient_sex")

        self.horizontalLayout_86.addWidget(self.patient_sex)


        self.verticalLayout_6.addLayout(self.horizontalLayout_86)

        self.horizontalLayout_87 = QHBoxLayout()
        self.horizontalLayout_87.setObjectName(u"horizontalLayout_87")
        self.label_14 = QLabel(self.patient_info1_widget)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_87.addWidget(self.label_14)

        self.patient_age = QLabel(self.patient_info1_widget)
        self.patient_age.setObjectName(u"patient_age")

        self.horizontalLayout_87.addWidget(self.patient_age)


        self.verticalLayout_6.addLayout(self.horizontalLayout_87)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_11 = QLabel(self.patient_info1_widget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_6.addWidget(self.label_11)

        self.patient_weight = QLabel(self.patient_info1_widget)
        self.patient_weight.setObjectName(u"patient_weight")

        self.horizontalLayout_6.addWidget(self.patient_weight)


        self.verticalLayout_6.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_12 = QLabel(self.patient_info1_widget)
        self.label_12.setObjectName(u"label_12")

        self.horizontalLayout_7.addWidget(self.label_12)

        self.patient_height = QLabel(self.patient_info1_widget)
        self.patient_height.setObjectName(u"patient_height")

        self.horizontalLayout_7.addWidget(self.patient_height)


        self.verticalLayout_6.addLayout(self.horizontalLayout_7)


        self.horizontalLayout_161.addWidget(self.patient_info1_widget)

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

        self.patient_address_2 = QLabel(self.patient_info2_widget)
        self.patient_address_2.setObjectName(u"patient_address_2")

        self.horizontalLayout_8.addWidget(self.patient_address_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_tel_no = QLabel(self.patient_info2_widget)
        self.label_tel_no.setObjectName(u"label_tel_no")

        self.horizontalLayout_9.addWidget(self.label_tel_no)

        self.patient_tel = QLabel(self.patient_info2_widget)
        self.patient_tel.setObjectName(u"patient_tel")

        self.horizontalLayout_9.addWidget(self.patient_tel)


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
        self.blood_icon.setPixmap(QPixmap(u":/static/icons8-blood-50.png"))

        self.horizontalLayout_13.addWidget(self.blood_icon)

        self.horizontalSpacer_13 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_13)


        self.verticalLayout_7.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_88 = QHBoxLayout()
        self.horizontalLayout_88.setObjectName(u"horizontalLayout_88")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer_3)

        self.patient_blood_type = QLabel(self.patient_info3_widget)
        self.patient_blood_type.setObjectName(u"patient_blood_type")

        self.horizontalLayout_88.addWidget(self.patient_blood_type)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_88.addItem(self.horizontalSpacer)


        self.verticalLayout_7.addLayout(self.horizontalLayout_88)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalSpacer_14 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_14)

        self.patient_blood_pressure = QLabel(self.patient_info3_widget)
        self.patient_blood_pressure.setObjectName(u"patient_blood_pressure")

        self.horizontalLayout_14.addWidget(self.patient_blood_pressure)

        self.horizontalSpacer_15 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_15)


        self.verticalLayout_7.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_16)

        self.patient_blood_warning = QLabel(self.patient_info3_widget)
        self.patient_blood_warning.setObjectName(u"patient_blood_warning")
        self.patient_blood_warning.setStyleSheet(u"color: red;")

        self.horizontalLayout_15.addWidget(self.patient_blood_warning)

        self.horizontalSpacer_17 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_17)


        self.verticalLayout_7.addLayout(self.horizontalLayout_15)


        self.verticalLayout_5.addWidget(self.patient_info3_widget)


        self.horizontalLayout_161.addLayout(self.verticalLayout_5)


        self.verticalLayout_9.addLayout(self.horizontalLayout_161)

        self.medical_history_widget = QWidget(self.medical_record_widget)
        self.medical_history_widget.setObjectName(u"medical_history_widget")
        self.medical_history_widget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_8 = QVBoxLayout(self.medical_history_widget)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_medical_history = QLabel(self.medical_history_widget)
        self.label_medical_history.setObjectName(u"label_medical_history")
        self.label_medical_history.setStyleSheet(u"")

        self.verticalLayout_8.addWidget(self.label_medical_history)

        self.label_past_treatment_3 = QLabel(self.medical_history_widget)
        self.label_past_treatment_3.setObjectName(u"label_past_treatment_3")

        self.verticalLayout_8.addWidget(self.label_past_treatment_3)

        self.vaccine_list_table_2 = QTableWidget(self.medical_history_widget)
        if (self.vaccine_list_table_2.columnCount() < 2):
            self.vaccine_list_table_2.setColumnCount(2)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.vaccine_list_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.vaccine_list_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        self.vaccine_list_table_2.setObjectName(u"vaccine_list_table_2")
        self.vaccine_list_table_2.setMinimumSize(QSize(0, 300))
        self.vaccine_list_table_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.vaccine_list_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.vaccine_list_table_2.horizontalHeader().setMinimumSectionSize(20)
        self.vaccine_list_table_2.horizontalHeader().setDefaultSectionSize(300)
        self.vaccine_list_table_2.horizontalHeader().setStretchLastSection(True)
        self.vaccine_list_table_2.verticalHeader().setVisible(False)
        self.vaccine_list_table_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.vaccine_list_table_2)

        self.label_past_treatment_4 = QLabel(self.medical_history_widget)
        self.label_past_treatment_4.setObjectName(u"label_past_treatment_4")

        self.verticalLayout_8.addWidget(self.label_past_treatment_4)

        self.medication_list_table_2 = QTableWidget(self.medical_history_widget)
        if (self.medication_list_table_2.columnCount() < 8):
            self.medication_list_table_2.setColumnCount(8)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.medication_list_table_2.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        self.medication_list_table_2.setObjectName(u"medication_list_table_2")
        self.medication_list_table_2.setMinimumSize(QSize(0, 300))
        self.medication_list_table_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.medication_list_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.medication_list_table_2.setWordWrap(False)
        self.medication_list_table_2.horizontalHeader().setDefaultSectionSize(200)
        self.medication_list_table_2.horizontalHeader().setStretchLastSection(True)
        self.medication_list_table_2.verticalHeader().setVisible(False)
        self.medication_list_table_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.medication_list_table_2)

        self.label_allergies = QLabel(self.medical_history_widget)
        self.label_allergies.setObjectName(u"label_allergies")

        self.verticalLayout_8.addWidget(self.label_allergies)

        self.allergy_list_table_2 = QTableWidget(self.medical_history_widget)
        if (self.allergy_list_table_2.columnCount() < 1):
            self.allergy_list_table_2.setColumnCount(1)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.allergy_list_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        self.allergy_list_table_2.setObjectName(u"allergy_list_table_2")
        self.allergy_list_table_2.setMinimumSize(QSize(0, 200))
        self.allergy_list_table_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.allergy_list_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.allergy_list_table_2.horizontalHeader().setStretchLastSection(True)
        self.allergy_list_table_2.verticalHeader().setVisible(False)
        self.allergy_list_table_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_8.addWidget(self.allergy_list_table_2)

        self.label_past_treatment_2 = QLabel(self.medical_history_widget)
        self.label_past_treatment_2.setObjectName(u"label_past_treatment_2")

        self.verticalLayout_8.addWidget(self.label_past_treatment_2)

        self.lab_test_list_table_2 = QTableWidget(self.medical_history_widget)
        if (self.lab_test_list_table_2.columnCount() < 5):
            self.lab_test_list_table_2.setColumnCount(5)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.lab_test_list_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.lab_test_list_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.lab_test_list_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.lab_test_list_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.lab_test_list_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        self.lab_test_list_table_2.setObjectName(u"lab_test_list_table_2")
        self.lab_test_list_table_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.lab_test_list_table_2.horizontalHeader().setDefaultSectionSize(120)
        self.lab_test_list_table_2.horizontalHeader().setStretchLastSection(True)
        self.lab_test_list_table_2.verticalHeader().setVisible(False)

        self.verticalLayout_8.addWidget(self.lab_test_list_table_2)


        self.verticalLayout_9.addWidget(self.medical_history_widget)


        self.verticalLayout_12.addWidget(self.medical_record_widget)

        self.stackedWidget_2.addWidget(self.medical_record_page)
        self.patient_report_page = QWidget()
        self.patient_report_page.setObjectName(u"patient_report_page")
        self.verticalLayout_61 = QVBoxLayout(self.patient_report_page)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.horizontalLayout_97 = QHBoxLayout()
        self.horizontalLayout_97.setObjectName(u"horizontalLayout_97")
        self.label_71 = QLabel(self.patient_report_page)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_97.addWidget(self.label_71)

        self.horizontalSpacer_105 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_97.addItem(self.horizontalSpacer_105)

        self.report_edit_button = QPushButton(self.patient_report_page)
        self.report_edit_button.setObjectName(u"report_edit_button")
        self.report_edit_button.setStyleSheet(u"QPushButton#report_edit_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"	border-radius: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#report_edit_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_97.addWidget(self.report_edit_button)


        self.verticalLayout_61.addLayout(self.horizontalLayout_97)

        self.report_patient_table = QTableWidget(self.patient_report_page)
        if (self.report_patient_table.columnCount() < 2):
            self.report_patient_table.setColumnCount(2)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.report_patient_table.setHorizontalHeaderItem(0, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.report_patient_table.setHorizontalHeaderItem(1, __qtablewidgetitem41)
        self.report_patient_table.setObjectName(u"report_patient_table")
        self.report_patient_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.report_patient_table.horizontalHeader().setDefaultSectionSize(200)
        self.report_patient_table.horizontalHeader().setStretchLastSection(True)
        self.report_patient_table.verticalHeader().setVisible(False)

        self.verticalLayout_61.addWidget(self.report_patient_table)

        self.stackedWidget_2.addWidget(self.patient_report_page)
        self.report_page = QWidget()
        self.report_page.setObjectName(u"report_page")
        self.verticalLayout_62 = QVBoxLayout(self.report_page)
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.horizontalLayout_95 = QHBoxLayout()
        self.horizontalLayout_95.setObjectName(u"horizontalLayout_95")
        self.horizontalSpacer_102 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_102)

        self.label_63 = QLabel(self.report_page)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_95.addWidget(self.label_63)

        self.horizontalSpacer_103 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_95.addItem(self.horizontalSpacer_103)


        self.verticalLayout_62.addLayout(self.horizontalLayout_95)

        self.horizontalLayout_96 = QHBoxLayout()
        self.horizontalLayout_96.setObjectName(u"horizontalLayout_96")
        self.horizontalSpacer_104 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_104)

        self.report_date = QLabel(self.report_page)
        self.report_date.setObjectName(u"report_date")
        self.report_date.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_96.addWidget(self.report_date)

        self.horizontalSpacer_106 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_106)

        self.label_65 = QLabel(self.report_page)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_96.addWidget(self.label_65)

        self.report_hn_no = QLabel(self.report_page)
        self.report_hn_no.setObjectName(u"report_hn_no")
        self.report_hn_no.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_96.addWidget(self.report_hn_no)

        self.horizontalSpacer_112 = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_112)

        self.label_66 = QLabel(self.report_page)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_96.addWidget(self.label_66)

        self.report_patient_name = QLabel(self.report_page)
        self.report_patient_name.setObjectName(u"report_patient_name")
        self.report_patient_name.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_96.addWidget(self.report_patient_name)

        self.horizontalSpacer_117 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_96.addItem(self.horizontalSpacer_117)


        self.verticalLayout_62.addLayout(self.horizontalLayout_96)

        self.horizontalLayout_99 = QHBoxLayout()
        self.horizontalLayout_99.setObjectName(u"horizontalLayout_99")
        self.label_64 = QLabel(self.report_page)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_99.addWidget(self.label_64)

        self.horizontalSpacer_107 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_99.addItem(self.horizontalSpacer_107)


        self.verticalLayout_62.addLayout(self.horizontalLayout_99)

        self.report_summary = QTextEdit(self.report_page)
        self.report_summary.setObjectName(u"report_summary")
        self.report_summary.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_62.addWidget(self.report_summary)

        self.horizontalLayout_100 = QHBoxLayout()
        self.horizontalLayout_100.setObjectName(u"horizontalLayout_100")
        self.label_67 = QLabel(self.report_page)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_100.addWidget(self.label_67)

        self.horizontalSpacer_108 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_100.addItem(self.horizontalSpacer_108)


        self.verticalLayout_62.addLayout(self.horizontalLayout_100)

        self.report_vaccine_table = QTableWidget(self.report_page)
        if (self.report_vaccine_table.columnCount() < 2):
            self.report_vaccine_table.setColumnCount(2)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.report_vaccine_table.setHorizontalHeaderItem(0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.report_vaccine_table.setHorizontalHeaderItem(1, __qtablewidgetitem43)
        self.report_vaccine_table.setObjectName(u"report_vaccine_table")
        self.report_vaccine_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.report_vaccine_table.horizontalHeader().setDefaultSectionSize(200)
        self.report_vaccine_table.horizontalHeader().setStretchLastSection(True)
        self.report_vaccine_table.verticalHeader().setVisible(False)

        self.verticalLayout_62.addWidget(self.report_vaccine_table)

        self.horizontalLayout_101 = QHBoxLayout()
        self.horizontalLayout_101.setObjectName(u"horizontalLayout_101")
        self.label_68 = QLabel(self.report_page)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_101.addWidget(self.label_68)

        self.horizontalSpacer_109 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_101.addItem(self.horizontalSpacer_109)


        self.verticalLayout_62.addLayout(self.horizontalLayout_101)

        self.report_medication_table = QTableWidget(self.report_page)
        if (self.report_medication_table.columnCount() < 6):
            self.report_medication_table.setColumnCount(6)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.report_medication_table.setHorizontalHeaderItem(0, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.report_medication_table.setHorizontalHeaderItem(1, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.report_medication_table.setHorizontalHeaderItem(2, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.report_medication_table.setHorizontalHeaderItem(3, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.report_medication_table.setHorizontalHeaderItem(4, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.report_medication_table.setHorizontalHeaderItem(5, __qtablewidgetitem49)
        self.report_medication_table.setObjectName(u"report_medication_table")
        self.report_medication_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.report_medication_table.horizontalHeader().setDefaultSectionSize(150)
        self.report_medication_table.horizontalHeader().setStretchLastSection(True)
        self.report_medication_table.verticalHeader().setVisible(False)

        self.verticalLayout_62.addWidget(self.report_medication_table)

        self.horizontalLayout_102 = QHBoxLayout()
        self.horizontalLayout_102.setObjectName(u"horizontalLayout_102")
        self.label_69 = QLabel(self.report_page)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_102.addWidget(self.label_69)

        self.horizontalSpacer_110 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_102.addItem(self.horizontalSpacer_110)


        self.verticalLayout_62.addLayout(self.horizontalLayout_102)

        self.report_lab_test_table = QTableWidget(self.report_page)
        if (self.report_lab_test_table.columnCount() < 2):
            self.report_lab_test_table.setColumnCount(2)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.report_lab_test_table.setHorizontalHeaderItem(0, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.report_lab_test_table.setHorizontalHeaderItem(1, __qtablewidgetitem51)
        self.report_lab_test_table.setObjectName(u"report_lab_test_table")
        self.report_lab_test_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.report_lab_test_table.horizontalHeader().setDefaultSectionSize(300)
        self.report_lab_test_table.horizontalHeader().setStretchLastSection(True)
        self.report_lab_test_table.verticalHeader().setVisible(False)

        self.verticalLayout_62.addWidget(self.report_lab_test_table)

        self.horizontalLayout_103 = QHBoxLayout()
        self.horizontalLayout_103.setObjectName(u"horizontalLayout_103")
        self.label_70 = QLabel(self.report_page)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_103.addWidget(self.label_70)

        self.horizontalSpacer_111 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_103.addItem(self.horizontalSpacer_111)


        self.verticalLayout_62.addLayout(self.horizontalLayout_103)

        self.report_other_table = QTableWidget(self.report_page)
        if (self.report_other_table.columnCount() < 2):
            self.report_other_table.setColumnCount(2)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.report_other_table.setHorizontalHeaderItem(0, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.report_other_table.setHorizontalHeaderItem(1, __qtablewidgetitem53)
        self.report_other_table.setObjectName(u"report_other_table")
        self.report_other_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.report_other_table.horizontalHeader().setDefaultSectionSize(150)
        self.report_other_table.horizontalHeader().setStretchLastSection(True)
        self.report_other_table.verticalHeader().setVisible(False)

        self.verticalLayout_62.addWidget(self.report_other_table)

        self.horizontalLayout_106 = QHBoxLayout()
        self.horizontalLayout_106.setObjectName(u"horizontalLayout_106")
        self.horizontalSpacer_113 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_113)

        self.report_add_other = QPushButton(self.report_page)
        self.report_add_other.setObjectName(u"report_add_other")
        self.report_add_other.setStyleSheet(u"QPushButton#report_add_other {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#report_add_other:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_106.addWidget(self.report_add_other)

        self.report_delete_other = QPushButton(self.report_page)
        self.report_delete_other.setObjectName(u"report_delete_other")
        self.report_delete_other.setStyleSheet(u"QPushButton#report_delete_other {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#report_delete_other:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_106.addWidget(self.report_delete_other)

        self.horizontalSpacer_114 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_106.addItem(self.horizontalSpacer_114)


        self.verticalLayout_62.addLayout(self.horizontalLayout_106)

        self.horizontalLayout_104 = QHBoxLayout()
        self.horizontalLayout_104.setObjectName(u"horizontalLayout_104")
        self.horizontalSpacer_115 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_115)

        self.report_confirm_button = QPushButton(self.report_page)
        self.report_confirm_button.setObjectName(u"report_confirm_button")
        self.report_confirm_button.setStyleSheet(u"QPushButton#report_confirm_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#report_confirm_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_104.addWidget(self.report_confirm_button)

        self.report_draft_button = QPushButton(self.report_page)
        self.report_draft_button.setObjectName(u"report_draft_button")
        self.report_draft_button.setStyleSheet(u"QPushButton#report_draft_button {\n"
"	background-color: white;\n"
"	color: black;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#report_draft_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_104.addWidget(self.report_draft_button)

        self.report_cancel_button = QPushButton(self.report_page)
        self.report_cancel_button.setObjectName(u"report_cancel_button")
        self.report_cancel_button.setStyleSheet(u"QPushButton#report_cancel_button {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#report_cancel_button:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_104.addWidget(self.report_cancel_button)

        self.horizontalSpacer_116 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_104.addItem(self.horizontalSpacer_116)


        self.verticalLayout_62.addLayout(self.horizontalLayout_104)

        self.stackedWidget_2.addWidget(self.report_page)
        self.lab_request_page = QWidget()
        self.lab_request_page.setObjectName(u"lab_request_page")
        self.verticalLayout_11 = QVBoxLayout(self.lab_request_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.widget = QWidget(self.lab_request_page)
        self.widget.setObjectName(u"widget")
        self.verticalLayout_10 = QVBoxLayout(self.widget)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalSpacer_18 = QSpacerItem(168, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_16.addItem(self.horizontalSpacer_18)

        self.lab_title = QLabel(self.widget)
        self.lab_title.setObjectName(u"lab_title")
        self.lab_title.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

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
        self.dat_request_2.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_17.addWidget(self.dat_request_2)

        self.horizontalSpacer_21 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_21)

        self.date_request = QLabel(self.widget)
        self.date_request.setObjectName(u"date_request")
        self.date_request.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_17.addWidget(self.date_request)

        self.horizontalSpacer_22 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_22)


        self.verticalLayout_10.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_127 = QHBoxLayout()
        self.horizontalLayout_127.setObjectName(u"horizontalLayout_127")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_127.addWidget(self.label_5)

        self.case_type = QComboBox(self.widget)
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.addItem("")
        self.case_type.setObjectName(u"case_type")
        self.case_type.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_127.addWidget(self.case_type)

        self.horizontalSpacer_23 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_127.addItem(self.horizontalSpacer_23)


        self.verticalLayout_10.addLayout(self.horizontalLayout_127)

        self.horizontalLayout_98 = QHBoxLayout()
        self.horizontalLayout_98.setObjectName(u"horizontalLayout_98")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_98.addWidget(self.label_7)

        self.urgency = QComboBox(self.widget)
        self.urgency.addItem("")
        self.urgency.addItem("")
        self.urgency.addItem("")
        self.urgency.setObjectName(u"urgency")
        self.urgency.setStyleSheet(u"background-color: white;\n"
"font: 10pt \"Microsoft Sans Serif\";")

        self.horizontalLayout_98.addWidget(self.urgency)

        self.horizontalSpacer_118 = QSpacerItem(13, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_98.addItem(self.horizontalSpacer_118)


        self.verticalLayout_10.addLayout(self.horizontalLayout_98)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_73 = QLabel(self.widget)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_18.addWidget(self.label_73)

        self.faculty = QComboBox(self.widget)
        self.faculty.setObjectName(u"faculty")
        self.faculty.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_18.addWidget(self.faculty)

        self.horizontalSpacer_143 = QSpacerItem(13, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_143)


        self.verticalLayout_10.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_108 = QHBoxLayout()
        self.horizontalLayout_108.setObjectName(u"horizontalLayout_108")
        self.label_76 = QLabel(self.widget)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_108.addWidget(self.label_76)

        self.lab_request_hn_no = QLineEdit(self.widget)
        self.lab_request_hn_no.setObjectName(u"lab_request_hn_no")
        self.lab_request_hn_no.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_108.addWidget(self.lab_request_hn_no)

        self.label_77 = QLabel(self.widget)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_108.addWidget(self.label_77)

        self.lab_request_patient_name = QLineEdit(self.widget)
        self.lab_request_patient_name.setObjectName(u"lab_request_patient_name")
        self.lab_request_patient_name.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_108.addWidget(self.lab_request_patient_name)


        self.verticalLayout_10.addLayout(self.horizontalLayout_108)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.verticalLayout_10.addWidget(self.label_6)

        self.reason = QTextEdit(self.widget)
        self.reason.setObjectName(u"reason")
        self.reason.setStyleSheet(u"background-color: white;\n"
"border: 1px solid black;")

        self.verticalLayout_10.addWidget(self.reason)

        self.submit_button = QPushButton(self.widget)
        self.submit_button.setObjectName(u"submit_button")
        self.submit_button.setStyleSheet(u"QPushButton#submit_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#submit_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_10.addWidget(self.submit_button)

        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_10.addWidget(self.pushButton_5)


        self.verticalLayout_11.addWidget(self.widget)

        self.stackedWidget_2.addWidget(self.lab_request_page)
        self.lab_reply_page = QWidget()
        self.lab_reply_page.setObjectName(u"lab_reply_page")
        self.verticalLayout_14 = QVBoxLayout(self.lab_reply_page)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.horizontalLayout_110 = QHBoxLayout()
        self.horizontalLayout_110.setObjectName(u"horizontalLayout_110")
        self.horizontalSpacer_122 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_122)

        self.label_75 = QLabel(self.lab_reply_page)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_110.addWidget(self.label_75)

        self.horizontalSpacer_123 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_110.addItem(self.horizontalSpacer_123)


        self.verticalLayout_14.addLayout(self.horizontalLayout_110)

        self.horizontalLayout_111 = QHBoxLayout()
        self.horizontalLayout_111.setObjectName(u"horizontalLayout_111")
        self.horizontalSpacer_126 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_126)

        self.dat_request_3 = QLabel(self.lab_reply_page)
        self.dat_request_3.setObjectName(u"dat_request_3")
        self.dat_request_3.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_111.addWidget(self.dat_request_3)

        self.horizontalSpacer_127 = QSpacerItem(118, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_127)

        self.date_request_2 = QLabel(self.lab_reply_page)
        self.date_request_2.setObjectName(u"date_request_2")
        self.date_request_2.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_111.addWidget(self.date_request_2)

        self.horizontalSpacer_128 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_111.addItem(self.horizontalSpacer_128)


        self.verticalLayout_14.addLayout(self.horizontalLayout_111)

        self.horizontalLayout_118 = QHBoxLayout()
        self.horizontalLayout_118.setObjectName(u"horizontalLayout_118")
        self.label_80 = QLabel(self.lab_reply_page)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_118.addWidget(self.label_80)

        self.case_type_2 = QLabel(self.lab_reply_page)
        self.case_type_2.setObjectName(u"case_type_2")
        self.case_type_2.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_118.addWidget(self.case_type_2)

        self.horizontalSpacer_129 = QSpacerItem(18, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_118.addItem(self.horizontalSpacer_129)


        self.verticalLayout_14.addLayout(self.horizontalLayout_118)

        self.horizontalLayout_115 = QHBoxLayout()
        self.horizontalLayout_115.setObjectName(u"horizontalLayout_115")
        self.label_81 = QLabel(self.lab_reply_page)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_115.addWidget(self.label_81)

        self.urgency_2 = QLabel(self.lab_reply_page)
        self.urgency_2.setObjectName(u"urgency_2")
        self.urgency_2.setStyleSheet(u"font:15pt;\n"
"")

        self.horizontalLayout_115.addWidget(self.urgency_2)

        self.horizontalSpacer_130 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_115.addItem(self.horizontalSpacer_130)


        self.verticalLayout_14.addLayout(self.horizontalLayout_115)

        self.horizontalLayout_114 = QHBoxLayout()
        self.horizontalLayout_114.setObjectName(u"horizontalLayout_114")
        self.label_82 = QLabel(self.lab_reply_page)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_114.addWidget(self.label_82)

        self.faculty_2 = QLabel(self.lab_reply_page)
        self.faculty_2.setObjectName(u"faculty_2")
        self.faculty_2.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_114.addWidget(self.faculty_2)

        self.horizontalSpacer_133 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_114.addItem(self.horizontalSpacer_133)


        self.verticalLayout_14.addLayout(self.horizontalLayout_114)

        self.horizontalLayout_116 = QHBoxLayout()
        self.horizontalLayout_116.setObjectName(u"horizontalLayout_116")
        self.label_83 = QLabel(self.lab_reply_page)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_116.addWidget(self.label_83)

        self.lab_request_hn_no_2 = QLabel(self.lab_reply_page)
        self.lab_request_hn_no_2.setObjectName(u"lab_request_hn_no_2")
        self.lab_request_hn_no_2.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_116.addWidget(self.lab_request_hn_no_2)

        self.label_84 = QLabel(self.lab_reply_page)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_116.addWidget(self.label_84)

        self.lab_request_patient_name_2 = QLabel(self.lab_reply_page)
        self.lab_request_patient_name_2.setObjectName(u"lab_request_patient_name_2")
        self.lab_request_patient_name_2.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_116.addWidget(self.lab_request_patient_name_2)


        self.verticalLayout_14.addLayout(self.horizontalLayout_116)

        self.label_85 = QLabel(self.lab_reply_page)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.verticalLayout_14.addWidget(self.label_85)

        self.reason_2 = QTextEdit(self.lab_reply_page)
        self.reason_2.setObjectName(u"reason_2")
        self.reason_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid black;")
        self.reason_2.setReadOnly(True)

        self.verticalLayout_14.addWidget(self.reason_2)

        self.horizontalLayout_109 = QHBoxLayout()
        self.horizontalLayout_109.setObjectName(u"horizontalLayout_109")
        self.horizontalSpacer_124 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_124)

        self.display_file_name = QLabel(self.lab_reply_page)
        self.display_file_name.setObjectName(u"display_file_name")

        self.horizontalLayout_109.addWidget(self.display_file_name)

        self.upload_file_button = QPushButton(self.lab_reply_page)
        self.upload_file_button.setObjectName(u"upload_file_button")
        self.upload_file_button.setStyleSheet(u"QPushButton#upload_file_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#upload_file_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_109.addWidget(self.upload_file_button)

        self.horizontalSpacer_125 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_109.addItem(self.horizontalSpacer_125)


        self.verticalLayout_14.addLayout(self.horizontalLayout_109)

        self.label_78 = QLabel(self.lab_reply_page)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.verticalLayout_14.addWidget(self.label_78)

        self.note_2 = QTextEdit(self.lab_reply_page)
        self.note_2.setObjectName(u"note_2")
        self.note_2.setStyleSheet(u"background-color: white;\n"
"border: 1px solid black;")

        self.verticalLayout_14.addWidget(self.note_2)

        self.horizontalLayout_117 = QHBoxLayout()
        self.horizontalLayout_117.setObjectName(u"horizontalLayout_117")
        self.horizontalSpacer_131 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_131)

        self.confirm_lab_reply = QPushButton(self.lab_reply_page)
        self.confirm_lab_reply.setObjectName(u"confirm_lab_reply")
        self.confirm_lab_reply.setStyleSheet(u"QPushButton#confirm_lab_reply {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_lab_reply:hover {\n"
"    background-color: grey;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_117.addWidget(self.confirm_lab_reply)

        self.cancel_lab_reply = QPushButton(self.lab_reply_page)
        self.cancel_lab_reply.setObjectName(u"cancel_lab_reply")
        self.cancel_lab_reply.setStyleSheet(u"QPushButton#cancel_lab_reply {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#cancel_lab_reply:hover {\n"
"    background-color: grey;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_117.addWidget(self.cancel_lab_reply)

        self.reject_lab_reply = QPushButton(self.lab_reply_page)
        self.reject_lab_reply.setObjectName(u"reject_lab_reply")
        self.reject_lab_reply.setStyleSheet(u"QPushButton#reject_lab_reply {\n"
"	background-color: red;\n"
"	color: white;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#reject_lab_reply:hover {\n"
"    background-color: grey;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_117.addWidget(self.reject_lab_reply)

        self.horizontalSpacer_132 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_117.addItem(self.horizontalSpacer_132)


        self.verticalLayout_14.addLayout(self.horizontalLayout_117)

        self.verticalSpacer_17 = QSpacerItem(20, 782, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_14.addItem(self.verticalSpacer_17)

        self.stackedWidget_2.addWidget(self.lab_reply_page)
        self.received_replies_page = QWidget()
        self.received_replies_page.setObjectName(u"received_replies_page")
        self.verticalLayout_66 = QVBoxLayout(self.received_replies_page)
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.horizontalLayout_119 = QHBoxLayout()
        self.horizontalLayout_119.setObjectName(u"horizontalLayout_119")
        self.horizontalSpacer_134 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_119.addItem(self.horizontalSpacer_134)

        self.label_86 = QLabel(self.received_replies_page)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_119.addWidget(self.label_86)

        self.horizontalSpacer_135 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_119.addItem(self.horizontalSpacer_135)


        self.verticalLayout_66.addLayout(self.horizontalLayout_119)

        self.horizontalLayout_120 = QHBoxLayout()
        self.horizontalLayout_120.setObjectName(u"horizontalLayout_120")
        self.horizontalSpacer_136 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_120.addItem(self.horizontalSpacer_136)

        self.viewButton = QPushButton(self.received_replies_page)
        self.viewButton.setObjectName(u"viewButton")
        self.viewButton.setStyleSheet(u"QPushButton#viewButton {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#viewButton:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_120.addWidget(self.viewButton)

        self.backBT = QPushButton(self.received_replies_page)
        self.backBT.setObjectName(u"backBT")
        self.backBT.setStyleSheet(u"QPushButton#backBT {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#backBT:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_120.addWidget(self.backBT)


        self.verticalLayout_66.addLayout(self.horizontalLayout_120)

        self.lab_requests_table_2 = QTableWidget(self.received_replies_page)
        if (self.lab_requests_table_2.columnCount() < 5):
            self.lab_requests_table_2.setColumnCount(5)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.lab_requests_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.lab_requests_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.lab_requests_table_2.setHorizontalHeaderItem(2, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.lab_requests_table_2.setHorizontalHeaderItem(3, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.lab_requests_table_2.setHorizontalHeaderItem(4, __qtablewidgetitem58)
        self.lab_requests_table_2.setObjectName(u"lab_requests_table_2")
        self.lab_requests_table_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.lab_requests_table_2.horizontalHeader().setDefaultSectionSize(120)
        self.lab_requests_table_2.horizontalHeader().setStretchLastSection(True)
        self.lab_requests_table_2.verticalHeader().setVisible(False)

        self.verticalLayout_66.addWidget(self.lab_requests_table_2)

        self.stackedWidget_2.addWidget(self.received_replies_page)
        self.received_reply = QWidget()
        self.received_reply.setObjectName(u"received_reply")
        self.verticalLayout_67 = QVBoxLayout(self.received_reply)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.horizontalLayout_123 = QHBoxLayout()
        self.horizontalLayout_123.setObjectName(u"horizontalLayout_123")
        self.horizontalSpacer_137 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_137)

        self.label_87 = QLabel(self.received_reply)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_123.addWidget(self.label_87)

        self.horizontalSpacer_138 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_123.addItem(self.horizontalSpacer_138)


        self.verticalLayout_67.addLayout(self.horizontalLayout_123)

        self.horizontalLayout_121 = QHBoxLayout()
        self.horizontalLayout_121.setObjectName(u"horizontalLayout_121")
        self.dat_request_4 = QLabel(self.received_reply)
        self.dat_request_4.setObjectName(u"dat_request_4")
        self.dat_request_4.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_121.addWidget(self.dat_request_4)

        self.date_request_3 = QLabel(self.received_reply)
        self.date_request_3.setObjectName(u"date_request_3")
        self.date_request_3.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_121.addWidget(self.date_request_3)


        self.verticalLayout_67.addLayout(self.horizontalLayout_121)

        self.horizontalLayout_126 = QHBoxLayout()
        self.horizontalLayout_126.setObjectName(u"horizontalLayout_126")
        self.label_88 = QLabel(self.received_reply)
        self.label_88.setObjectName(u"label_88")
        self.label_88.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_126.addWidget(self.label_88)

        self.case_type_3 = QLabel(self.received_reply)
        self.case_type_3.setObjectName(u"case_type_3")
        self.case_type_3.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_126.addWidget(self.case_type_3)


        self.verticalLayout_67.addLayout(self.horizontalLayout_126)

        self.horizontalLayout_122 = QHBoxLayout()
        self.horizontalLayout_122.setObjectName(u"horizontalLayout_122")
        self.label_89 = QLabel(self.received_reply)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_122.addWidget(self.label_89)

        self.lab_request_hn_no_3 = QLabel(self.received_reply)
        self.lab_request_hn_no_3.setObjectName(u"lab_request_hn_no_3")
        self.lab_request_hn_no_3.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_122.addWidget(self.lab_request_hn_no_3)

        self.label_90 = QLabel(self.received_reply)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_122.addWidget(self.label_90)

        self.lab_request_patient_name_3 = QLabel(self.received_reply)
        self.lab_request_patient_name_3.setObjectName(u"lab_request_patient_name_3")
        self.lab_request_patient_name_3.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_122.addWidget(self.lab_request_patient_name_3)


        self.verticalLayout_67.addLayout(self.horizontalLayout_122)

        self.horizontalLayout_124 = QHBoxLayout()
        self.horizontalLayout_124.setObjectName(u"horizontalLayout_124")
        self.horizontalSpacer_139 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_124.addItem(self.horizontalSpacer_139)

        self.label_91 = QLabel(self.received_reply)
        self.label_91.setObjectName(u"label_91")
        self.label_91.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_124.addWidget(self.label_91)

        self.download_button = QPushButton(self.received_reply)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setStyleSheet(u"QPushButton#download_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#download_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_124.addWidget(self.download_button)

        self.horizontalSpacer_140 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_124.addItem(self.horizontalSpacer_140)


        self.verticalLayout_67.addLayout(self.horizontalLayout_124)

        self.label_92 = QLabel(self.received_reply)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.verticalLayout_67.addWidget(self.label_92)

        self.textEdit = QTextEdit(self.received_reply)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setStyleSheet(u"background-color: white;\n"
"border: 1px solid black;")
        self.textEdit.setReadOnly(True)

        self.verticalLayout_67.addWidget(self.textEdit)

        self.horizontalLayout_125 = QHBoxLayout()
        self.horizontalLayout_125.setObjectName(u"horizontalLayout_125")
        self.horizontalSpacer_141 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_125.addItem(self.horizontalSpacer_141)

        self.backBT2 = QPushButton(self.received_reply)
        self.backBT2.setObjectName(u"backBT2")
        self.backBT2.setStyleSheet(u"QPushButton#backBT2 {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#backBT2:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_125.addWidget(self.backBT2)

        self.horizontalSpacer_142 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_125.addItem(self.horizontalSpacer_142)


        self.verticalLayout_67.addLayout(self.horizontalLayout_125)

        self.stackedWidget_2.addWidget(self.received_reply)
        self.reject_lab_page = QWidget()
        self.reject_lab_page.setObjectName(u"reject_lab_page")
        self.verticalLayout_68 = QVBoxLayout(self.reject_lab_page)
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.horizontalLayout_129 = QHBoxLayout()
        self.horizontalLayout_129.setObjectName(u"horizontalLayout_129")
        self.horizontalSpacer_145 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_129.addItem(self.horizontalSpacer_145)

        self.label_94 = QLabel(self.reject_lab_page)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_129.addWidget(self.label_94)

        self.horizontalSpacer_146 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_129.addItem(self.horizontalSpacer_146)


        self.verticalLayout_68.addLayout(self.horizontalLayout_129)

        self.horizontalLayout_133 = QHBoxLayout()
        self.horizontalLayout_133.setObjectName(u"horizontalLayout_133")
        self.dat_request_6 = QLabel(self.reject_lab_page)
        self.dat_request_6.setObjectName(u"dat_request_6")
        self.dat_request_6.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_133.addWidget(self.dat_request_6)

        self.date_request_5 = QLabel(self.reject_lab_page)
        self.date_request_5.setObjectName(u"date_request_5")
        self.date_request_5.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_133.addWidget(self.date_request_5)


        self.verticalLayout_68.addLayout(self.horizontalLayout_133)

        self.horizontalLayout_134 = QHBoxLayout()
        self.horizontalLayout_134.setObjectName(u"horizontalLayout_134")
        self.label_98 = QLabel(self.reject_lab_page)
        self.label_98.setObjectName(u"label_98")
        self.label_98.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_134.addWidget(self.label_98)

        self.case_type_5 = QLabel(self.reject_lab_page)
        self.case_type_5.setObjectName(u"case_type_5")
        self.case_type_5.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_134.addWidget(self.case_type_5)

        self.horizontalSpacer_149 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_134.addItem(self.horizontalSpacer_149)


        self.verticalLayout_68.addLayout(self.horizontalLayout_134)

        self.horizontalLayout_135 = QHBoxLayout()
        self.horizontalLayout_135.setObjectName(u"horizontalLayout_135")
        self.label_99 = QLabel(self.reject_lab_page)
        self.label_99.setObjectName(u"label_99")
        self.label_99.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_135.addWidget(self.label_99)

        self.lab_request_hn_no_5 = QLabel(self.reject_lab_page)
        self.lab_request_hn_no_5.setObjectName(u"lab_request_hn_no_5")
        self.lab_request_hn_no_5.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_135.addWidget(self.lab_request_hn_no_5)

        self.label_100 = QLabel(self.reject_lab_page)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setStyleSheet(u"font:15pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_135.addWidget(self.label_100)

        self.lab_request_patient_name_5 = QLabel(self.reject_lab_page)
        self.lab_request_patient_name_5.setObjectName(u"lab_request_patient_name_5")
        self.lab_request_patient_name_5.setStyleSheet(u"font:15pt;")

        self.horizontalLayout_135.addWidget(self.lab_request_patient_name_5)


        self.verticalLayout_68.addLayout(self.horizontalLayout_135)

        self.horizontalLayout_136 = QHBoxLayout()
        self.horizontalLayout_136.setObjectName(u"horizontalLayout_136")
        self.horizontalSpacer_147 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_147)

        self.label_101 = QLabel(self.reject_lab_page)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setStyleSheet(u"font:30pt;\n"
"font-weight: bold; \n"
"color: red;")

        self.horizontalLayout_136.addWidget(self.label_101)

        self.horizontalSpacer_148 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_136.addItem(self.horizontalSpacer_148)


        self.verticalLayout_68.addLayout(self.horizontalLayout_136)

        self.horizontalLayout_137 = QHBoxLayout()
        self.horizontalLayout_137.setObjectName(u"horizontalLayout_137")
        self.horizontalSpacer_150 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_150)

        self.backBT3 = QPushButton(self.reject_lab_page)
        self.backBT3.setObjectName(u"backBT3")
        self.backBT3.setStyleSheet(u"QPushButton#backBT3 {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#backBT3:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_137.addWidget(self.backBT3)

        self.horizontalSpacer_151 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_137.addItem(self.horizontalSpacer_151)


        self.verticalLayout_68.addLayout(self.horizontalLayout_137)

        self.verticalSpacer_18 = QSpacerItem(20, 1446, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_68.addItem(self.verticalSpacer_18)

        self.stackedWidget_2.addWidget(self.reject_lab_page)
        self.bill_list_page = QWidget()
        self.bill_list_page.setObjectName(u"bill_list_page")
        self.verticalLayout_69 = QVBoxLayout(self.bill_list_page)
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.horizontalLayout_146 = QHBoxLayout()
        self.horizontalLayout_146.setObjectName(u"horizontalLayout_146")
        self.horizontalSpacer_163 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_163)

        self.label_95 = QLabel(self.bill_list_page)
        self.label_95.setObjectName(u"label_95")
        self.label_95.setStyleSheet(u"font: 30pt;\n"
"font-weight: bold;")

        self.horizontalLayout_146.addWidget(self.label_95)

        self.horizontalSpacer_164 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_146.addItem(self.horizontalSpacer_164)


        self.verticalLayout_69.addLayout(self.horizontalLayout_146)

        self.horizontalLayout_147 = QHBoxLayout()
        self.horizontalLayout_147.setObjectName(u"horizontalLayout_147")
        self.horizontalSpacer_165 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_147.addItem(self.horizontalSpacer_165)

        self.doctor_view_bill_button = QPushButton(self.bill_list_page)
        self.doctor_view_bill_button.setObjectName(u"doctor_view_bill_button")
        self.doctor_view_bill_button.setStyleSheet(u"QPushButton#doctor_view_bill_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#doctor_view_bill_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_147.addWidget(self.doctor_view_bill_button)


        self.verticalLayout_69.addLayout(self.horizontalLayout_147)

        self.doctor_bill_list_table = QTableWidget(self.bill_list_page)
        if (self.doctor_bill_list_table.columnCount() < 6):
            self.doctor_bill_list_table.setColumnCount(6)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.doctor_bill_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.doctor_bill_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        self.doctor_bill_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.doctor_bill_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.doctor_bill_list_table.setHorizontalHeaderItem(4, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.doctor_bill_list_table.setHorizontalHeaderItem(5, __qtablewidgetitem64)
        self.doctor_bill_list_table.setObjectName(u"doctor_bill_list_table")
        self.doctor_bill_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.doctor_bill_list_table.horizontalHeader().setStretchLastSection(True)
        self.doctor_bill_list_table.verticalHeader().setVisible(False)

        self.verticalLayout_69.addWidget(self.doctor_bill_list_table)

        self.stackedWidget_2.addWidget(self.bill_list_page)
        self.bill_page_2 = QWidget()
        self.bill_page_2.setObjectName(u"bill_page_2")
        self.verticalLayout_70 = QVBoxLayout(self.bill_page_2)
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.horizontalLayout_148 = QHBoxLayout()
        self.horizontalLayout_148.setObjectName(u"horizontalLayout_148")
        self.horizontalSpacer_166 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_166)

        self.label_96 = QLabel(self.bill_page_2)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setStyleSheet(u"font: 30pt;\n"
"font-weight: bold;")

        self.horizontalLayout_148.addWidget(self.label_96)

        self.horizontalSpacer_167 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_148.addItem(self.horizontalSpacer_167)


        self.verticalLayout_70.addLayout(self.horizontalLayout_148)

        self.horizontalLayout_149 = QHBoxLayout()
        self.horizontalLayout_149.setObjectName(u"horizontalLayout_149")
        self.horizontalLayout_150 = QHBoxLayout()
        self.horizontalLayout_150.setObjectName(u"horizontalLayout_150")
        self.label_102 = QLabel(self.bill_page_2)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_150.addWidget(self.label_102)

        self.bill_number_2 = QLabel(self.bill_page_2)
        self.bill_number_2.setObjectName(u"bill_number_2")
        self.bill_number_2.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_150.addWidget(self.bill_number_2)


        self.horizontalLayout_149.addLayout(self.horizontalLayout_150)

        self.horizontalSpacer_168 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_149.addItem(self.horizontalSpacer_168)


        self.verticalLayout_70.addLayout(self.horizontalLayout_149)

        self.horizontalLayout_151 = QHBoxLayout()
        self.horizontalLayout_151.setObjectName(u"horizontalLayout_151")
        self.horizontalLayout_152 = QHBoxLayout()
        self.horizontalLayout_152.setObjectName(u"horizontalLayout_152")
        self.label_103 = QLabel(self.bill_page_2)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_152.addWidget(self.label_103)

        self.bill_date_2 = QLabel(self.bill_page_2)
        self.bill_date_2.setObjectName(u"bill_date_2")
        self.bill_date_2.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_152.addWidget(self.bill_date_2)


        self.horizontalLayout_151.addLayout(self.horizontalLayout_152)

        self.horizontalSpacer_169 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_151.addItem(self.horizontalSpacer_169)


        self.verticalLayout_70.addLayout(self.horizontalLayout_151)

        self.horizontalLayout_153 = QHBoxLayout()
        self.horizontalLayout_153.setObjectName(u"horizontalLayout_153")
        self.label_104 = QLabel(self.bill_page_2)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setStyleSheet(u"font: 20pt;\n"
"font-weight: bold;")

        self.horizontalLayout_153.addWidget(self.label_104)

        self.horizontalSpacer_170 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_153.addItem(self.horizontalSpacer_170)


        self.verticalLayout_70.addLayout(self.horizontalLayout_153)

        self.horizontalLayout_155 = QHBoxLayout()
        self.horizontalLayout_155.setObjectName(u"horizontalLayout_155")
        self.label_106 = QLabel(self.bill_page_2)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_155.addWidget(self.label_106)

        self.bill_patient_name_2 = QLabel(self.bill_page_2)
        self.bill_patient_name_2.setObjectName(u"bill_patient_name_2")
        self.bill_patient_name_2.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_155.addWidget(self.bill_patient_name_2)

        self.horizontalSpacer_172 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_155.addItem(self.horizontalSpacer_172)


        self.verticalLayout_70.addLayout(self.horizontalLayout_155)

        self.horizontalLayout_154 = QHBoxLayout()
        self.horizontalLayout_154.setObjectName(u"horizontalLayout_154")
        self.label_105 = QLabel(self.bill_page_2)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_154.addWidget(self.label_105)

        self.bill_patient_hn_no_2 = QLabel(self.bill_page_2)
        self.bill_patient_hn_no_2.setObjectName(u"bill_patient_hn_no_2")
        self.bill_patient_hn_no_2.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_154.addWidget(self.bill_patient_hn_no_2)

        self.horizontalSpacer_171 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_154.addItem(self.horizontalSpacer_171)


        self.verticalLayout_70.addLayout(self.horizontalLayout_154)

        self.horizontalLayout_156 = QHBoxLayout()
        self.horizontalLayout_156.setObjectName(u"horizontalLayout_156")
        self.label_107 = QLabel(self.bill_page_2)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_156.addWidget(self.label_107)

        self.bill_total_charge_2 = QLabel(self.bill_page_2)
        self.bill_total_charge_2.setObjectName(u"bill_total_charge_2")
        self.bill_total_charge_2.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_156.addWidget(self.bill_total_charge_2)

        self.horizontalSpacer_173 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_156.addItem(self.horizontalSpacer_173)


        self.verticalLayout_70.addLayout(self.horizontalLayout_156)

        self.horizontalLayout_159 = QHBoxLayout()
        self.horizontalLayout_159.setObjectName(u"horizontalLayout_159")
        self.label_110 = QLabel(self.bill_page_2)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_159.addWidget(self.label_110)

        self.bill_status_2 = QLabel(self.bill_page_2)
        self.bill_status_2.setObjectName(u"bill_status_2")
        self.bill_status_2.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_159.addWidget(self.bill_status_2)

        self.horizontalSpacer_176 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_159.addItem(self.horizontalSpacer_176)


        self.verticalLayout_70.addLayout(self.horizontalLayout_159)

        self.horizontalLayout_157 = QHBoxLayout()
        self.horizontalLayout_157.setObjectName(u"horizontalLayout_157")
        self.horizontalSpacer_174 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_157.addItem(self.horizontalSpacer_174)

        self.confirm_payment_button = QPushButton(self.bill_page_2)
        self.confirm_payment_button.setObjectName(u"confirm_payment_button")
        self.confirm_payment_button.setStyleSheet(u"QPushButton#confirm_payment_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#confirm_payment_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_157.addWidget(self.confirm_payment_button)


        self.verticalLayout_70.addLayout(self.horizontalLayout_157)

        self.bill_table_2 = QTableWidget(self.bill_page_2)
        if (self.bill_table_2.columnCount() < 2):
            self.bill_table_2.setColumnCount(2)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.bill_table_2.setHorizontalHeaderItem(0, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.bill_table_2.setHorizontalHeaderItem(1, __qtablewidgetitem66)
        self.bill_table_2.setObjectName(u"bill_table_2")
        self.bill_table_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.bill_table_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.bill_table_2.horizontalHeader().setDefaultSectionSize(200)
        self.bill_table_2.horizontalHeader().setStretchLastSection(True)
        self.bill_table_2.verticalHeader().setVisible(False)
        self.bill_table_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_70.addWidget(self.bill_table_2)

        self.stackedWidget_2.addWidget(self.bill_page_2)

        self.horizontalLayout_2.addWidget(self.stackedWidget_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_2.addWidget(self.scrollArea)


        self.horizontalLayout_19.addWidget(self.main_widget)

        self.stackedWidget.addWidget(self.doctor_sidebar)
        self.patient_sidebar = QWidget()
        self.patient_sidebar.setObjectName(u"patient_sidebar")
        self.gridLayout = QGridLayout(self.patient_sidebar)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.main_widget_2 = QWidget(self.patient_sidebar)
        self.main_widget_2.setObjectName(u"main_widget_2")
        self.verticalLayout_38 = QVBoxLayout(self.main_widget_2)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.header_widget_2 = QWidget(self.main_widget_2)
        self.header_widget_2.setObjectName(u"header_widget_2")
        self.header_widget_2.setStyleSheet(u"QWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	margin: 0;\n"
"}")
        self.horizontalLayout_39 = QHBoxLayout(self.header_widget_2)
        self.horizontalLayout_39.setSpacing(7)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(12, 12, 12, -1)
        self.horizontalSpacer_45 = QSpacerItem(93, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_39.addItem(self.horizontalSpacer_45)

        self.Username_2 = QLabel(self.header_widget_2)
        self.Username_2.setObjectName(u"Username_2")

        self.horizontalLayout_39.addWidget(self.Username_2)

        self.userprofile_pic_2 = QPushButton(self.header_widget_2)
        self.userprofile_pic_2.setObjectName(u"userprofile_pic_2")
        self.userprofile_pic_2.setIcon(icon1)
        self.userprofile_pic_2.setIconSize(QSize(30, 30))

        self.horizontalLayout_39.addWidget(self.userprofile_pic_2)


        self.verticalLayout_38.addWidget(self.header_widget_2)

        self.scrollArea_2 = QScrollArea(self.main_widget_2)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setMaximumSize(QSize(1280, 10000))
        self.scrollArea_2.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"\n"
"")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 744, 1696))
        self.scrollAreaWidgetContents_2.setMaximumSize(QSize(1280, 16777215))
        self.horizontalLayout_40 = QHBoxLayout(self.scrollAreaWidgetContents_2)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget_3 = QStackedWidget(self.scrollAreaWidgetContents_2)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setMinimumSize(QSize(0, 0))
        self.medical_record_page_2 = QWidget()
        self.medical_record_page_2.setObjectName(u"medical_record_page_2")
        self.verticalLayout_44 = QVBoxLayout(self.medical_record_page_2)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.medical_record_widget_2 = QWidget(self.medical_record_page_2)
        self.medical_record_widget_2.setObjectName(u"medical_record_widget_2")
        self.medical_record_widget_2.setMinimumSize(QSize(0, 0))
        self.verticalLayout_49 = QVBoxLayout(self.medical_record_widget_2)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_patient_info_2 = QLabel(self.medical_record_widget_2)
        self.label_patient_info_2.setObjectName(u"label_patient_info_2")
        self.label_patient_info_2.setStyleSheet(u"font:20pt;\n"
"font-weight: bold; ")

        self.verticalLayout_49.addWidget(self.label_patient_info_2)

        self.horizontalLayout_93 = QHBoxLayout()
        self.horizontalLayout_93.setObjectName(u"horizontalLayout_93")
        self.patient_info1_widget_2 = QWidget(self.medical_record_widget_2)
        self.patient_info1_widget_2.setObjectName(u"patient_info1_widget_2")
        self.patient_info1_widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_45 = QVBoxLayout(self.patient_info1_widget_2)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalSpacer_53 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_53)

        self.med_record_photo = QLabel(self.patient_info1_widget_2)
        self.med_record_photo.setObjectName(u"med_record_photo")
        self.med_record_photo.setPixmap(QPixmap(u":/static/icons8-user-48.png"))

        self.horizontalLayout_46.addWidget(self.med_record_photo)

        self.horizontalSpacer_54 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_46.addItem(self.horizontalSpacer_54)


        self.verticalLayout_45.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalSpacer_55 = QSpacerItem(68, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_55)

        self.med_record_name = QLabel(self.patient_info1_widget_2)
        self.med_record_name.setObjectName(u"med_record_name")

        self.horizontalLayout_47.addWidget(self.med_record_name)

        self.horizontalSpacer_56 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_47.addItem(self.horizontalSpacer_56)


        self.verticalLayout_45.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_90 = QHBoxLayout()
        self.horizontalLayout_90.setObjectName(u"horizontalLayout_90")
        self.label_52 = QLabel(self.patient_info1_widget_2)
        self.label_52.setObjectName(u"label_52")

        self.horizontalLayout_90.addWidget(self.label_52)

        self.med_record_hn_no = QLabel(self.patient_info1_widget_2)
        self.med_record_hn_no.setObjectName(u"med_record_hn_no")

        self.horizontalLayout_90.addWidget(self.med_record_hn_no)


        self.verticalLayout_45.addLayout(self.horizontalLayout_90)

        self.horizontalLayout_162 = QHBoxLayout()
        self.horizontalLayout_162.setObjectName(u"horizontalLayout_162")
        self.label_113 = QLabel(self.patient_info1_widget_2)
        self.label_113.setObjectName(u"label_113")

        self.horizontalLayout_162.addWidget(self.label_113)

        self.patient_email_display_2 = QLabel(self.patient_info1_widget_2)
        self.patient_email_display_2.setObjectName(u"patient_email_display_2")

        self.horizontalLayout_162.addWidget(self.patient_email_display_2)


        self.verticalLayout_45.addLayout(self.horizontalLayout_162)

        self.horizontalLayout_91 = QHBoxLayout()
        self.horizontalLayout_91.setObjectName(u"horizontalLayout_91")
        self.label_27 = QLabel(self.patient_info1_widget_2)
        self.label_27.setObjectName(u"label_27")

        self.horizontalLayout_91.addWidget(self.label_27)

        self.med_record_dob = QLabel(self.patient_info1_widget_2)
        self.med_record_dob.setObjectName(u"med_record_dob")

        self.horizontalLayout_91.addWidget(self.med_record_dob)


        self.verticalLayout_45.addLayout(self.horizontalLayout_91)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.label_28 = QLabel(self.patient_info1_widget_2)
        self.label_28.setObjectName(u"label_28")

        self.horizontalLayout_45.addWidget(self.label_28)

        self.med_record_sex = QLabel(self.patient_info1_widget_2)
        self.med_record_sex.setObjectName(u"med_record_sex")

        self.horizontalLayout_45.addWidget(self.med_record_sex)


        self.verticalLayout_45.addLayout(self.horizontalLayout_45)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_29 = QLabel(self.patient_info1_widget_2)
        self.label_29.setObjectName(u"label_29")

        self.horizontalLayout_48.addWidget(self.label_29)

        self.med_record_age = QLabel(self.patient_info1_widget_2)
        self.med_record_age.setObjectName(u"med_record_age")

        self.horizontalLayout_48.addWidget(self.med_record_age)


        self.verticalLayout_45.addLayout(self.horizontalLayout_48)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_30 = QLabel(self.patient_info1_widget_2)
        self.label_30.setObjectName(u"label_30")

        self.horizontalLayout_49.addWidget(self.label_30)

        self.med_record_weight = QLabel(self.patient_info1_widget_2)
        self.med_record_weight.setObjectName(u"med_record_weight")

        self.horizontalLayout_49.addWidget(self.med_record_weight)


        self.verticalLayout_45.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_31 = QLabel(self.patient_info1_widget_2)
        self.label_31.setObjectName(u"label_31")

        self.horizontalLayout_50.addWidget(self.label_31)

        self.med_record_height = QLabel(self.patient_info1_widget_2)
        self.med_record_height.setObjectName(u"med_record_height")

        self.horizontalLayout_50.addWidget(self.med_record_height)


        self.verticalLayout_45.addLayout(self.horizontalLayout_50)


        self.horizontalLayout_93.addWidget(self.patient_info1_widget_2)

        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.patient_info2_widget_2 = QWidget(self.medical_record_widget_2)
        self.patient_info2_widget_2.setObjectName(u"patient_info2_widget_2")
        self.patient_info2_widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_48 = QVBoxLayout(self.patient_info2_widget_2)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.label_address_2 = QLabel(self.patient_info2_widget_2)
        self.label_address_2.setObjectName(u"label_address_2")

        self.horizontalLayout_51.addWidget(self.label_address_2)

        self.horizontalSpacer_59 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_51.addItem(self.horizontalSpacer_59)

        self.med_record_address = QLabel(self.patient_info2_widget_2)
        self.med_record_address.setObjectName(u"med_record_address")

        self.horizontalLayout_51.addWidget(self.med_record_address)


        self.verticalLayout_48.addLayout(self.horizontalLayout_51)

        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_tel_no_2 = QLabel(self.patient_info2_widget_2)
        self.label_tel_no_2.setObjectName(u"label_tel_no_2")

        self.horizontalLayout_52.addWidget(self.label_tel_no_2)

        self.horizontalSpacer_60 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_52.addItem(self.horizontalSpacer_60)

        self.med_record_tel = QLabel(self.patient_info2_widget_2)
        self.med_record_tel.setObjectName(u"med_record_tel")

        self.horizontalLayout_52.addWidget(self.med_record_tel)


        self.verticalLayout_48.addLayout(self.horizontalLayout_52)


        self.verticalLayout_47.addWidget(self.patient_info2_widget_2)

        self.patient_info3_widget_2 = QWidget(self.medical_record_widget_2)
        self.patient_info3_widget_2.setObjectName(u"patient_info3_widget_2")
        self.patient_info3_widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_46 = QVBoxLayout(self.patient_info3_widget_2)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.horizontalSpacer_61 = QSpacerItem(88, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_61)

        self.label_blood_status_2 = QLabel(self.patient_info3_widget_2)
        self.label_blood_status_2.setObjectName(u"label_blood_status_2")
        self.label_blood_status_2.setStyleSheet(u"font: 15pt \"Microsoft Sans Serif\";\n"
"color: grey;")

        self.horizontalLayout_53.addWidget(self.label_blood_status_2)

        self.horizontalSpacer_62 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_53.addItem(self.horizontalSpacer_62)


        self.verticalLayout_46.addLayout(self.horizontalLayout_53)

        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.horizontalSpacer_63 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_63)

        self.blood_icon_2 = QLabel(self.patient_info3_widget_2)
        self.blood_icon_2.setObjectName(u"blood_icon_2")
        self.blood_icon_2.setBaseSize(QSize(0, 0))
        self.blood_icon_2.setPixmap(QPixmap(u":/static/icons8-blood-50.png"))

        self.horizontalLayout_54.addWidget(self.blood_icon_2)

        self.horizontalSpacer_64 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_54.addItem(self.horizontalSpacer_64)


        self.verticalLayout_46.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_92 = QHBoxLayout()
        self.horizontalLayout_92.setObjectName(u"horizontalLayout_92")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_4)

        self.med_record_blood_type = QLabel(self.patient_info3_widget_2)
        self.med_record_blood_type.setObjectName(u"med_record_blood_type")

        self.horizontalLayout_92.addWidget(self.med_record_blood_type)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_92.addItem(self.horizontalSpacer_5)


        self.verticalLayout_46.addLayout(self.horizontalLayout_92)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.horizontalSpacer_65 = QSpacerItem(78, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_65)

        self.med_record_blood_pressure = QLabel(self.patient_info3_widget_2)
        self.med_record_blood_pressure.setObjectName(u"med_record_blood_pressure")

        self.horizontalLayout_55.addWidget(self.med_record_blood_pressure)

        self.horizontalSpacer_66 = QSpacerItem(98, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_55.addItem(self.horizontalSpacer_66)


        self.verticalLayout_46.addLayout(self.horizontalLayout_55)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.horizontalSpacer_67 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_67)

        self.med_record_blood_warning = QLabel(self.patient_info3_widget_2)
        self.med_record_blood_warning.setObjectName(u"med_record_blood_warning")

        self.horizontalLayout_56.addWidget(self.med_record_blood_warning)

        self.horizontalSpacer_68 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_56.addItem(self.horizontalSpacer_68)


        self.verticalLayout_46.addLayout(self.horizontalLayout_56)


        self.verticalLayout_47.addWidget(self.patient_info3_widget_2)


        self.horizontalLayout_93.addLayout(self.verticalLayout_47)


        self.verticalLayout_49.addLayout(self.horizontalLayout_93)

        self.medical_history_widget_2 = QWidget(self.medical_record_widget_2)
        self.medical_history_widget_2.setObjectName(u"medical_history_widget_2")
        self.medical_history_widget_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.verticalLayout_50 = QVBoxLayout(self.medical_history_widget_2)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_medical_history_2 = QLabel(self.medical_history_widget_2)
        self.label_medical_history_2.setObjectName(u"label_medical_history_2")
        self.label_medical_history_2.setStyleSheet(u"")

        self.verticalLayout_50.addWidget(self.label_medical_history_2)

        self.label_past_treatment_7 = QLabel(self.medical_history_widget_2)
        self.label_past_treatment_7.setObjectName(u"label_past_treatment_7")

        self.verticalLayout_50.addWidget(self.label_past_treatment_7)

        self.vaccine_list_table_3 = QTableWidget(self.medical_history_widget_2)
        if (self.vaccine_list_table_3.columnCount() < 2):
            self.vaccine_list_table_3.setColumnCount(2)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.vaccine_list_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.vaccine_list_table_3.setHorizontalHeaderItem(1, __qtablewidgetitem68)
        self.vaccine_list_table_3.setObjectName(u"vaccine_list_table_3")
        self.vaccine_list_table_3.setMinimumSize(QSize(0, 300))
        self.vaccine_list_table_3.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.vaccine_list_table_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.vaccine_list_table_3.horizontalHeader().setDefaultSectionSize(300)
        self.vaccine_list_table_3.horizontalHeader().setStretchLastSection(True)
        self.vaccine_list_table_3.verticalHeader().setVisible(False)
        self.vaccine_list_table_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_50.addWidget(self.vaccine_list_table_3)

        self.label_past_treatment_8 = QLabel(self.medical_history_widget_2)
        self.label_past_treatment_8.setObjectName(u"label_past_treatment_8")

        self.verticalLayout_50.addWidget(self.label_past_treatment_8)

        self.medication_list_table_3 = QTableWidget(self.medical_history_widget_2)
        if (self.medication_list_table_3.columnCount() < 8):
            self.medication_list_table_3.setColumnCount(8)
        __qtablewidgetitem69 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(1, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(2, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(3, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(4, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(5, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(6, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.medication_list_table_3.setHorizontalHeaderItem(7, __qtablewidgetitem76)
        self.medication_list_table_3.setObjectName(u"medication_list_table_3")
        self.medication_list_table_3.setMinimumSize(QSize(0, 300))
        self.medication_list_table_3.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.medication_list_table_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.medication_list_table_3.horizontalHeader().setDefaultSectionSize(200)
        self.medication_list_table_3.horizontalHeader().setStretchLastSection(True)
        self.medication_list_table_3.verticalHeader().setVisible(False)
        self.medication_list_table_3.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_50.addWidget(self.medication_list_table_3)

        self.label_allergies_2 = QLabel(self.medical_history_widget_2)
        self.label_allergies_2.setObjectName(u"label_allergies_2")

        self.verticalLayout_50.addWidget(self.label_allergies_2)

        self.allergy_list_table_3 = QTableWidget(self.medical_history_widget_2)
        if (self.allergy_list_table_3.columnCount() < 1):
            self.allergy_list_table_3.setColumnCount(1)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.allergy_list_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem77)
        self.allergy_list_table_3.setObjectName(u"allergy_list_table_3")
        self.allergy_list_table_3.setMinimumSize(QSize(0, 300))
        self.allergy_list_table_3.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.allergy_list_table_3.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.allergy_list_table_3.horizontalHeader().setStretchLastSection(True)
        self.allergy_list_table_3.verticalHeader().setVisible(False)

        self.verticalLayout_50.addWidget(self.allergy_list_table_3)

        self.label_past_treatment_6 = QLabel(self.medical_history_widget_2)
        self.label_past_treatment_6.setObjectName(u"label_past_treatment_6")

        self.verticalLayout_50.addWidget(self.label_past_treatment_6)

        self.lab_test_list_table_3 = QTableWidget(self.medical_history_widget_2)
        if (self.lab_test_list_table_3.columnCount() < 5):
            self.lab_test_list_table_3.setColumnCount(5)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.lab_test_list_table_3.setHorizontalHeaderItem(0, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.lab_test_list_table_3.setHorizontalHeaderItem(1, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.lab_test_list_table_3.setHorizontalHeaderItem(2, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.lab_test_list_table_3.setHorizontalHeaderItem(3, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.lab_test_list_table_3.setHorizontalHeaderItem(4, __qtablewidgetitem82)
        self.lab_test_list_table_3.setObjectName(u"lab_test_list_table_3")
        self.lab_test_list_table_3.setMinimumSize(QSize(0, 300))
        self.lab_test_list_table_3.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.lab_test_list_table_3.horizontalHeader().setDefaultSectionSize(120)
        self.lab_test_list_table_3.horizontalHeader().setStretchLastSection(True)
        self.lab_test_list_table_3.verticalHeader().setVisible(False)

        self.verticalLayout_50.addWidget(self.lab_test_list_table_3)


        self.verticalLayout_49.addWidget(self.medical_history_widget_2)


        self.verticalLayout_44.addWidget(self.medical_record_widget_2)

        self.stackedWidget_3.addWidget(self.medical_record_page_2)
        self.schedule_page_2 = QWidget()
        self.schedule_page_2.setObjectName(u"schedule_page_2")
        self.verticalLayout_41 = QVBoxLayout(self.schedule_page_2)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_34 = QLabel(self.schedule_page_2)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"font: 20pt;\n"
"font-weight: bold;")

        self.horizontalLayout_43.addWidget(self.label_34)

        self.horizontalSpacer_72 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_72)


        self.verticalLayout_41.addLayout(self.horizontalLayout_43)

        self.horizontalLayout_57 = QHBoxLayout()
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_35 = QLabel(self.schedule_page_2)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"font: 12pt;")

        self.horizontalLayout_57.addWidget(self.label_35)

        self.appointment_date = QDateEdit(self.schedule_page_2)
        self.appointment_date.setObjectName(u"appointment_date")
        self.appointment_date.setStyleSheet(u"background-color: white;")

        self.horizontalLayout_57.addWidget(self.appointment_date)

        self.search_date_button = QPushButton(self.schedule_page_2)
        self.search_date_button.setObjectName(u"search_date_button")
        self.search_date_button.setIcon(icon17)
        self.search_date_button.setIconSize(QSize(40, 40))

        self.horizontalLayout_57.addWidget(self.search_date_button)

        self.horizontalSpacer_71 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_57.addItem(self.horizontalSpacer_71)

        self.cancel_appointment = QPushButton(self.schedule_page_2)
        self.cancel_appointment.setObjectName(u"cancel_appointment")
        self.cancel_appointment.setStyleSheet(u"QPushButton#cancel_appointment {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#cancel_appointment:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_57.addWidget(self.cancel_appointment)

        self.new_appointment_button = QPushButton(self.schedule_page_2)
        self.new_appointment_button.setObjectName(u"new_appointment_button")
        self.new_appointment_button.setStyleSheet(u"QPushButton#new_appointment_button {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#new_appointment_button:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_57.addWidget(self.new_appointment_button)


        self.verticalLayout_41.addLayout(self.horizontalLayout_57)

        self.patient_schedule_table = QTableWidget(self.schedule_page_2)
        if (self.patient_schedule_table.columnCount() < 3):
            self.patient_schedule_table.setColumnCount(3)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.patient_schedule_table.setHorizontalHeaderItem(0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.patient_schedule_table.setHorizontalHeaderItem(1, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.patient_schedule_table.setHorizontalHeaderItem(2, __qtablewidgetitem85)
        self.patient_schedule_table.setObjectName(u"patient_schedule_table")
        self.patient_schedule_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.patient_schedule_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.patient_schedule_table.horizontalHeader().setStretchLastSection(True)
        self.patient_schedule_table.verticalHeader().setVisible(False)
        self.patient_schedule_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_41.addWidget(self.patient_schedule_table)

        self.stackedWidget_3.addWidget(self.schedule_page_2)
        self.bill_page = QWidget()
        self.bill_page.setObjectName(u"bill_page")
        self.verticalLayout_40 = QVBoxLayout(self.bill_page)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_131 = QHBoxLayout()
        self.horizontalLayout_131.setObjectName(u"horizontalLayout_131")
        self.horizontalSpacer_156 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_156)

        self.label_26 = QLabel(self.bill_page)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"font: 30pt;\n"
"font-weight: bold;")

        self.horizontalLayout_131.addWidget(self.label_26)

        self.horizontalSpacer_155 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_131.addItem(self.horizontalSpacer_155)


        self.verticalLayout_40.addLayout(self.horizontalLayout_131)

        self.horizontalLayout_140 = QHBoxLayout()
        self.horizontalLayout_140.setObjectName(u"horizontalLayout_140")
        self.horizontalLayout_138 = QHBoxLayout()
        self.horizontalLayout_138.setObjectName(u"horizontalLayout_138")
        self.label_32 = QLabel(self.bill_page)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_138.addWidget(self.label_32)

        self.bill_number = QLabel(self.bill_page)
        self.bill_number.setObjectName(u"bill_number")
        self.bill_number.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_138.addWidget(self.bill_number)


        self.horizontalLayout_140.addLayout(self.horizontalLayout_138)

        self.horizontalSpacer_50 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_140.addItem(self.horizontalSpacer_50)


        self.verticalLayout_40.addLayout(self.horizontalLayout_140)

        self.horizontalLayout_132 = QHBoxLayout()
        self.horizontalLayout_132.setObjectName(u"horizontalLayout_132")
        self.horizontalLayout_139 = QHBoxLayout()
        self.horizontalLayout_139.setObjectName(u"horizontalLayout_139")
        self.label_37 = QLabel(self.bill_page)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_139.addWidget(self.label_37)

        self.bill_date = QLabel(self.bill_page)
        self.bill_date.setObjectName(u"bill_date")
        self.bill_date.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_139.addWidget(self.bill_date)


        self.horizontalLayout_132.addLayout(self.horizontalLayout_139)

        self.horizontalSpacer_51 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_132.addItem(self.horizontalSpacer_51)


        self.verticalLayout_40.addLayout(self.horizontalLayout_132)

        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_38 = QLabel(self.bill_page)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setStyleSheet(u"font: 20pt;\n"
"font-weight: bold;")

        self.horizontalLayout_63.addWidget(self.label_38)

        self.horizontalSpacer_69 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_63.addItem(self.horizontalSpacer_69)


        self.verticalLayout_40.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.label_39 = QLabel(self.bill_page)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_64.addWidget(self.label_39)

        self.bill_patient_name = QLabel(self.bill_page)
        self.bill_patient_name.setObjectName(u"bill_patient_name")
        self.bill_patient_name.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_64.addWidget(self.bill_patient_name)

        self.horizontalSpacer_70 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_64.addItem(self.horizontalSpacer_70)


        self.verticalLayout_40.addLayout(self.horizontalLayout_64)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.label_40 = QLabel(self.bill_page)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_65.addWidget(self.label_40)

        self.bill_patient_hn_no = QLabel(self.bill_page)
        self.bill_patient_hn_no.setObjectName(u"bill_patient_hn_no")
        self.bill_patient_hn_no.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_65.addWidget(self.bill_patient_hn_no)

        self.horizontalSpacer_73 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_65.addItem(self.horizontalSpacer_73)


        self.verticalLayout_40.addLayout(self.horizontalLayout_65)

        self.horizontalLayout_130 = QHBoxLayout()
        self.horizontalLayout_130.setObjectName(u"horizontalLayout_130")
        self.label_97 = QLabel(self.bill_page)
        self.label_97.setObjectName(u"label_97")
        self.label_97.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_130.addWidget(self.label_97)

        self.bill_total_charge = QLabel(self.bill_page)
        self.bill_total_charge.setObjectName(u"bill_total_charge")
        self.bill_total_charge.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_130.addWidget(self.bill_total_charge)

        self.horizontalSpacer_154 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_130.addItem(self.horizontalSpacer_154)


        self.verticalLayout_40.addLayout(self.horizontalLayout_130)

        self.horizontalLayout_158 = QHBoxLayout()
        self.horizontalLayout_158.setObjectName(u"horizontalLayout_158")
        self.label_109 = QLabel(self.bill_page)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_158.addWidget(self.label_109)

        self.bill_status = QLabel(self.bill_page)
        self.bill_status.setObjectName(u"bill_status")
        self.bill_status.setStyleSheet(u"font: 15pt;")

        self.horizontalLayout_158.addWidget(self.bill_status)

        self.horizontalSpacer_175 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_158.addItem(self.horizontalSpacer_175)


        self.verticalLayout_40.addLayout(self.horizontalLayout_158)

        self.horizontalLayout_144 = QHBoxLayout()
        self.horizontalLayout_144.setObjectName(u"horizontalLayout_144")
        self.horizontalSpacer_161 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_144.addItem(self.horizontalSpacer_161)

        self.label_33 = QLabel(self.bill_page)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setStyleSheet(u"font: 15pt;\n"
"font-weight: bold;")

        self.horizontalLayout_144.addWidget(self.label_33)

        self.select_discount = QComboBox(self.bill_page)
        self.select_discount.addItem("")
        self.select_discount.addItem("")
        self.select_discount.addItem("")
        self.select_discount.setObjectName(u"select_discount")
        self.select_discount.setMinimumSize(QSize(200, 0))
        self.select_discount.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_144.addWidget(self.select_discount)


        self.verticalLayout_40.addLayout(self.horizontalLayout_144)

        self.insurance = QWidget(self.bill_page)
        self.insurance.setObjectName(u"insurance")
        self.insurance.setStyleSheet(u"")
        self.horizontalLayout_145 = QHBoxLayout(self.insurance)
        self.horizontalLayout_145.setObjectName(u"horizontalLayout_145")
        self.horizontalSpacer_162 = QSpacerItem(268, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_145.addItem(self.horizontalSpacer_162)

        self.label_36 = QLabel(self.insurance)
        self.label_36.setObjectName(u"label_36")

        self.horizontalLayout_145.addWidget(self.label_36)

        self.insurance_value = QLineEdit(self.insurance)
        self.insurance_value.setObjectName(u"insurance_value")
        self.insurance_value.setEnabled(True)
        self.insurance_value.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_145.addWidget(self.insurance_value)


        self.verticalLayout_40.addWidget(self.insurance)

        self.horizontalLayout_143 = QHBoxLayout()
        self.horizontalLayout_143.setObjectName(u"horizontalLayout_143")
        self.horizontalSpacer_160 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_143.addItem(self.horizontalSpacer_160)

        self.apply_discount_button = QPushButton(self.bill_page)
        self.apply_discount_button.setObjectName(u"apply_discount_button")
        self.apply_discount_button.setStyleSheet(u"QPushButton#apply_discount_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#apply_discount_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_143.addWidget(self.apply_discount_button)


        self.verticalLayout_40.addLayout(self.horizontalLayout_143)

        self.bill_table = QTableWidget(self.bill_page)
        if (self.bill_table.columnCount() < 2):
            self.bill_table.setColumnCount(2)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.bill_table.setHorizontalHeaderItem(0, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.bill_table.setHorizontalHeaderItem(1, __qtablewidgetitem87)
        self.bill_table.setObjectName(u"bill_table")
        self.bill_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.bill_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.bill_table.horizontalHeader().setDefaultSectionSize(200)
        self.bill_table.horizontalHeader().setStretchLastSection(True)
        self.bill_table.verticalHeader().setVisible(False)
        self.bill_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_40.addWidget(self.bill_table)

        self.stackedWidget_3.addWidget(self.bill_page)
        self.bill_list_page_2 = QWidget()
        self.bill_list_page_2.setObjectName(u"bill_list_page_2")
        self.verticalLayout_39 = QVBoxLayout(self.bill_list_page_2)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.horizontalLayout_141 = QHBoxLayout()
        self.horizontalLayout_141.setObjectName(u"horizontalLayout_141")
        self.horizontalSpacer_157 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_157)

        self.label_25 = QLabel(self.bill_list_page_2)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setStyleSheet(u"font: 30pt;\n"
"font-weight: bold;")

        self.horizontalLayout_141.addWidget(self.label_25)

        self.horizontalSpacer_158 = QSpacerItem(40, 28, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_141.addItem(self.horizontalSpacer_158)


        self.verticalLayout_39.addLayout(self.horizontalLayout_141)

        self.horizontalLayout_142 = QHBoxLayout()
        self.horizontalLayout_142.setObjectName(u"horizontalLayout_142")
        self.horizontalSpacer_159 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_142.addItem(self.horizontalSpacer_159)

        self.view_bill_button = QPushButton(self.bill_list_page_2)
        self.view_bill_button.setObjectName(u"view_bill_button")
        self.view_bill_button.setStyleSheet(u"QPushButton#view_bill_button {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#view_bill_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_142.addWidget(self.view_bill_button)


        self.verticalLayout_39.addLayout(self.horizontalLayout_142)

        self.bill_list_table = QTableWidget(self.bill_list_page_2)
        if (self.bill_list_table.columnCount() < 4):
            self.bill_list_table.setColumnCount(4)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.bill_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        self.bill_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.bill_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.bill_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem91)
        self.bill_list_table.setObjectName(u"bill_list_table")
        self.bill_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.bill_list_table.horizontalHeader().setDefaultSectionSize(150)
        self.bill_list_table.horizontalHeader().setStretchLastSection(True)
        self.bill_list_table.verticalHeader().setVisible(False)

        self.verticalLayout_39.addWidget(self.bill_list_table)

        self.stackedWidget_3.addWidget(self.bill_list_page_2)

        self.horizontalLayout_40.addWidget(self.stackedWidget_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_38.addWidget(self.scrollArea_2)


        self.gridLayout.addWidget(self.main_widget_2, 0, 1, 1, 1)

        self.icon_name_widget_2 = QWidget(self.patient_sidebar)
        self.icon_name_widget_2.setObjectName(u"icon_name_widget_2")
        self.icon_name_widget_2.setStyleSheet(u"QWidget{\n"
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
        self.verticalLayout_37 = QVBoxLayout(self.icon_name_widget_2)
        self.verticalLayout_37.setSpacing(7)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, 12, 0, 12)
        self.menu_icon_2 = QPushButton(self.icon_name_widget_2)
        self.menu_icon_2.setObjectName(u"menu_icon_2")
        self.menu_icon_2.setMinimumSize(QSize(50, 50))
        self.menu_icon_2.setIcon(icon9)
        self.menu_icon_2.setIconSize(QSize(50, 50))

        self.verticalLayout_37.addWidget(self.menu_icon_2)

        self.home_Button_2 = QPushButton(self.icon_name_widget_2)
        self.home_Button_2.setObjectName(u"home_Button_2")
        self.home_Button_2.setMinimumSize(QSize(40, 40))
        self.home_Button_2.setIcon(icon10)
        self.home_Button_2.setIconSize(QSize(40, 40))
        self.home_Button_2.setCheckable(False)
        self.home_Button_2.setAutoExclusive(True)

        self.verticalLayout_37.addWidget(self.home_Button_2)

        self.viewMedRecord_button = QPushButton(self.icon_name_widget_2)
        self.viewMedRecord_button.setObjectName(u"viewMedRecord_button")
        self.viewMedRecord_button.setMinimumSize(QSize(40, 40))
        icon19 = QIcon()
        icon19.addFile(u":/static/med_record_white.png", QSize(), QIcon.Normal, QIcon.Off)
        self.viewMedRecord_button.setIcon(icon19)
        self.viewMedRecord_button.setIconSize(QSize(40, 40))
        self.viewMedRecord_button.setCheckable(True)
        self.viewMedRecord_button.setAutoExclusive(True)

        self.verticalLayout_37.addWidget(self.viewMedRecord_button)

        self.manageAppointmentButton = QPushButton(self.icon_name_widget_2)
        self.manageAppointmentButton.setObjectName(u"manageAppointmentButton")
        self.manageAppointmentButton.setMinimumSize(QSize(40, 40))
        icon20 = QIcon()
        icon20.addFile(u":/static/Schedule_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.manageAppointmentButton.setIcon(icon20)
        self.manageAppointmentButton.setIconSize(QSize(40, 40))
        self.manageAppointmentButton.setCheckable(True)
        self.manageAppointmentButton.setAutoExclusive(True)

        self.verticalLayout_37.addWidget(self.manageAppointmentButton)

        self.billPaymentButton = QPushButton(self.icon_name_widget_2)
        self.billPaymentButton.setObjectName(u"billPaymentButton")
        self.billPaymentButton.setMinimumSize(QSize(40, 40))
        icon21 = QIcon()
        icon21.addFile(u":/static/Payment_white_new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.billPaymentButton.setIcon(icon21)
        self.billPaymentButton.setIconSize(QSize(40, 40))
        self.billPaymentButton.setCheckable(True)
        self.billPaymentButton.setAutoExclusive(True)

        self.verticalLayout_37.addWidget(self.billPaymentButton)

        self.verticalSpacer_12 = QSpacerItem(20, 111, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_37.addItem(self.verticalSpacer_12)

        self.logout_button_2 = QPushButton(self.icon_name_widget_2)
        self.logout_button_2.setObjectName(u"logout_button_2")
        self.logout_button_2.setMinimumSize(QSize(40, 40))
        self.logout_button_2.setIcon(icon16)
        self.logout_button_2.setIconSize(QSize(40, 40))

        self.verticalLayout_37.addWidget(self.logout_button_2)


        self.gridLayout.addWidget(self.icon_name_widget_2, 0, 0, 1, 1)

        self.stackedWidget.addWidget(self.patient_sidebar)
        self.admin_page = QWidget()
        self.admin_page.setObjectName(u"admin_page")
        self.verticalLayout_56 = QVBoxLayout(self.admin_page)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.verticalSpacer_10 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_10)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_37 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_37)

        self.label = QLabel(self.admin_page)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"color: #EE99F3; font-size: 50px\n"
"px; font-weight: bold; font-family: Monospace;")

        self.horizontalLayout_26.addWidget(self.label)

        self.horizontalSpacer_42 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_42)


        self.verticalLayout_56.addLayout(self.horizontalLayout_26)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.directory = QLabel(self.admin_page)
        self.directory.setObjectName(u"directory")
        self.directory.setStyleSheet(u"")

        self.verticalLayout_28.addWidget(self.directory)

        self.doctor_profile = QLabel(self.admin_page)
        self.doctor_profile.setObjectName(u"doctor_profile")
        self.doctor_profile.setMinimumSize(QSize(100, 100))
        self.doctor_profile.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_28.addWidget(self.doctor_profile)

        self.take_pic_button_2 = QPushButton(self.admin_page)
        self.take_pic_button_2.setObjectName(u"take_pic_button_2")
        self.take_pic_button_2.setStyleSheet(u"QPushButton#take_pic_button_2 {\n"
"	background-color: black;\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#take_pic_button_2:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_28.addWidget(self.take_pic_button_2)

        self.browse_page_2 = QPushButton(self.admin_page)
        self.browse_page_2.setObjectName(u"browse_page_2")
        self.browse_page_2.setStyleSheet(u"QPushButton#browse_page_2 {\n"
"	background-color: grey;\n"
"	color: white;\n"
"	padding: 6px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#browse_page_2:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")

        self.verticalLayout_28.addWidget(self.browse_page_2)


        self.horizontalLayout_36.addLayout(self.verticalLayout_28)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.userName = QLabel(self.admin_page)
        self.userName.setObjectName(u"userName")
        self.userName.setStyleSheet(u"font:20pt;")

        self.verticalLayout_33.addWidget(self.userName)

        self.userName_2 = QLineEdit(self.admin_page)
        self.userName_2.setObjectName(u"userName_2")
        self.userName_2.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_33.addWidget(self.userName_2)


        self.verticalLayout_57.addLayout(self.verticalLayout_33)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.password_2 = QLabel(self.admin_page)
        self.password_2.setObjectName(u"password_2")
        self.password_2.setStyleSheet(u"font:20pt;")

        self.verticalLayout_34.addWidget(self.password_2)

        self.password_doctor = QLineEdit(self.admin_page)
        self.password_doctor.setObjectName(u"password_doctor")
        self.password_doctor.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_34.addWidget(self.password_doctor)

        self.doctor_email = QLabel(self.admin_page)
        self.doctor_email.setObjectName(u"doctor_email")
        self.doctor_email.setStyleSheet(u"font:20pt;")

        self.verticalLayout_34.addWidget(self.doctor_email)

        self.doctor_email_input = QLineEdit(self.admin_page)
        self.doctor_email_input.setObjectName(u"doctor_email_input")
        self.doctor_email_input.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_34.addWidget(self.doctor_email_input)


        self.verticalLayout_57.addLayout(self.verticalLayout_34)


        self.horizontalLayout_36.addLayout(self.verticalLayout_57)


        self.verticalLayout_56.addLayout(self.horizontalLayout_36)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.label_22 = QLabel(self.admin_page)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setStyleSheet(u"font:20pt;")

        self.verticalLayout_25.addWidget(self.label_22)

        self.firstName = QLineEdit(self.admin_page)
        self.firstName.setObjectName(u"firstName")
        self.firstName.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_25.addWidget(self.firstName)


        self.horizontalLayout_37.addLayout(self.verticalLayout_25)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.middleName2 = QLabel(self.admin_page)
        self.middleName2.setObjectName(u"middleName2")
        self.middleName2.setStyleSheet(u"font:20pt;")

        self.verticalLayout_31.addWidget(self.middleName2)

        self.middleName = QLineEdit(self.admin_page)
        self.middleName.setObjectName(u"middleName")
        self.middleName.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_31.addWidget(self.middleName)


        self.horizontalLayout_37.addLayout(self.verticalLayout_31)

        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.lastName2 = QLabel(self.admin_page)
        self.lastName2.setObjectName(u"lastName2")
        self.lastName2.setStyleSheet(u"font:20pt;")

        self.verticalLayout_32.addWidget(self.lastName2)

        self.lastName = QLineEdit(self.admin_page)
        self.lastName.setObjectName(u"lastName")
        self.lastName.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_32.addWidget(self.lastName)


        self.horizontalLayout_37.addLayout(self.verticalLayout_32)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.speciality2 = QLabel(self.admin_page)
        self.speciality2.setObjectName(u"speciality2")
        self.speciality2.setStyleSheet(u"font:20pt;")

        self.verticalLayout_35.addWidget(self.speciality2)

        self.speciality = QLineEdit(self.admin_page)
        self.speciality.setObjectName(u"speciality")
        self.speciality.setStyleSheet(u"font-size: 20px; background-color: white;")

        self.verticalLayout_35.addWidget(self.speciality)


        self.horizontalLayout_37.addLayout(self.verticalLayout_35)


        self.verticalLayout_56.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.horizontalSpacer_43 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_43)

        self.addDoctorButton = QPushButton(self.admin_page)
        self.addDoctorButton.setObjectName(u"addDoctorButton")
        self.addDoctorButton.setStyleSheet(u"QPushButton#addDoctorButton {\n"
"	background-color: #EE99F3; \n"
"	color: black;\n"
"	padding: 10px; 	\n"
"	border-radius: 10px; \n"
"    border-style: outset;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#addDoctorButton:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_38.addWidget(self.addDoctorButton)

        self.see_doctor_list_button = QPushButton(self.admin_page)
        self.see_doctor_list_button.setObjectName(u"see_doctor_list_button")
        self.see_doctor_list_button.setStyleSheet(u"QPushButton#see_doctor_list_button {\n"
"	background-color: #EE99F3; \n"
"	color: black;\n"
"	padding: 10px; 	\n"
"	border-radius: 10px; \n"
"    border-style: outset;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#see_doctor_list_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_38.addWidget(self.see_doctor_list_button)

        self.horizontalSpacer_44 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_38.addItem(self.horizontalSpacer_44)


        self.verticalLayout_56.addLayout(self.horizontalLayout_38)

        self.horizontalLayout_80 = QHBoxLayout()
        self.horizontalLayout_80.setObjectName(u"horizontalLayout_80")
        self.horizontalSpacer_75 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_75)

        self.logout_button_5 = QPushButton(self.admin_page)
        self.logout_button_5.setObjectName(u"logout_button_5")
        self.logout_button_5.setStyleSheet(u"QPushButton#logout_button_5 {\n"
"	background-color: #EE99F3; \n"
"	color: black;\n"
"	padding: 10px; 	\n"
"	border-radius: 10px; \n"
"    border-style: outset;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#logout_button_5:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_80.addWidget(self.logout_button_5)

        self.horizontalSpacer_76 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_80.addItem(self.horizontalSpacer_76)


        self.verticalLayout_56.addLayout(self.horizontalLayout_80)

        self.verticalSpacer_11 = QSpacerItem(20, 24, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_56.addItem(self.verticalSpacer_11)

        self.stackedWidget.addWidget(self.admin_page)
        self.doctor_list_page = QWidget()
        self.doctor_list_page.setObjectName(u"doctor_list_page")
        self.verticalLayout_43 = QVBoxLayout(self.doctor_list_page)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.horizontalLayout_79 = QHBoxLayout()
        self.horizontalLayout_79.setObjectName(u"horizontalLayout_79")
        self.label_53 = QLabel(self.doctor_list_page)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setStyleSheet(u"font:50pt;\n"
"font-weight: bold; ")

        self.horizontalLayout_79.addWidget(self.label_53)

        self.horizontalSpacer_99 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_79.addItem(self.horizontalSpacer_99)

        self.back_button = QPushButton(self.doctor_list_page)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setStyleSheet(u"QPushButton#back_button {\n"
"	background-color: #EE99F3; \n"
"	color: black;\n"
"	padding: 10px; 	\n"
"	border-radius: 10px; \n"
"    border-style: outset;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#back_button:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")

        self.horizontalLayout_79.addWidget(self.back_button)


        self.verticalLayout_43.addLayout(self.horizontalLayout_79)

        self.horizontalLayout_128 = QHBoxLayout()
        self.horizontalLayout_128.setObjectName(u"horizontalLayout_128")
        self.label_93 = QLabel(self.doctor_list_page)
        self.label_93.setObjectName(u"label_93")
        self.label_93.setStyleSheet(u"font:20pt;\n"
"")

        self.horizontalLayout_128.addWidget(self.label_93)

        self.search_username = QLineEdit(self.doctor_list_page)
        self.search_username.setObjectName(u"search_username")
        self.search_username.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.horizontalLayout_128.addWidget(self.search_username)

        self.search_username_button = QPushButton(self.doctor_list_page)
        self.search_username_button.setObjectName(u"search_username_button")
        self.search_username_button.setIcon(icon17)
        self.search_username_button.setIconSize(QSize(30, 30))

        self.horizontalLayout_128.addWidget(self.search_username_button)

        self.horizontalSpacer_144 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_128.addItem(self.horizontalSpacer_144)


        self.verticalLayout_43.addLayout(self.horizontalLayout_128)

        self.doctor_list_table = QTableWidget(self.doctor_list_page)
        if (self.doctor_list_table.columnCount() < 4):
            self.doctor_list_table.setColumnCount(4)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.doctor_list_table.setHorizontalHeaderItem(0, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.doctor_list_table.setHorizontalHeaderItem(1, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.doctor_list_table.setHorizontalHeaderItem(2, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.doctor_list_table.setHorizontalHeaderItem(3, __qtablewidgetitem95)
        self.doctor_list_table.setObjectName(u"doctor_list_table")
        self.doctor_list_table.setStyleSheet(u"QScrollBar{\n"
"	background-color: rgb(222, 224, 224);\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"	border: 1px solid black;\n"
"}\n"
"\n"
"QHeaderView::section{\n"
"	background-color: rgb(255, 237, 213);\n"
"	border: none;\n"
"	border-bottom: 1px solid black;\n"
"	padding: 3px 5px;\n"
"}\n"
"\n"
"QHeaderView::item{\n"
"	border-bottom: 1px solid black;\n"
"	background-color: rgb(255, 255, 246);\n"
"	text-align: left;\n"
"	padding-left: 3px;\n"
"}\n"
"\n"
"\n"
"")
        self.doctor_list_table.horizontalHeader().setDefaultSectionSize(150)
        self.doctor_list_table.horizontalHeader().setStretchLastSection(True)
        self.doctor_list_table.verticalHeader().setVisible(False)
        self.doctor_list_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_43.addWidget(self.doctor_list_table)

        self.stackedWidget.addWidget(self.doctor_list_page)

        self.verticalLayout_65.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(4)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.app_title_2.setText(QCoreApplication.translate("MainWindow", u"PatientSphere", None))
        self.app_title.setText(QCoreApplication.translate("MainWindow", u"PatientSphere", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LOG IN", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SIGN IN TO CONTINUE", None))
        self.username.setText("")
        self.username.setPlaceholderText(QCoreApplication.translate("MainWindow", u"HN NO./ USERNAME", None))
        self.password.setText("")
        self.password.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CITIZEN NO./PASSPORT NO./PASSWORD", None))
        self.show_password_button.setText("")
        self.loginButton.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.Username_6.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.doctor_setting_button.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Patient Sphere", None))
        self.home_patient_icon.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Manage Patient", None))
        self.home_lab_icon.setText("")
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Lab Request", None))
        self.home_report_icon.setText("")
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Write Report", None))
        self.bill_list_icon.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Bill List", None))
        self.home_schedule_icon.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Check Schedule", None))
        self.logout_button_4.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.Username_7.setText(QCoreApplication.translate("MainWindow", u"Mr.Ms", None))
        self.userprofile_pic_7.setText("")
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Patient Sphere", None))
        self.patient_record_icon.setText("")
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"View Medical Record", None))
        self.patient_appointment_icon.setText("")
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Manage Appointment", None))
        self.patient_payment_icon.setText("")
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"View Payment", None))
        self.logout_button_3.setText(QCoreApplication.translate("MainWindow", u"Log out", None))
        self.menu_icon.setText("")
        self.home_Button.setText("")
        self.patientListButton.setText("")
        self.labButton.setText("")
        self.reportButton.setText("")
        self.billButton.setText("")
        self.scheduleButton.setText("")
        self.logout_button.setText("")
        self.Username.setText(QCoreApplication.translate("MainWindow", u"DR", None))
        self.doctor_setting_button_2.setText("")
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"HN No.", None))
        self.searchButton.setText("")
        self.AddPatientButton.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))
        self.view_patient_info_button.setText(QCoreApplication.translate("MainWindow", u"View Patient Info", None))
        self.edit_patient_info_button.setText(QCoreApplication.translate("MainWindow", u"Edit Patient Info", None))
        ___qtablewidgetitem = self.patient_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"HN No.", None));
        ___qtablewidgetitem1 = self.patient_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Add Patient", None))
        self.upload_photo.setText("")
        self.take_pic_button.setText(QCoreApplication.translate("MainWindow", u"Take Picture", None))
        self.browse_page.setText(QCoreApplication.translate("MainWindow", u"Upload Photo", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"First Name", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Middle Name", None))
        self.middleName_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"optional", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Last Name", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Citizen ID / Passport No.", None))
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Date of Birth", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Weight", None))
        self.weight.setPlaceholderText(QCoreApplication.translate("MainWindow", u"kg", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Sex", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Height", None))
        self.sex.setItemText(0, QCoreApplication.translate("MainWindow", u"Male", None))
        self.sex.setItemText(1, QCoreApplication.translate("MainWindow", u"Female", None))

        self.height.setPlaceholderText(QCoreApplication.translate("MainWindow", u"cm", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Blood Type", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Blodd Pressure", None))
        self.blood_type.setItemText(0, QCoreApplication.translate("MainWindow", u"A+", None))
        self.blood_type.setItemText(1, QCoreApplication.translate("MainWindow", u"A-", None))
        self.blood_type.setItemText(2, QCoreApplication.translate("MainWindow", u"B+", None))
        self.blood_type.setItemText(3, QCoreApplication.translate("MainWindow", u"B-", None))
        self.blood_type.setItemText(4, QCoreApplication.translate("MainWindow", u"O+", None))
        self.blood_type.setItemText(5, QCoreApplication.translate("MainWindow", u"O-", None))
        self.blood_type.setItemText(6, QCoreApplication.translate("MainWindow", u"AB+", None))
        self.blood_type.setItemText(7, QCoreApplication.translate("MainWindow", u"AB-", None))

        self.blood_pressure.setPlaceholderText(QCoreApplication.translate("MainWindow", u"xxx/xx", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"HN No.", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Tel.", None))
        self.tel.setPlaceholderText(QCoreApplication.translate("MainWindow", u"xxx-xxx-xxxx", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Address", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Vaccine History:", None))
        ___qtablewidgetitem2 = self.vaccine_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Vaccine Name", None));
        ___qtablewidgetitem3 = self.vaccine_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date Administered", None));
        self.add_vaccine_button.setText(QCoreApplication.translate("MainWindow", u"Add Vaccine", None))
        self.delete_vaccine_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Medication History:", None))
        ___qtablewidgetitem4 = self.medication_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Medication Name", None));
        ___qtablewidgetitem5 = self.medication_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Amount/container", None));
        ___qtablewidgetitem6 = self.medication_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Dosage", None));
        ___qtablewidgetitem7 = self.medication_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem8 = self.medication_list_table.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Attending Physician", None));
        ___qtablewidgetitem9 = self.medication_list_table.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Administered Date", None));
        ___qtablewidgetitem10 = self.medication_list_table.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Administered TIme", None));
        ___qtablewidgetitem11 = self.medication_list_table.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Side Note", None));
        self.add_medication_button.setText(QCoreApplication.translate("MainWindow", u"Add Medication", None))
        self.delete_medication_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Allergies:", None))
        ___qtablewidgetitem12 = self.allergy_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Allergy Name", None));
        self.add_allergy_button.setText(QCoreApplication.translate("MainWindow", u"Add Allergy", None))
        self.delete_allergy_button.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.confirm_button_2.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.cancel_button_2.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"Lab Requests", None))
        self.view_received_replies.setText(QCoreApplication.translate("MainWindow", u"Lab Results Received", None))
        self.make_lab_request_button.setText(QCoreApplication.translate("MainWindow", u"Make Lab request", None))
        self.make_lab_reply_button.setText(QCoreApplication.translate("MainWindow", u"Reply", None))
        ___qtablewidgetitem13 = self.lab_requests_table.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Urgency", None));
        ___qtablewidgetitem14 = self.lab_requests_table.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Lab Requested", None));
        ___qtablewidgetitem15 = self.lab_requests_table.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Patient HN No", None));
        ___qtablewidgetitem16 = self.lab_requests_table.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None));
        ___qtablewidgetitem17 = self.lab_requests_table.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Attending Physician", None));
        ___qtablewidgetitem18 = self.lab_requests_table.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Date Requested", None));
        ___qtablewidgetitem19 = self.lab_requests_table.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Time Requested", None));
        self.doctor_profile_2.setText("")
        self.fullName_profile.setText(QCoreApplication.translate("MainWindow", u"firstname", None))
        self.speciality_profile.setText(QCoreApplication.translate("MainWindow", u"speciality", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Old Password", None))
        self.show_old_password.setText("")
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"New Password", None))
        self.show_new_password.setText("")
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Confirm New Password", None))
        self.show_confirm_password.setText("")
        self.confirm_button.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"HN No. ", None))
        self.search_button.setText("")
        ___qtablewidgetitem20 = self.doctor_schedule_table.horizontalHeaderItem(0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem21 = self.doctor_schedule_table.horizontalHeaderItem(1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem22 = self.doctor_schedule_table.horizontalHeaderItem(2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"HN No", None));
        ___qtablewidgetitem23 = self.doctor_schedule_table.horizontalHeaderItem(3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.pushButton.setText("")
        self.label_patient_info.setText(QCoreApplication.translate("MainWindow", u"Patient Informations", None))
        self.edit_patient_info.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.back_button_2.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.patient_photo.setText("")
        self.patient_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"HN Number:", None))
        self.patient_hn_no.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.patient_email_display.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth:", None))
        self.patient_dob.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.patient_sex.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.patient_age.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.patient_weight.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.patient_height.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_address.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.patient_address_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_tel_no.setText(QCoreApplication.translate("MainWindow", u"Tel:", None))
        self.patient_tel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_blood_status.setText(QCoreApplication.translate("MainWindow", u"Blood Status", None))
        self.blood_icon.setText("")
        self.patient_blood_type.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.patient_blood_pressure.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.patient_blood_warning.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_medical_history.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.label_past_treatment_3.setText(QCoreApplication.translate("MainWindow", u"Vaccination:", None))
        ___qtablewidgetitem24 = self.vaccine_list_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Vaccine Name", None));
        ___qtablewidgetitem25 = self.vaccine_list_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Date Administrated", None));
        self.label_past_treatment_4.setText(QCoreApplication.translate("MainWindow", u"Medication:", None))
        ___qtablewidgetitem26 = self.medication_list_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem27 = self.medication_list_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem28 = self.medication_list_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Dosage", None));
        ___qtablewidgetitem29 = self.medication_list_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem30 = self.medication_list_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Attending Physician", None));
        ___qtablewidgetitem31 = self.medication_list_table_2.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Date Administrated", None));
        ___qtablewidgetitem32 = self.medication_list_table_2.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Time Administrated", None));
        ___qtablewidgetitem33 = self.medication_list_table_2.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Sidenote", None));
        self.label_allergies.setText(QCoreApplication.translate("MainWindow", u"Allergies:", None))
        ___qtablewidgetitem34 = self.allergy_list_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Allergy Name", None));
        self.label_past_treatment_2.setText(QCoreApplication.translate("MainWindow", u"Lab Test Result:", None))
        ___qtablewidgetitem35 = self.lab_test_list_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem36 = self.lab_test_list_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Doctor", None));
        ___qtablewidgetitem37 = self.lab_test_list_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem38 = self.lab_test_list_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Date Requested", None));
        ___qtablewidgetitem39 = self.lab_test_list_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Time Requested", None));
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Patient Reports", None))
        self.report_edit_button.setText(QCoreApplication.translate("MainWindow", u"EDIT", None))
        ___qtablewidgetitem40 = self.report_patient_table.horizontalHeaderItem(0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"HN NO", None));
        ___qtablewidgetitem41 = self.report_patient_table.horizontalHeaderItem(1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.report_date.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"HN Number :", None))
        self.report_hn_no.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.report_patient_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Summary", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Vaccine", None))
        ___qtablewidgetitem42 = self.report_vaccine_table.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem43 = self.report_vaccine_table.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"Medication", None))
        ___qtablewidgetitem44 = self.report_medication_table.horizontalHeaderItem(0)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem45 = self.report_medication_table.horizontalHeaderItem(1)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem46 = self.report_medication_table.horizontalHeaderItem(2)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Dosage", None));
        ___qtablewidgetitem47 = self.report_medication_table.horizontalHeaderItem(3)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem48 = self.report_medication_table.horizontalHeaderItem(4)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Attending Physician", None));
        ___qtablewidgetitem49 = self.report_medication_table.horizontalHeaderItem(5)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"Lab Test", None))
        ___qtablewidgetitem50 = self.report_lab_test_table.horizontalHeaderItem(0)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem51 = self.report_lab_test_table.horizontalHeaderItem(1)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Other", None))
        ___qtablewidgetitem52 = self.report_other_table.horizontalHeaderItem(0)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem53 = self.report_other_table.horizontalHeaderItem(1)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.report_add_other.setText(QCoreApplication.translate("MainWindow", u"Add", None))
        self.report_delete_other.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.report_confirm_button.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.report_draft_button.setText(QCoreApplication.translate("MainWindow", u"Save as draft", None))
        self.report_cancel_button.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.lab_title.setText(QCoreApplication.translate("MainWindow", u"Lab Request Form", None))
        self.dat_request_2.setText(QCoreApplication.translate("MainWindow", u"Time Requested: xx:xx:xx", None))
        self.date_request.setText(QCoreApplication.translate("MainWindow", u"Date Requested: xx/xx/xxxx", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Requested Tests:", None))
        self.case_type.setItemText(0, QCoreApplication.translate("MainWindow", u"Complete Blood Count (CBC)", None))
        self.case_type.setItemText(1, QCoreApplication.translate("MainWindow", u"Basic Metabolic Panel (BMP)", None))
        self.case_type.setItemText(2, QCoreApplication.translate("MainWindow", u"Liver Function Tests (LFTs)", None))
        self.case_type.setItemText(3, QCoreApplication.translate("MainWindow", u"Lipid Profile", None))
        self.case_type.setItemText(4, QCoreApplication.translate("MainWindow", u"Thyroid Function Tests", None))
        self.case_type.setItemText(5, QCoreApplication.translate("MainWindow", u"Blood Glucose Test", None))
        self.case_type.setItemText(6, QCoreApplication.translate("MainWindow", u"Coagulation Profile", None))
        self.case_type.setItemText(7, QCoreApplication.translate("MainWindow", u"Urinalysis", None))
        self.case_type.setItemText(8, QCoreApplication.translate("MainWindow", u"Cancer Markers", None))
        self.case_type.setItemText(9, QCoreApplication.translate("MainWindow", u"Infectious Disease Tests", None))

        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Urgency:", None))
        self.urgency.setItemText(0, QCoreApplication.translate("MainWindow", u"Routine", None))
        self.urgency.setItemText(1, QCoreApplication.translate("MainWindow", u"Urgent", None))
        self.urgency.setItemText(2, QCoreApplication.translate("MainWindow", u"Immediately Necessary", None))

        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Department:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"HN No:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Patient's Name:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Reason For Request:", None))
        self.submit_button.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Lab Result Submission", None))
        self.dat_request_3.setText(QCoreApplication.translate("MainWindow", u"Time Requested: xx:xx:xx", None))
        self.date_request_2.setText(QCoreApplication.translate("MainWindow", u"Date Requested: xx/xx/xxxx", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Requested Tests:", None))
        self.case_type_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Urgency:", None))
        self.urgency_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Department:", None))
        self.faculty_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"HN No:", None))
        self.lab_request_hn_no_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Patient's Name:", None))
        self.lab_request_patient_name_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Reason For Request:", None))
        self.display_file_name.setText(QCoreApplication.translate("MainWindow", u"No File Selected", None))
        self.upload_file_button.setText(QCoreApplication.translate("MainWindow", u"Upload File", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Note:", None))
        self.confirm_lab_reply.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.cancel_lab_reply.setText(QCoreApplication.translate("MainWindow", u"Cancel", None))
        self.reject_lab_reply.setText(QCoreApplication.translate("MainWindow", u"Reject", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Lab Results Received", None))
        self.viewButton.setText(QCoreApplication.translate("MainWindow", u"View", None))
        self.backBT.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        ___qtablewidgetitem54 = self.lab_requests_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Lab Requested", None));
        ___qtablewidgetitem55 = self.lab_requests_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Patient HN No", None));
        ___qtablewidgetitem56 = self.lab_requests_table_2.horizontalHeaderItem(2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None));
        ___qtablewidgetitem57 = self.lab_requests_table_2.horizontalHeaderItem(3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Date Requested", None));
        ___qtablewidgetitem58 = self.lab_requests_table_2.horizontalHeaderItem(4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Time Requested", None));
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Lab Result", None))
        self.dat_request_4.setText(QCoreApplication.translate("MainWindow", u"Time Requested: xx:xx:xx", None))
        self.date_request_3.setText(QCoreApplication.translate("MainWindow", u"Date Requested: xx/xx/xxxx", None))
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Requested Tests:", None))
        self.case_type_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"HN No:", None))
        self.lab_request_hn_no_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Patient's Name:", None))
        self.lab_request_patient_name_3.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"No file uploaded", None))
        self.download_button.setText(QCoreApplication.translate("MainWindow", u"Download", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Notes:", None))
        self.backBT2.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Lab Result", None))
        self.dat_request_6.setText(QCoreApplication.translate("MainWindow", u"Time Requested: xx:xx:xx", None))
        self.date_request_5.setText(QCoreApplication.translate("MainWindow", u"Date Requested: xx/xx/xxxx", None))
        self.label_98.setText(QCoreApplication.translate("MainWindow", u"Requested Tests:", None))
        self.case_type_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_99.setText(QCoreApplication.translate("MainWindow", u"HN No:", None))
        self.lab_request_hn_no_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"Patient's Name:", None))
        self.lab_request_patient_name_5.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Rejected", None))
        self.backBT3.setText(QCoreApplication.translate("MainWindow", u"Done", None))
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Bill List", None))
        self.doctor_view_bill_button.setText(QCoreApplication.translate("MainWindow", u"VIEW", None))
        ___qtablewidgetitem59 = self.doctor_bill_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Patient Name", None));
        ___qtablewidgetitem60 = self.doctor_bill_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"HN No", None));
        ___qtablewidgetitem61 = self.doctor_bill_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Bill Number", None));
        ___qtablewidgetitem62 = self.doctor_bill_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Bill Date", None));
        ___qtablewidgetitem63 = self.doctor_bill_list_table.horizontalHeaderItem(4)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem64 = self.doctor_bill_list_table.horizontalHeaderItem(5)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Bill Receipt", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Bill Number :", None))
        self.bill_number_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Bill Date :", None))
        self.bill_date_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Patient Information", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.bill_patient_name_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"HN No :", None))
        self.bill_patient_hn_no_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Total Charge :", None))
        self.bill_total_charge_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.bill_status_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.confirm_payment_button.setText(QCoreApplication.translate("MainWindow", u"Payment Confirm ", None))
        ___qtablewidgetitem65 = self.bill_table_2.horizontalHeaderItem(0)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Description of Service", None));
        ___qtablewidgetitem66 = self.bill_table_2.horizontalHeaderItem(1)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.Username_2.setText(QCoreApplication.translate("MainWindow", u"NAME", None))
        self.userprofile_pic_2.setText("")
        self.label_patient_info_2.setText(QCoreApplication.translate("MainWindow", u"Patient Informations", None))
        self.med_record_photo.setText("")
        self.med_record_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"HN Number:", None))
        self.med_record_hn_no.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.patient_email_display_2.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Date Of Birth:", None))
        self.med_record_dob.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"Sex:", None))
        self.med_record_sex.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.med_record_age.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"Weight:", None))
        self.med_record_weight.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Height:", None))
        self.med_record_height.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_address_2.setText(QCoreApplication.translate("MainWindow", u"Address:", None))
        self.med_record_address.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_tel_no_2.setText(QCoreApplication.translate("MainWindow", u"Tel:", None))
        self.med_record_tel.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_blood_status_2.setText(QCoreApplication.translate("MainWindow", u"Blood Status", None))
        self.blood_icon_2.setText("")
        self.med_record_blood_type.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.med_record_blood_pressure.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.med_record_blood_warning.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_medical_history_2.setText(QCoreApplication.translate("MainWindow", u"Medical History", None))
        self.label_past_treatment_7.setText(QCoreApplication.translate("MainWindow", u"Vaccination:", None))
        ___qtablewidgetitem67 = self.vaccine_list_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Vaccine Name", None));
        ___qtablewidgetitem68 = self.vaccine_list_table_3.horizontalHeaderItem(1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"Date Administrated", None));
        self.label_past_treatment_8.setText(QCoreApplication.translate("MainWindow", u"Medication:", None))
        ___qtablewidgetitem69 = self.medication_list_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem70 = self.medication_list_table_3.horizontalHeaderItem(1)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem71 = self.medication_list_table_3.horizontalHeaderItem(2)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"Dosage", None));
        ___qtablewidgetitem72 = self.medication_list_table_3.horizontalHeaderItem(3)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"Duration", None));
        ___qtablewidgetitem73 = self.medication_list_table_3.horizontalHeaderItem(4)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Attending Physician", None));
        ___qtablewidgetitem74 = self.medication_list_table_3.horizontalHeaderItem(5)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Date Administrated", None));
        ___qtablewidgetitem75 = self.medication_list_table_3.horizontalHeaderItem(6)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"Time Administrated", None));
        ___qtablewidgetitem76 = self.medication_list_table_3.horizontalHeaderItem(7)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Sidenote", None));
        self.label_allergies_2.setText(QCoreApplication.translate("MainWindow", u"Allergies:", None))
        ___qtablewidgetitem77 = self.allergy_list_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"Allergy Name", None));
        self.label_past_treatment_6.setText(QCoreApplication.translate("MainWindow", u"Lab Test Result:", None))
        ___qtablewidgetitem78 = self.lab_test_list_table_3.horizontalHeaderItem(0)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem79 = self.lab_test_list_table_3.horizontalHeaderItem(1)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"Doctor", None));
        ___qtablewidgetitem80 = self.lab_test_list_table_3.horizontalHeaderItem(2)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        ___qtablewidgetitem81 = self.lab_test_list_table_3.horizontalHeaderItem(3)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Date Requested", None));
        ___qtablewidgetitem82 = self.lab_test_list_table_3.horizontalHeaderItem(4)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Time Requested", None));
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Schedule", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.search_date_button.setText("")
        self.cancel_appointment.setText(QCoreApplication.translate("MainWindow", u"Cancel Appointment", None))
        self.new_appointment_button.setText(QCoreApplication.translate("MainWindow", u"Make New Appointment", None))
        ___qtablewidgetitem83 = self.patient_schedule_table.horizontalHeaderItem(0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem84 = self.patient_schedule_table.horizontalHeaderItem(1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"Time", None));
        ___qtablewidgetitem85 = self.patient_schedule_table.horizontalHeaderItem(2)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"Doctor", None));
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Bill Receipt", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Bill Number :", None))
        self.bill_number.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Bill Date :", None))
        self.bill_date.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Patient Information", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Name :", None))
        self.bill_patient_name.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"HN No :", None))
        self.bill_patient_hn_no.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_97.setText(QCoreApplication.translate("MainWindow", u"Total Charge :", None))
        self.bill_total_charge.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Status :", None))
        self.bill_status.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Apply Discount :", None))
        self.select_discount.setItemText(0, QCoreApplication.translate("MainWindow", u"Medical Golden Card", None))
        self.select_discount.setItemText(1, QCoreApplication.translate("MainWindow", u"Health Insurance Card", None))
        self.select_discount.setItemText(2, QCoreApplication.translate("MainWindow", u"Clinic Member Card", None))

        self.label_36.setText(QCoreApplication.translate("MainWindow", u"Enter Insurance Value :", None))
        self.apply_discount_button.setText(QCoreApplication.translate("MainWindow", u"Apply DIscount", None))
        ___qtablewidgetitem86 = self.bill_table.horizontalHeaderItem(0)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Description of Service", None));
        ___qtablewidgetitem87 = self.bill_table.horizontalHeaderItem(1)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Bill List", None))
        self.view_bill_button.setText(QCoreApplication.translate("MainWindow", u"VIEW", None))
        ___qtablewidgetitem88 = self.bill_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u" Number", None));
        ___qtablewidgetitem89 = self.bill_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem90 = self.bill_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem91 = self.bill_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"Status", None));
        self.menu_icon_2.setText("")
        self.home_Button_2.setText("")
        self.viewMedRecord_button.setText("")
        self.manageAppointmentButton.setText("")
        self.billPaymentButton.setText("")
        self.logout_button_2.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"ADMIN: Add Doctor", None))
        self.directory.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.doctor_profile.setText("")
        self.take_pic_button_2.setText(QCoreApplication.translate("MainWindow", u"Take Picture", None))
        self.browse_page_2.setText(QCoreApplication.translate("MainWindow", u"Upload Photo", None))
        self.userName.setText(QCoreApplication.translate("MainWindow", u"USERNAME", None))
        self.password_2.setText(QCoreApplication.translate("MainWindow", u"PASSWORD", None))
        self.doctor_email.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"First name", None))
        self.middleName2.setText(QCoreApplication.translate("MainWindow", u"Middle name", None))
        self.middleName.setPlaceholderText(QCoreApplication.translate("MainWindow", u"optional", None))
        self.lastName2.setText(QCoreApplication.translate("MainWindow", u"Last name", None))
        self.speciality2.setText(QCoreApplication.translate("MainWindow", u"Department", None))
        self.addDoctorButton.setText(QCoreApplication.translate("MainWindow", u"Add Doctor", None))
        self.see_doctor_list_button.setText(QCoreApplication.translate("MainWindow", u"See Doctor List", None))
        self.logout_button_5.setText(QCoreApplication.translate("MainWindow", u"LOG OUT", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Doctor List", None))
        self.back_button.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Username :", None))
        self.search_username_button.setText("")
        ___qtablewidgetitem92 = self.doctor_list_table.horizontalHeaderItem(0)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"Username", None));
        ___qtablewidgetitem93 = self.doctor_list_table.horizontalHeaderItem(1)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Password", None));
        ___qtablewidgetitem94 = self.doctor_list_table.horizontalHeaderItem(2)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem95 = self.doctor_list_table.horizontalHeaderItem(3)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Speciality", None));
    # retranslateUi

