from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys


class Main_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("DesktopHelper")
        Form.resize(400, 630)
        pixmap = QPixmap(r"geralt.png")
        pixmap = pixmap.scaled(400, 630)
        icon = QIcon(pixmap)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(pixmap.rect().size())
        self.pushButton.setFixedSize(pixmap.rect().size())
        self.pushButton.setFlat(True)
        self.pushButton.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))