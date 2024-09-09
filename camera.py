import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog, QLabel, QPushButton, QVBoxLayout, QGridLayout, QComboBox, QWidget
from PySide6.QtCore import Qt, QThread, Signal, Slot
from PySide6.QtGui import QImage
from PySide6.QtGui import QPixmap, QImage
from PySide6.QtMultimedia import QMediaDevices
from PySide6.QtNetwork import QNetworkAccessManager
import cv2
import datetime
import os

class Camera(QWidget):
    def __init__(self, ui, user_type):
        super().__init__()
        self.directory = ""
        self.ui = ui
        self.user_type = user_type
        self.profile = ""
        self.network_manager = QNetworkAccessManager()
        
        self.layout = QGridLayout(self)
        self.availableCameras = []
        self.th = Thread(self)
        self.th.finished.connect(self.close)
        self.th.updateFrame.connect(self.setImage)

        self.label = QLabel(self)
        self.label.setStyleSheet(u"background-color: black;")
        self.layout.addWidget(self.label)
        
        self.combobox = QComboBox(self)
        self.getAvailableCameras()
        self.current = "Select Camera"
        self.combobox.addItem(self.current)
        self.combobox.addItems(self.availableCameras)
        self.layout.addWidget(self.combobox)
        self.combobox.currentIndexChanged.connect(self.runWebCam)
        
        captureBT = QtWidgets.QPushButton("Capture", self)
        captureBT.setObjectName(u"captureBT")
        captureBT.setStyleSheet(u"QPushButton#captureBT {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#captureBT:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        self.layout.addWidget(captureBT)
        captureBT.clicked.connect(self.captureImage)


    @Slot(QImage)
    def runWebCam(self):
        if self.current == "Select Camera":
            self.current = "Selected"
            self.combobox.removeItem(0)
        self.th.start()
        
    @Slot(QImage)
    def setImage(self, image):
        self.label.setPixmap(QPixmap.fromImage(image))
    
    def getAvailableCameras(self):
        cameras = QMediaDevices.videoInputs()
        for cameraDevice in cameras:
            self.availableCameras.append(cameraDevice.description())
    
    def captureImage(self):
        img = self.th.capturePicture()
        self.directory = f"upload/capture_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        img.save(self.directory)
        self.image_dialog = QDialog()
        self.image_dialog.setWindowTitle("Captured Image")
        self.image_dialog.resize(800, 600)
        image_layout = QVBoxLayout()
        self.image_dialog.setLayout(image_layout)
        image = open(self.directory, "rb").read()
        image_label = QLabel()
        image_layout.addWidget(image_label, alignment=Qt.AlignHCenter)
        image_label.setPixmap(QPixmap.fromImage(QImage.fromData(image)))
        saveBT = QPushButton("Save")
        saveBT.setObjectName(u"saveBT")
        saveBT.setStyleSheet(u"QPushButton#saveBT {\n"
"	background-color: rgb(39, 86, 193);\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#saveBT:hover {\n"
"    background-color: black;\n"
"	color: white;\n"
"    border-style: inset;\n"
"}")
        saveBT.clicked.connect(self.saveImage)
        image_layout.addWidget(saveBT)
        
        cancelBT = QPushButton("Cancel")
        cancelBT.setObjectName(u"cancelBT")
        cancelBT.setStyleSheet(u"QPushButton#cancelBT {\n"
"	background-color: black;\n"
"	color: white;\n"
"	border-radius: 10px;\n"
"	padding: 10px;\n"
"    font: bold 14px;\n"
"}\n"
"QPushButton#cancelBT:hover {\n"
"    background-color: white;\n"
"	color: black;\n"
"    border-style: inset;\n"
"}")
        image_layout.addWidget(cancelBT)
        cancelBT.clicked.connect(self.deleteImage)
        
        self.image_dialog.exec()
        
    def saveImage(self):
        self.image_dialog.close()
        file = open(self.directory, "rb").read()
        image = QPixmap.fromImage(QImage.fromData(file))
        if self.user_type == "patient":
            self.ui.upload_photo.setPixmap(image)
            self.ui.upload_photo.setScaledContents(True)
            self.ui.upload_photo.setFixedSize(100, 100)
        else:
            self.ui.doctor_profile.setPixmap(image)
            self.ui.doctor_profile.setScaledContents(True)
            self.ui.doctor_profile.setFixedSize(100, 100)
        self.ui.directory.setText(self.directory)  
        self.close()
        self.th.cap.release()
        self.th.status = False
        self.th.terminate()

    def getFilename(self):
        return self.directory
    
    def deleteImage(self):
        directory = self.directory
        os.remove(directory)
        self.image_dialog.close()
        
class Thread(QThread):
    updateFrame = Signal(QImage)
    def __init__(self, parent=None):
        QThread.__init__(self, parent)
        self.status = True
        self.cap = True

    def run(self):
        self.cap = cv2.VideoCapture(0)
        while self.status:
            ret, frame = self.cap.read()
            if not ret:
                continue
            h, w, ch = frame.shape
            img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = QImage(img.data, w, h, ch*w, QImage.Format.Format_RGB888)
            scaled_img = img.scaled(800, 600, Qt.AspectRatioMode.KeepAspectRatio)
            self.updateFrame.emit(scaled_img)
        sys.exit(-1)
    
    def capturePicture(self):
        ret, frame = self.cap.read()
        if not ret:
            return
        h, w, ch = frame.shape
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        img = QImage(img.data, w, h, ch*w, QImage.Format.Format_RGB888)
        return img
