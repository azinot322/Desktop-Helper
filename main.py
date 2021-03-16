from PyQt5.QtWidgets import QMainWindow, QApplication,QWidget
from dia import Dia_Form
from mainwindow import Main_Form


class ProjWindow(QMainWindow):
    def __init__(self):
        super(ProjWindow, self).__init__()
        self.ui = Main_Form()
        self.ui.MainWindow(self)
        self.ui.pushButton.clicked.connect(self.hide_dialogue)
    def hide_dialogue(self):
        Form.hide()



if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    window = ProjWindow()
    Form = QWidget()
    ui = Dia_Form()
    ui.Dialoguewindow(Form)
    window.show()
    Form.show()
    sys.exit(app.exec_())