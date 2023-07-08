import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
dlgMain = QDialog()
dlgMain.setWindowTitle('First GUI')
dlgMain.show()

sys.exit(app.exec_())
