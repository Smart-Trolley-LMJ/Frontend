import sys
import os
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QDate
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from Custom_Widgets.Widgets import loadJsonStyle


class my_app(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        # loadJsonStyle(self, self.ui)


        

def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    
    
    sys.exit(app.exec_())

create_app() 