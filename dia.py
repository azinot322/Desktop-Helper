import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QComboBox, QLabel
import keyboard


class Dia_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("Form")
        Form.resize(500, 440)
        Form.setMinimumSize(QtCore.QSize(500, 440))
        Form.setMaximumSize(QtCore.QSize(500, 440))

        pixset = QtGui.QPixmap(r'resources\exit.png')
        pixset = pixset.scaled(40, 30)
        iconset = QtGui.QIcon(pixset)
        self.exit_button = QtWidgets.QPushButton(Form)
        self.exit_button.setGeometry(QtCore.QRect(460, 0, 40, 30))
        self.exit_button.setText("")
        self.exit_button.setObjectName("exit_button")
        self.exit_button.setCheckable(True)
        self.exit_button.setIcon(iconset)
        self.exit_button.setIconSize(pixset.rect().size())
        self.exit_button.setFixedSize(pixset.rect().size())
        self.exit_button.setFlat(True)
        self.exit_button.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.exit_button.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.stackedWidget = QtWidgets.QStackedWidget(Form)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 30, 570, 410))
        self.stackedWidget.setObjectName("stackedWidget")
        self.dialog_window = QtWidgets.QWidget()  # диалоговое окно
        self.dialog_window.setObjectName("dialog_window")
        self.label = QtWidgets.QLabel(self.dialog_window)
        self.label.setGeometry(QtCore.QRect(-10, -10, 550, 450))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/back1.jpg"))
        self.label.setObjectName("label")
        self.label.raise_()
        pixset = QtGui.QPixmap(r'resources\settings.png')
        pixset = pixset.scaled(51, 41)
        iconset = QtGui.QIcon(pixset)
        self.settings_button = QtWidgets.QPushButton(self.dialog_window)
        self.settings_button.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.settings_button.setText("")
        self.settings_button.setObjectName("settings_button")
        self.settings_button.setCheckable(True)
        self.settings_button.setIcon(iconset)
        self.settings_button.setIconSize(pixset.rect().size())
        self.settings_button.setFixedSize(pixset.rect().size())
        self.settings_button.setFlat(True)
        self.settings_button.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.settings_button.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        pixsend = QtGui.QPixmap('resources\send.png', "r")
        pixsend = pixsend.scaled(51, 41)
        iconsend = QtGui.QIcon(pixsend)
        self.send = QtWidgets.QPushButton(self.dialog_window)
        self.send.setGeometry(QtCore.QRect(430, 349, 41, 41))
        self.send.setText("")
        self.send.setObjectName("send")
        self.send.setIcon(iconsend)
        self.send.setIconSize(pixsend.rect().size())
        self.send.setFixedSize(pixsend.rect().size())
        self.send.setFlat(True)
        self.send.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.send.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        pixmicro = QtGui.QPixmap('resources\micro.png', "r")
        pixmicro = pixmicro.scaled(41, 51)
        iconmicro = QtGui.QIcon(pixmicro)
        self.micro = QtWidgets.QPushButton(self.dialog_window)
        self.micro.setGeometry(QtCore.QRect(15, 340, 41, 51))
        self.micro.setText("")
        self.micro.setObjectName("micro")
        self.micro.setIcon(iconmicro)
        self.micro.setIconSize(pixmicro.rect().size())
        self.micro.setFixedSize(pixmicro.rect().size())
        self.micro.setFlat(True)
        self.micro.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.micro.setStyleSheet('background-color: rgba(255, 255, 255, 0);')

        self.lineEdit = QtWidgets.QLineEdit(self.dialog_window)
        self.lineEdit.setGeometry(QtCore.QRect(95, 348, 301, 43))
        self.lineEdit.setStyleSheet("background-color:rgb(255, 255, 255);\n"
                                    "border: 1px solid black;\n"
                                    "border-radius: 10px;\n"
                                    "\n""")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setPlaceholderText("Введите текст")
        self.dialog = QtWidgets.QTextBrowser(self.dialog_window)
        self.dialog.setGeometry(QtCore.QRect(70, 20, 400, 311))
        self.dialog.setObjectName("dialog")
        self.stackedWidget.addWidget(self.dialog_window)
        self.dialog.setStyleSheet('background-color: rgb(172, 200, 242);')

        self.settings_window = QtWidgets.QWidget()  # окно настроек
        self.label1 = QtWidgets.QLabel(self.settings_window)
        self.label1.setGeometry(QtCore.QRect(-10, -10, 550, 450))
        self.label1.setText("")
        self.label1.setPixmap(QtGui.QPixmap("resources/back1.jpg"))
        self.label1.setObjectName("label")
        self.check_auto_fill = QtWidgets.QCheckBox(self.settings_window)
        self.check_auto_fill.setGeometry(QtCore.QRect(6, 80, 261, 31))
        self.check_auto_fill.setObjectName("check_auto_fill")
        self.settings_button2 = QtWidgets.QPushButton(self.settings_window)
        self.settings_button2.setGeometry(QtCore.QRect(10, 10, 51, 51))
        self.settings_button2.setText("")
        self.settings_button2.setObjectName("settings_button2")
        self.settings_button2.setCheckable(True)
        self.settings_button2.setIcon(iconset)
        self.settings_button2.setIconSize(pixset.rect().size())
        self.settings_button2.setFixedSize(pixset.rect().size())
        self.settings_button2.setFlat(True)
        self.settings_button2.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.settings_button2.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.add_command = QtWidgets.QPushButton(self.settings_window)
        self.add_command.setGeometry(QtCore.QRect(350, 330, 129, 60))
        self.add_command.setObjectName("pushButton")
        self.add_command.setStyleSheet('border-radius: 15px;'
                                       'background-color: white;')
        self.Delete = QtWidgets.QPushButton(self.settings_window)
        self.Delete.setGeometry(QtCore.QRect(201, 330, 129, 60))
        self.Delete.setObjectName("Accept")
        self.Delete.setStyleSheet('border-radius: 15px;'
                                       'background-color: white;')
        pixhelp = QtGui.QPixmap('resources\help.png', "r")
        pixhelp = pixhelp.scaled(51, 51)
        iconhelp = QtGui.QIcon(pixhelp)
        self.help_button = QtWidgets.QPushButton(self.settings_window)
        self.help_button.setGeometry(QtCore.QRect(435, 10, 51, 51))
        self.help_button.setObjectName("help_button")
        self.help_button.setIcon(iconhelp)
        self.help_button.setIconSize(pixset.rect().size())
        self.help_button.setFixedSize(pixset.rect().size())
        self.help_button.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.help_button.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.textList = QtWidgets.QListWidget(self.settings_window)
        self.textList.setGeometry(QtCore.QRect(200, 61, 280, 200))
        self.textList.setObjectName("ListWidget")
        self.textList.setStyleSheet('background-color: rgb(172, 200, 242);')
        self.command_line = QtWidgets.QLineEdit(self.settings_window)
        self.command_line.setGeometry(QtCore.QRect(200, 250, 280, 25))
        self.command_line.setObjectName("lineEdit1")
        self.command_line.setPlaceholderText("Название команды")
        self.url_line = QtWidgets.QLineEdit(self.settings_window)
        self.url_line.setGeometry(QtCore.QRect(200, 275, 280, 25))
        self.url_line.setObjectName("lineEdit2")
        self.url_line.setPlaceholderText("Ссылка или путь к папке")
        self.settings_window.setObjectName("settings_window")
        self.stackedWidget.addWidget(self.settings_window)
        self.stackedWidget.addWidget(self.settings_window)
        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle("Desktop helper")
        Form.setWindowIcon(QtGui.QIcon('resources/ved.png'))
        self.check_auto_fill.setText(_translate("Form", "Обрабатывать голосовую\n команду автоматически"))
        self.add_command.setText(_translate("Form", "Добавить команду"))
        self.Delete.setText(_translate("Form", "Удалить команду"))
