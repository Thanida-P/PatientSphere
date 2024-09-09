from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton

class Sidebar(QMainWindow):
    def __init__(self):
        super(Sidebar, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("PatientSphere")
        self.ui.home_Button.clicked.connect(self.switch_to_home)
        self.ui.patientListButton.clicked.connect(self.switch_to_patients)
        self.ui.scheduleButton.clicked.connect(self.switch_to_appointments)

    def switch_to_home(self):
        self.ui.stackedWidget.setCurrentIndex(0)

    def switch_to_patients(self):
        self.ui.stackedWidget.setCurrentIndex(2)

    def switch_to_appointments(self):
        self.ui.stackedWidget.setCurrentIndex(1)