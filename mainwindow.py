from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys


class Main_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("DesktopHelper")
        Form.resize(400, 630)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (Form.frameSize().width(), Form.frameSize().height())
        x = screen_size[0] - win_size[0]
        y = screen_size[1] - win_size[1]
        Form.move(x, y)
        pixmap = QPixmap(r"geralt.png")
        pixmap = pixmap.scaled(400, 630)
        icon = QIcon(pixmap)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(-10, 0, 400, 630))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(pixmap.rect().size())
        self.pushButton.setFixedSize(pixmap.rect().size())
        self.pushButton.setFlat(True)
        self.pushButton.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
