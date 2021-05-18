import PyQt5


class Main_Form(object):
    def setupUi(self, Form):
        Form.setWindowFlags(PyQt5.QtCore.Qt.FramelessWindowHint)
        Form.setObjectName("DesktopHelper")
        Form.resize(400, 630)
        pixmap = PyQt5.QtGui.QPixmap("resources\geralt.png", "r")
        pixmap = pixmap.scaled(400, 630)
        icon = PyQt5.QtGui.QIcon(pixmap)
        self.pushButton = PyQt5.QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(pixmap.rect().size())
        self.pushButton.setFixedSize(pixmap.rect().size())
        self.pushButton.setFlat(True)
        self.pushButton.setStyleSheet('background-color: rgba(255, 255, 255, 0);')
        self.retranslateUi(Form)
        PyQt5.QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = PyQt5.QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
