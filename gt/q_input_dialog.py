import sys
from PyQt5.QtWidgets import *


class DlgMain(QDialog):

    def __init__(self):
        super().__init__()
        self.resize(200, 200)

        self.btn = QPushButton('Show Input', self)
        self.btn.move(35, 50)
        self.btn.clicked.connect(self.evt_btn_clicked)

    def evt_btn_clicked(self):
        i_age, b_ok = QInputDialog.getInt(self, 'Title', 'Enter your age:', 18, 18, 65, 1)
        if b_ok:
            QMessageBox.information(self, 'Age', 'Your age is ' + str(i_age))
        else:
            QMessageBox.critical(self, 'Canceled', 'User hae clicked "Cancel"')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlgMain = DlgMain()
    dlgMain.show()
    sys.exit(app.exec_())
