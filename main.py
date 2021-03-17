from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget
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
    def __init__(self):
        super(ProjWindow2, self).__init__()
        self.ui = Dia_Form()
        self.ui.Dialoguewindow(self)
        self.ui.settings_button.clicked.connect(self.hide_settings)
    def hide_settings(self):
        if self.j == 0:
            set.hide()
            self.j = 1
        elif self.j == 1:
            set.show()
            self.j = 0

if __name__ == '__main__':
    import sys




    app = QApplication(sys.argv)
    window = ProjWindow()
    Form = ProjWindow2()
    set = QWidget()
    ui = Dia_Form()
    Set_Form().setupUi(set)
    window.show()
    sys.exit(app.exec_())