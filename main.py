import sys
import speech_recognition
from threading import *
from PyQt5 import QtCore, QtGui, QtWidgets

from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QDialog, QStackedWidget, \
    QMenu, QSystemTrayIcon, QAction, QGraphicsColorizeEffect, QLabel, QComboBox, QMessageBox
from PyQt5.QtGui import QPixmap, QIcon, QColor, QImage
from dia import Dia_Form
from mainwindow import Main_Form
import sqlite3
import os
import difflib


class ProjWindow(QLabel):
    trayIcon = None
    startPos = QtCore.QPoint()

    def __init__(self):
        super(ProjWindow, self).__init__()
        pixmap = QPixmap("resources\geralt.png", "r")
        pixmap = pixmap.scaled(400, 630)
        self.setPixmap(pixmap)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.setStyleSheet('QLabel{background-color: rgba(255, 255, 255, 0);}')
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # Создание трея
        self.trayIcon = QSystemTrayIcon(self)
        self.trayIcon.setIcon(QIcon("resources/ved.png"))
        exAction = QAction('Выход', self)
        self.trayIcon.activated.connect(self.show)
        exAction.triggered.connect(self.close)
        trayMenu = QMenu()
        trayMenu.addAction(exAction)
        self.trayIcon.setContextMenu(trayMenu)
        self.trayIcon.show()

    def start_dialogue(self):
        dialog_window = ProjWindow2()
        dialog_window.exec()

    # Перемещение персонажа по экрану
    def mousePressEvent(self, event):
        self.startPos = event.pos()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        delta = event.pos() - self.startPos
        self.move(self.pos() + delta)
        super().mouseMoveEvent(event)

    def mouseDoubleClickEvent(self, event):
        self.start_dialogue()

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Enter:
            self.start_dialogue()

    # Создание контекстного меню при нажатии ПКМ по персонажу
    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)
        openDialogue = contextMenu.addAction('Открыть диалоговое окно')
        hideAction = contextMenu.addAction('Скрыть персонажа')
        quitAction = contextMenu.addAction('Выход')
        action = contextMenu.exec_(self.mapToGlobal(event.pos()))
        if action == quitAction:
            self.close()
        if action == hideAction:
            self.hide()
        if action == openDialogue:
            self.start_dialogue()


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
        self.ui.micro.clicked.connect(self.listening)
        self.ui.send.clicked.connect(self.output)
        self.ui.settings_button.clicked.connect(self.settings_button_open)
        self.ui.settings_button2.clicked.connect(self.settings_button_closed)
        self.ui.send.setAutoDefault(True)
        self.ui.settings_button.setAutoDefault(False)
        self.ui.settings_button2.setAutoDefault(False)
        self.ui.add_command.clicked.connect(self.add_command)
        self.ui.help_button.clicked.connect(self.show_help)
        # self.effect = QGraphicsColorizeEffect(self)
        self.ui.lineEdit.returnPressed.connect(self.ui.send.click)
        self.ui.Delete.clicked.connect(self.delete_command)
        self.row_number = 0
        conn = sqlite3.connect("based.db")
        cursor = conn.cursor()
        for command_name in cursor.execute('SELECT name FROM commands'):
            command_name = transform_to_str(command_name).capitalize()
            self.ui.textList.addItem(command_name)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Up:
            self.auto_fill()
        if event.key() == QtCore.Qt.Key_Alt:
            self.listening()

    def auto_fill(self):
        if self.ui.textList.count() != 0:
            if self.row_number == self.ui.textList.count():
                self.row_number = 0
            command_text = self.ui.textList.item(self.row_number).text()
            self.ui.lineEdit.setText(command_text)
            self.row_number += 1

    def show_help(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setWindowTitle("Справка")
        msg.setText("Программа требует подключения к интернету.\n"
                    "Чтобы начать голосовой ввод - нажмите на иконку микрофона.\n"
                    "Микрофон имеет три состояния:\n"
                    "1. Черный - готов к работе\n"
                    "2. Серый - подключение микрофона\n"
                    "3. Синий - запись, в это время озвучиваете команду\n"
                    "В окне настроек присутсвует список команд, его можно модифицировать - \n"
                    "Заполнив два поля нажмите на кнопку 'Добавить команду',чтобы удалить команду нужно \n"
                    "выбрать команду из списка и нажать на кнопку 'Удалить команду'")
        msg.exec()

    def delete_command(self):
        if self.ui.textList.currentItem():
            command = self.ui.textList.currentItem().text().lower()
            self.ui.textList.takeItem(self.ui.textList.currentRow())
            conn = sqlite3.connect("based.db")
            cursor = conn.cursor()
            cursor.execute(f"DELETE FROM commands WHERE name = '{command}'")
            conn.commit()
            self.row_number = 0

    def add_command(self):
        command_text = self.ui.command_line.text().lower()
        url_text = self.ui.url_line.text()
        if command_text and url_text:
            conn = sqlite3.connect("based.db")
            cursor = conn.cursor()
            cursor.execute(f"INSERT INTO commands VALUES ('{command_text}','{url_text}')")
            conn.commit()
            self.ui.textList.addItem(command_text.capitalize())
        self.ui.command_line.clear()
        self.ui.url_line.clear()
        self.row_number = 0

    def settings_button_open(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.settings_window)

    def settings_button_closed(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.dialog_window)

    def output(self):
        self.clearFocus()
        input_text = self.ui.lineEdit.text()
        if input_text != "":
            self.ui.lineEdit.clear()
            self.ui.dialog.append(input_text)
        input_text = input_text.lower()
        conn = sqlite3.connect("based.db")
        cursor = conn.cursor()
        for command_name, command in cursor.execute('SELECT name, function FROM commands'):
            command = transform_to_str(command)
            command_name = transform_to_str(command_name)
            matcher = difflib.SequenceMatcher(None, command_name, input_text)
            if matcher.ratio() >= 0.8:
                username = os.environ['USERPROFILE']
                username = username.encode('unicode-escape').decode()
                username = username.split(r'\\')
                command = command.replace("username", username[2])
                try:
                    os.system(f'start {command}')
                except FileNotFoundError:
                    self.ui.dialog.append("Не могу выполнить команду")

        if input_text.lower() == "привет":
            self.ui.dialog.append("Привет, путник!")
        self.setFocus()

    def listening(self):
        self.effect = QGraphicsColorizeEffect(self)
        t1 = Thread(target=self.record_and_recognize_audio)
        t1.start()

    def record_and_recognize_audio(self):
        self.ui.micro.setEnabled(False)
        recognizer = speech_recognition.Recognizer()
        microphone = speech_recognition.Microphone()
        with microphone:
            recognized_data = ""
            recognizer.adjust_for_ambient_noise(microphone, duration=2)
            self.ui.lineEdit.clear()
            self.ui.micro.setGraphicsEffect(self.effect)
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
            self.ui.lineEdit.setText(recognized_data.capitalize())
        if self.ui.check_auto_fill.isChecked():
            self.output()
        self.ui.micro.setEnabled(True)
        self.ui.micro.setGraphicsEffect(None)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ProjWindow()
    window.show()
    sys.exit(app.exec_())
