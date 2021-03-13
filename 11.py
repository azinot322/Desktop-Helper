from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap, QIcon
import sys
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(400, 400)
        screen_geometry = QApplication.desktop().availableGeometry()
        screen_size = (screen_geometry.width(), screen_geometry.height())
        win_size = (Form.frameSize().width(), Form.frameSize().height())
        x = screen_size[0] - win_size[0]
        y = screen_size[1] - win_size[1]
        Form.move(x, y)
        pixmap = QPixmap(r"22.jpg")
        pixmap = pixmap.scaled(400, 400)
        icon = QIcon(pixmap)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(-10, 0, 400, 400))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(pixmap.rect().size())
        self.pushButton.setFixedSize(pixmap.rect().size())
        self.pushButton.setFlat(True)
        self.pushButton.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.pushButton.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.pushButton.clicked.connect(self.click_on_character)
        self.pushButton.raise_()
        """self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 0, 611, 541))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(r"22.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()"""
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


    def click_on_character(self):
        print("123")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
