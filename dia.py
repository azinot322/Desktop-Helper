from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(505, 407)
        Form.setStyleSheet("background-color:#FFCCCCC\n"
                           "")
        self.dialog = QtWidgets.QTextBrowser(Form)
        self.dialog.setGeometry(QtCore.QRect(70, 20, 381, 311))
        self.dialog.setObjectName("dialog")
        self.micro = QtWidgets.QPushButton(Form)
        self.micro.setGeometry(QtCore.QRect(10, 340, 41, 41))
        self.micro.setText("")
        self.micro.setObjectName("micro")
        self.settings = QtWidgets.QPushButton(Form)
        self.settings.setGeometry(QtCore.QRect(10, 10, 41, 31))
        self.settings.setText("")
        self.settings.setObjectName("settings")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(100, 350, 301, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                    "border: 1px solid black;\n"
                                    "border-radius: 10px;\n"
                                    "\n""")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите текст")
        self.send = QtWidgets.QPushButton(Form)
        self.send.setGeometry(QtCore.QRect(430, 340, 51, 41))
        self.send.setText("")
        self.send.setObjectName("send")
        self.send.clicked.connect(self.output)


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def output(self): # получение текста из поля и вывод его на экран
        input_text = self.lineEdit.text()
        if input_text != "":
            self.lineEdit.clear()
            self.dialog.append(input_text)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
