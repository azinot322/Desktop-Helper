import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QStackedWidget, \
    QMenu, QSystemTrayIcon, QAction
from PyQt5.QtGui import QPixmap, QIcon
from dia import Dia_Form
from mainwindow import Main_Form


class ProjWindow(QMainWindow):

    trayIcon = None
    def __init__(self):
        super(ProjWindow, self).__init__()
        self.ui = Main_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_dialogue)
        #Создание трея
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon('ved.png'))
        showAction = QAction('Открыть', self)
        exAction = QAction('Выход', self)
        showAction.triggered.connect(self.show)
        exAction.triggered.connect(self.close)
        trayMenu = QMenu()
        trayMenu.addAction(showAction)
        trayMenu.addAction(exAction)
        self.trayIcon.setContextMenu(trayMenu)
        self.trayIcon.show()

    def start_dialogue(self):
        dialog_window = ProjWindow2()
        dialog_window.exec()

    #Перемещение персонажа по экрану
    def mouseMoveEvent(self, event):
        self.ui.pushButton.move(event.pos())

    #Создание контекстного меню при нажатии ПКМ по персонажу
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        hideAction = contextMenu.addAction('Скрыть персонажа')
        quitAction = contextMenu.addAction('Выход')
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.close()
        if action == hideAction:
            self.hide()


class ProjWindow2(QDialog):

    def __init__(self):
        super(ProjWindow2, self).__init__()
        self.ui = Dia_Form()
        self.ui.setupUi(self)
        self.ui.micro.clicked.connect(self.record_and_recognize_audio)
        self.ui.send.clicked.connect(self.output)
        self.ui.settings_button.clicked[bool].connect(self.settings_button_clicked)


    def settings_button_clicked(self, pressed):
        if pressed:
            self.ui.stackedWidget.setCurrentWidget(self.ui.settings_window)
        else:
            self.ui.stackedWidget.setCurrentWidget(self.ui.dialog_window)

    def output(self):
        input_text = self.ui.lineEdit.text()
        if input_text != "":
            self.ui.lineEdit.clear()
            self.ui.dialog.append(input_text)
        if input_text.lower() == "привет":
            self.ui.dialog.append("Привет, путник!")



    def record_and_recognize_audio(self):
        self.ui.micro.setEnabled(False)
        print(123)
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        with microphone:
            recognized_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)

            try:
                print("Listening...")
                audio = recognizer.listen(microphone, 5, 5)
            except speech_recognition.WaitTimeoutError:
                print("Can you check if your microphone is on, please?")
                return
            try:
                print("Started recognition...")
                recognized_data = recognizer.recognize_google(audio, language="ru").lower()
            except speech_recognition.UnknownValueError:
                pass
            except speech_recognition.RequestError:
                print("Check your Internet Connection, please")

            self.ui.lineEdit.setText(recognized_data)
            self.ui.micro.setEnabled(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProjWindow()
    window.show()
    sys.exit(app.exec_())

