from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

#from PyQt5 import QtCore
#import PyQt5.QtCore
#FramelessWindowHint = PyQt5.QtCore.Qt.FramelessWindowHint

from qt_CameraWidget import ImageRIT_PyQt


class DisplayWindow(QMainWindow):
    def __init__(self, cameraId, config_file):
        QMainWindow.__init__(self)
        self.setupUi()

        self.cam = ImageRIT_PyQt(cameraId, config_file)
        self.cam.newFrame.connect(self.display)
        #self.cam.start()


    @QtCore.pyqtSlot(QImage)
    def display(self, frame):
        self.ImageLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.ImageLabel.setPixmap(QPixmap.fromImage(frame).scaled(self.ImageLabel.size(), \
            QtCore.Qt.KeepAspectRatio, QtCore.Qt.FastTransformation))
        self.ImageLabel.update()


    # auto generated past this point
    def setupUi(self):
        self.setObjectName("MainWindow")
        self.resize(800, 601)
        self.setAutoFillBackground(False)
        self.setStyleSheet("background-color: rgb(243, 110, 33);")
        self.VideoStream = QtWidgets.QWidget(self)
        self.VideoStream.setObjectName("VideoStream")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.VideoStream)
        self.verticalLayout.setObjectName("verticalLayout")
        self.ImageLabel = QtWidgets.QLabel(self.VideoStream)
        self.ImageLabel.setText("")
        self.ImageLabel.setObjectName("ImageLabel")
        self.verticalLayout.addWidget(self.ImageLabel)
        self.setCentralWidget(self.VideoStream)
        self.statusBar = QtWidgets.QStatusBar(self)
        self.statusBar.setStyleSheet("border-top-color: rgb(0, 0, 0);\n"
"background-color: rgb(0, 0, 0);")
        self.statusBar.setObjectName("statusBar")
        self.setStatusBar(self.statusBar)
        #self.setWindowFlags(FramelessWindowHint) 

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MainWindow", "MainWindow"))