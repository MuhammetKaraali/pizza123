from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

app = QApplication(sys.argv)

window = QWidget()
window.resize(400,350)
window.show()
app.exec_()