# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'controlpanel.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtGui import QImage, QPixmap
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

from PyQt5 import QtCore, QtGui, QtWidgets

class ControlPanel(QMainWindow):
    def __init__(self):
        super(ControlPanel, self).__init__()
        self.setupUi()

    def setupUi(self):
        self.setObjectName("ControlPanel")
        self.resize(800, 600)
        self.setStyleSheet("background-color: rgb(118, 118, 118);")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Impact Label")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setAlignment(QtCore.Qt.AlignCenter)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.red = QtWidgets.QFrame(self.groupBox)
        self.red.setStyleSheet("background-color: rgb(255, 0, 0);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 10px;")
        self.red.setFrameShape(QtWidgets.QFrame.Box)
        self.red.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.red.setLineWidth(2)
        self.red.setObjectName("red")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.red)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.mag = QtWidgets.QDial(self.red)
        self.mag.setContextMenuPolicy(QtCore.Qt.ActionsContextMenu)
        self.mag.setStyleSheet("image: url(:/forground.png);")
        self.mag.setWrapping(True)
        self.mag.setNotchesVisible(True)
        self.mag.setObjectName("mag")
        self.gridLayout_5.addWidget(self.mag, 0, 0, 1, 1)
        self.upper = QtWidgets.QDial(self.red)
        self.upper.setStyleSheet("")
        self.upper.setWrapping(True)
        self.upper.setNotchesVisible(True)
        self.upper.setObjectName("upper")
        self.gridLayout_5.addWidget(self.upper, 1, 0, 1, 1)
        self.lower = QtWidgets.QDial(self.red)
        self.lower.setStyleSheet("")
        self.lower.setWrapping(True)
        self.lower.setNotchesVisible(True)
        self.lower.setObjectName("lower")
        self.gridLayout_5.addWidget(self.lower, 2, 0, 1, 1)
        self.binary = QtWidgets.QCheckBox(self.red)
        self.binary.setText("")
        self.binary.setObjectName("binary")
        self.gridLayout_5.addWidget(self.binary, 3, 0, 1, 1)
        self.binary.raise_()
        self.lower.raise_()
        self.upper.raise_()
        self.mag.raise_()
        self.gridLayout.addWidget(self.red, 0, 0, 1, 1)
        self.blue = QtWidgets.QFrame(self.groupBox)
        self.blue.setStyleSheet("background-color: rgb(0, 0, 255);")
        self.blue.setFrameShape(QtWidgets.QFrame.Box)
        self.blue.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.blue.setLineWidth(2)
        self.blue.setObjectName("blue")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.blue)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.mag_3 = QtWidgets.QDial(self.blue)
        self.mag_3.setStyleSheet("")
        self.mag_3.setWrapping(True)
        self.mag_3.setNotchesVisible(True)
        self.mag_3.setObjectName("mag_3")
        self.gridLayout_3.addWidget(self.mag_3, 0, 0, 1, 1)
        self.upper_3 = QtWidgets.QDial(self.blue)
        self.upper_3.setStyleSheet("")
        self.upper_3.setWrapping(True)
        self.upper_3.setNotchesVisible(True)
        self.upper_3.setObjectName("upper_3")
        self.gridLayout_3.addWidget(self.upper_3, 1, 0, 1, 1)
        self.lower_3 = QtWidgets.QDial(self.blue)
        self.lower_3.setStyleSheet("")
        self.lower_3.setWrapping(True)
        self.lower_3.setNotchesVisible(True)
        self.lower_3.setObjectName("lower_3")
        self.gridLayout_3.addWidget(self.lower_3, 2, 0, 1, 1)
        self.binary_3 = QtWidgets.QCheckBox(self.blue)
        self.binary_3.setText("")
        self.binary_3.setObjectName("binary_3")
        self.gridLayout_3.addWidget(self.binary_3, 3, 0, 1, 1)
        self.binary_3.raise_()
        self.lower_3.raise_()
        self.mag_3.raise_()
        self.upper_3.raise_()
        self.gridLayout.addWidget(self.blue, 0, 1, 1, 1)
        self.green = QtWidgets.QFrame(self.groupBox)
        self.green.setStyleSheet("background-color: rgb(0, 255, 0);\n"
"border-color: rgb(0, 0, 0);")
        self.green.setFrameShape(QtWidgets.QFrame.Box)
        self.green.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.green.setLineWidth(2)
        self.green.setObjectName("green")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.green)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.mag_5 = QtWidgets.QDial(self.green)
        self.mag_5.setStyleSheet("")
        self.mag_5.setWrapping(True)
        self.mag_5.setNotchesVisible(True)
        self.mag_5.setObjectName("mag_5")
        self.gridLayout_4.addWidget(self.mag_5, 0, 0, 1, 1)
        self.upper_5 = QtWidgets.QDial(self.green)
        self.upper_5.setStyleSheet("")
        self.upper_5.setWrapping(True)
        self.upper_5.setNotchesVisible(True)
        self.upper_5.setObjectName("upper_5")
        self.gridLayout_4.addWidget(self.upper_5, 1, 0, 1, 1)
        self.lower_5 = QtWidgets.QDial(self.green)
        self.lower_5.setStyleSheet("")
        self.lower_5.setWrapping(True)
        self.lower_5.setNotchesVisible(True)
        self.lower_5.setObjectName("lower_5")
        self.gridLayout_4.addWidget(self.lower_5, 2, 0, 1, 1)
        self.binary_5 = QtWidgets.QCheckBox(self.green)
        self.binary_5.setText("")
        self.binary_5.setObjectName("binary_5")
        self.gridLayout_4.addWidget(self.binary_5, 3, 0, 1, 1)
        self.binary_5.raise_()
        self.lower_5.raise_()
        self.upper_5.raise_()
        self.mag_5.raise_()
        self.gridLayout.addWidget(self.green, 0, 2, 1, 1)
        self.black = QtWidgets.QFrame(self.groupBox)
        self.black.setStyleSheet("background-color: rgb(10,10,10);")
        self.black.setFrameShape(QtWidgets.QFrame.Box)
        self.black.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.black.setLineWidth(2)
        self.black.setObjectName("black")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.black)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.mag_6 = QtWidgets.QDial(self.black)
        self.mag_6.setStyleSheet("")
        self.mag_6.setWrapping(True)
        self.mag_6.setNotchesVisible(True)
        self.mag_6.setObjectName("mag_6")
        self.gridLayout_2.addWidget(self.mag_6, 0, 0, 1, 1)
        self.upper_6 = QtWidgets.QDial(self.black)
        self.upper_6.setStyleSheet("")
        self.upper_6.setWrapping(True)
        self.upper_6.setNotchesVisible(True)
        self.upper_6.setObjectName("upper_6")
        self.gridLayout_2.addWidget(self.upper_6, 1, 0, 1, 1)
        self.lower_6 = QtWidgets.QDial(self.black)
        self.lower_6.setStyleSheet("")
        self.lower_6.setWrapping(True)
        self.lower_6.setNotchesVisible(True)
        self.lower_6.setObjectName("lower_6")
        self.gridLayout_2.addWidget(self.lower_6, 2, 0, 1, 1)
        self.binary_6 = QtWidgets.QCheckBox(self.black)
        self.binary_6.setText("")
        self.binary_6.setObjectName("binary_6")
        self.gridLayout_2.addWidget(self.binary_6, 3, 0, 1, 1)
        self.upper_6.raise_()
        self.mag_6.raise_()
        self.binary_6.raise_()
        self.lower_6.raise_()
        self.gridLayout.addWidget(self.black, 0, 3, 1, 1)
        self.gridLayout_6.addWidget(self.groupBox, 0, 0, 1, 1)
        self.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(self)
        self.statusbar.setObjectName("statusbar")
        self.setStatusBar(self.statusbar)

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("ControlPanel", "MainWindow"))
        self.groupBox.setTitle(_translate("ControlPanel", "COLORS"))


