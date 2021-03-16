from PyQt5 import QtCore, QtGui, QtWidgets

class Dia_Form:
    def Dialoguewindow(self, Form1):
        Form1.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form1.setObjectName("Form1")
        Form1.resize(505, 407)
        self.dialog = QtWidgets.QTextBrowser(Form1)
        self.dialog.setGeometry(QtCore.QRect(70, 20, 381, 311))
        self.dialog.setObjectName("dialog")
        pixmicro = QtGui.QPixmap(r'micro.jpg')
        pixmicro = pixmicro.scaled(41, 41)
        iconmicro = QtGui.QIcon(pixmicro)
        self.micro = QtWidgets.QPushButton(Form1)
        self.micro.setGeometry(QtCore.QRect(10, 340, 41, 41))
        self.micro.setText("")
        self.micro.setObjectName("micro")
        self.micro.setIcon(iconmicro)
        self.micro.setIconSize(pixmicro.rect().size())
        self.micro.setFixedSize(pixmicro.rect().size())
        pixset = QtGui.QPixmap(r'settings.png')
        pixset = pixset.scaled(41, 31)
        iconset = QtGui.QIcon(pixset)
        self.settings = QtWidgets.QPushButton(Form1)
        self.settings.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.settings.setIcon(iconset)
        self.settings.setIconSize(pixset.rect().size())
        self.settings.setFixedSize(pixset.rect().size())
        self.lineEdit = QtWidgets.QLineEdit(Form1)
        self.lineEdit.setGeometry(QtCore.QRect(100, 350, 301, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                    "border: 1px solid black;\n"
                                    "border-radius: 10px;\n"
                                    "\n""")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите текст")
        pixsend = QtGui.QPixmap(r'send.jpg')
        pixsend = pixsend.scaled(51, 41)
        iconsend = QtGui.QIcon(pixsend)
        self.send = QtWidgets.QPushButton(Form1)
        self.send.setGeometry(QtCore.QRect(430, 340, 51, 41))
        self.send.setText("")
        self.send.setObjectName("send")
        self.send.setIcon(iconsend)
        self.send.setIconSize(pixsend.rect().size())
        self.send.setFixedSize(pixsend.rect().size())
        self.send.clicked.connect(self.output)
        self.retranslateUi(Form1)
        QtCore.QMetaObject.connectSlotsByName(Form1)
    def output(self): # получение текста из поля и вывод его на экран
        input_text = self.lineEdit.text()
        if input_text != "":
            self.lineEdit.clear()
            self.dialog.append(input_text)

    def retranslateUi(self, Form1):
        _translate = QtCore.QCoreApplication.translate
        Form1.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Dia_Form()
    ui.Dialoguewindow(Form)
    Form.show()
    Form.setVisible(False)
    sys.exit(app.exec_())
