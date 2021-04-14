import sys
import speech_recognition
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QStackedWidget, \
    QMenu, QSystemTrayIcon, QAction, QGraphicsColorizeEffect, QLabel, QComboBox
from PyQt5.QtGui import QPixmap, QIcon, QColor
from dia import Dia_Form
from mainwindow import Main_Form
import webbrowser
import sqlite3
import os
import difflib


class ProjWindow(QMainWindow):
    trayIcon = None

    def __init__(self):
        super(ProjWindow, self).__init__()
        self.ui = Main_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_dialogue)
        # Создание трея
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

    # Перемещение персонажа по экрану
    def mouseMoveEvent(self, event):
        self.ui.pushButton.move(event.pos())

    # Создание контекстного меню при нажатии ПКМ по персонажу
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        hideAction = contextMenu.addAction('Скрыть персонажа')
        quitAction = contextMenu.addAction('Выход')
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.close()
        if action == hideAction:
            self.hide()


def transform_to_str(sql_tuple):
    sql_string = str(sql_tuple)
    sql_string = sql_string.replace("(", "")
    sql_string = sql_string.replace(")", "")
    sql_string = sql_string.replace(",", "")
    sql_string = sql_string.replace("'", "")
    return sql_string


class ProjWindow2(QDialog):
    def __init__(self):
        super(ProjWindow2, self).__init__()
        self.ui = Dia_Form()
        self.ui.setupUi(self)
        self.ui.micro.clicked.connect(self.record_and_recognize_audio)
        self.ui.send.clicked.connect(self.output)
        self.ui.settings_button.clicked.connect(self.settings_button_open)
        self.ui.settings_button2.clicked.connect(self.settings_button_closed)
        self.ui.send.setAutoDefault(True)
        self.ui.settings_button.setAutoDefault(False)
        self.ui.settings_button2.setAutoDefault(False)
        self.ui.pushButton.clicked.connect(self.add_command)
        # self.effect = QGraphicsColorizeEffect(self)
        self.ui.lineEdit.returnPressed.connect(self.ui.send.click)
        conn = sqlite3.connect("based.db")
        cursor = conn.cursor()
        for command_name in cursor.execute('SELECT name FROM commands'):
            command_name = transform_to_str(command_name).capitalize()
            self.ui.textList.addItem(command_name)

    def add_command(self):
        command_text = self.ui.command_line.text()
        url_text = self.ui.url_line.text()
        url_type = self.ui.combo.currentText()
        if url_type == "Открыть в браузере":
            url_type = "website"
        elif url_type == "Открыть директорию":
            url_type = "directory"
        if command_text and url_text:
            conn = sqlite3.connect("based.db")
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO commands VALUES ('{command_text}','{url_text}','{url_type}')")
            conn.commit()
            self.ui.textList.addItem(command_text)

    def settings_button_open(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_window)

    def settings_button_closed(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dialog_window)

    def output(self):
        input_text = self.ui.lineEdit.text()
        if input_text != "":
            self.ui.lineEdit.clear()
            self.ui.dialog.append(input_text)
        input_text = input_text.lower()
        conn = sqlite3.connect("based.db")
        cursor = conn.cursor()
        for command_name, command, command_type in cursor.execute('SELECT name, function, type FROM commands'):
            command = transform_to_str(command)
            command_name = transform_to_str(command_name)
            command_type = transform_to_str(command_type)
            matcher = difflib.SequenceMatcher(None, command_name, input_text)
            if matcher.ratio() >= 0.8:
                if command_type == "website":
                    try:
                        webbrowser.open_new_tab(command)
                    except:
                        continue
                elif command_type == "directory":
                    username = os.environ['USERPROFILE']
                    username = username.encode('unicode-escape').decode()
                    username = username.split(r'\\')
                    try:
                        command = command.replace("username", username[2])
                    except:
                        continue
                    os.startfile(command)

        if input_text.lower() == "привет":
            self.ui.dialog.append("Привет, путник!")

    def record_and_recognize_audio(self):
        # self.ui.micro.setGraphicsEffect(self.effect)
        # self.ui.micro.setEnabled(False)
        self.ui.lineEdit.clear()
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
                # self.ui.micro.setEnabled(True)
                # self.ui.micro.setGraphicsEffect(None)
                pass
            except speech_recognition.RequestError:
                print("Check your Internet Connection, please")
                # self.ui.micro.setEnabled(True)
                # self.ui.micro.setGraphicsEffect(None)

            self.ui.lineEdit.setText(recognized_data)
            # self.ui.micro.setEnabled(True)
            # self.ui.micro.setGraphicsEffect(None)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProjWindow()
    window.show()
    sys.exit(app.exec_())
