from PyQt5 import QtCore, QtGui, QtWidgets


class Dia_Form:
    def Dialoguewindow(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(505, 407)
        self.dialog = QtWidgets.QTextBrowser(Form)
        self.dialog.setGeometry(QtCore.QRect(70, 20, 381, 311))
        self.dialog.setObjectName("dialog")
        pixmicro = QtGui.QPixmap(r'micro.jpg')
        pixmicro = pixmicro.scaled(41, 41)
        iconmicro = QtGui.QIcon(pixmicro)
        self.micro = QtWidgets.QPushButton(Form)
        self.micro.setGeometry(QtCore.QRect(10, 340, 41, 41))
        self.micro.setText("")
        self.micro.setObjectName("micro")
        self.micro.setIcon(iconmicro)
        self.micro.setIconSize(pixmicro.rect().size())
        self.micro.setFixedSize(pixmicro.rect().size())
        pixset = QtGui.QPixmap(r'settings.png')
        pixset = pixset.scaled(41, 31)
        iconset = QtGui.QIcon(pixset)
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings")
        self.settings_button.setIcon(iconset)
        self.settings_button.setIconSize(pixset.rect().size())
        self.settings_button.setFixedSize(pixset.rect().size())
        self.lineEdit = QtWidgets.QLineEdit(Form)
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
        self.send = QtWidgets.QPushButton(Form)
        self.send.setGeometry(QtCore.QRect(430, 340, 51, 41))
        self.send.setText("")
        self.send.setObjectName("send")
        self.send.setIcon(iconsend)
        self.send.setIconSize(pixsend.rect().size())
        self.send.setFixedSize(pixsend.rect().size())
        self.send.clicked.connect(self.output)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def output(self):  # получение текста из поля и вывод его на экран
        input_text = self.lineEdit.text()

        if input_text != "":
            self.lineEdit.clear()
            self.dialog.append(input_text)
        if input_text == "Привет".lower():
            self.dialog.append("Привет, путник!")

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Dia_Form()
    ui.Dialoguewindow(Form)
    Form.show()
    sys.exit(app.exec_())
