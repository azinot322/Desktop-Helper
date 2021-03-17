import speech_recognition
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget
from dia import Dia_Form
from mainwindow import Main_Form
from settings import Set_Form


class ProjWindow(QMainWindow):
    i = 1

    def __init__(self):
        super(ProjWindow, self).__init__()
        self.ui = Main_Form()
        self.ui.MainWindow(self)
        self.ui.pushButton.clicked.connect(self.hide_dialogue)

    def hide_dialogue(self):
        if self.i == 0:
            Form.hide()
            self.i = 1
        elif self.i == 1:
            Form.show()
            self.i = 0


class ProjWindow2(QMainWindow):
    j = 1
    check = 1
    def __init__(self):
        super(ProjWindow2, self).__init__()
        self.ui = Dia_Form()
        self.ui.Dialoguewindow(self)
        self.ui.settings_button.clicked.connect(self.hide_settings)
        self.ui.micro.clicked.connect(self.record_and_recognize_audio)


    def hide_settings(self):
        if self.j == 0:
            set.hide()
            self.j = 1
        elif self.j == 1:
            set.show()
            self.j = 0

    def record_and_recognize_audio(self):
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



if __name__ == '__main__':
    import sys, os

    app = QApplication(sys.argv)
    window = ProjWindow()
    Form = ProjWindow2()
    set = QWidget()
    ui = Dia_Form()
    Set_Form().setupUi(set)
    window.show()
    sys.exit(app.exec_())
