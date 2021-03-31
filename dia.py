from PyQt5 import QtCore, QtGui, QtWidgets


class Dia_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(600, 420)
        Form.setMinimumSize(QtCore.QSize(600, 420))
        Form.setMaximumSize(QtCore.QSize(600, 420))
        Form.setStyleSheet('background-color: rgb(255, 254, 228);')
        pixset = QtGui.QPixmap(r'settings.png')
        pixset = pixset.scaled(41, 31)
        iconset = QtGui.QIcon(pixset)
        self.settings_button = QtWidgets.QPushButton(Form)
        self.settings_button.setGeometry(QtCore.QRect(10, 20, 51, 51))
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.settings_button.setCheckable(True)
        self.settings_button.setIcon(iconset)
        self.settings_button.setIconSize(pixset.rect().size())
        self.settings_button.setFixedSize(pixset.rect().size())
        self.settings_button.setFlat(True)
        self.settings_button.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.settings_button.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(70, 10, 600, 600))
        self.stackedWidget.setObjectName("stackedWidget")
        self.dialog_window = QtWidgets.QWidget()
        self.dialog_window.setObjectName("dialog_window")
        pixsend = QtGui.QPixmap(r'send.png')
        pixsend = pixsend.scaled(51, 41)
        iconsend = QtGui.QIcon(pixsend)
        self.send = QtWidgets.QPushButton(self.dialog_window)
        self.send.setGeometry(QtCore.QRect(430, 340, 51, 41))
        self.send.setText("")
        self.send.setObjectName("send")
        self.send.setIcon(iconsend)
        self.send.setIconSize(pixsend.rect().size())
        self.send.setFixedSize(pixsend.rect().size())
        self.send.setFlat(True)
        self.send.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.send.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        pixmicro = QtGui.QPixmap(r'micro.png')
        pixmicro = pixmicro.scaled(41, 51)
        iconmicro = QtGui.QIcon(pixmicro)
        self.micro = QtWidgets.QPushButton(self.dialog_window)
        self.micro.setGeometry(QtCore.QRect(10, 340, 41, 51))
        self.micro.setText("")
        self.micro.setObjectName("micro")
        self.micro.setIcon(iconmicro)
        self.micro.setIconSize(pixmicro.rect().size())
        self.micro.setFixedSize(pixmicro.rect().size())
        self.micro.setFlat(True)
        self.micro.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.micro.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.lineEdit = QtWidgets.QLineEdit(self.dialog_window)
        self.lineEdit.setGeometry(QtCore.QRect(100, 350, 301, 31))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                    "border: 1px solid black;\n"
                                    "border-radius: 10px;\n"
                                    "\n""")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите текст")
        self.dialog = QtWidgets.QTextBrowser(self.dialog_window)
        self.dialog.setGeometry(QtCore.QRect(70, 20, 381, 311))
        self.dialog.setObjectName("dialog")
        self.stackedWidget.addWidget(self.dialog_window)
        self.dialog.setStyleSheet('background-color: rgb(172, 200, 242);')
        self.settings_window = QtWidgets.QWidget()
        self.auto_1 = QtWidgets.QCheckBox(self.settings_window)
        self.auto_1.setGeometry(QtCore.QRect(10, 10, 261, 31))
        self.auto_1.setObjectName("auto_1")
        self.checkBox_2 = QtWidgets.QCheckBox(self.settings_window)
        self.checkBox_2.setGeometry(QtCore.QRect(10, 40, 261, 21))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.settings_window)
        self.checkBox_3.setGeometry(QtCore.QRect(10, 70, 261, 21))
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.settings_window)
        self.checkBox_4.setGeometry(QtCore.QRect(10, 100, 261, 21))
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.settings_window)
        self.checkBox_5.setGeometry(QtCore.QRect(10, 130, 281, 21))
        self.checkBox_5.setObjectName("checkBox_5")
        self.checkBox_6 = QtWidgets.QCheckBox(self.settings_window)
        self.checkBox_6.setGeometry(QtCore.QRect(10, 160, 271, 21))
        self.checkBox_6.setObjectName("checkBox_6")
        self.pushButton = QtWidgets.QPushButton(self.settings_window)
        self.pushButton.setGeometry(QtCore.QRect(340, 320, 141, 51))
        self.pushButton.setObjectName("pushButton")
        self.Accept = QtWidgets.QPushButton(self.settings_window)
        self.Accept.setGeometry(QtCore.QRect(30, 320, 111, 51))
        self.Accept.setObjectName("Accept")
        self.textBrowser = QtWidgets.QTextBrowser(self.settings_window)
        self.textBrowser.setGeometry(QtCore.QRect(230, 61, 256, 191))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet('background-color: rgb(172, 200, 242);')
        self.lineEdit1 = QtWidgets.QLineEdit(self.settings_window)
        self.lineEdit1.setGeometry(QtCore.QRect(230, 250, 256, 25))
        self.lineEdit1.setObjectName("lineEdit1")
        self.settings_window.setObjectName("settings_window")
        self.stackedWidget.addWidget(self.settings_window)
        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Ведьмачел")
        Form.setWindowIcon(QtGui.QIcon('ved.jpg'))
        self.auto_1.setText(_translate("Form", "запускать автоматически при запуске windows"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.checkBox_3.setText(_translate("Form", "CheckBox"))
        self.checkBox_4.setText(_translate("Form", "CheckBox"))
        self.checkBox_5.setText(_translate("Form", "CheckBox"))
        self.checkBox_6.setText(_translate("Form", "CheckBox"))
        self.pushButton.setText(_translate("Form", "Добавить команду"))
        self.Accept.setText(_translate("Form", "Подтвердить"))


