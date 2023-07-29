from Custom_Widgets.Widgets import QDialog, QLineEdit
from PyQt5.QtCore import Qt

from UI.Images.numpad import Ui_Numpad
import os

CURRENT_WORKING_DIRECTORY = os.getcwd()

class VirtualNumpad(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Numpad()
        self.ui.setupUi(self)
        
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setModal(True)

        self.line_edit = QLineEdit()
        self.ui.No0.clicked.connect(lambda: self.line_edit.insert('0'))
        self.ui.No1.clicked.connect(lambda: self.line_edit.insert('1'))
        self.ui.No2.clicked.connect(lambda: self.line_edit.insert('2'))
        self.ui.No3.clicked.connect(lambda: self.line_edit.insert('3'))
        self.ui.No4.clicked.connect(lambda: self.line_edit.insert('4'))
        self.ui.No5.clicked.connect(lambda: self.line_edit.insert('5'))
        self.ui.No6.clicked.connect(lambda: self.line_edit.insert('6'))
        self.ui.No7.clicked.connect(lambda: self.line_edit.insert('7'))
        self.ui.No8.clicked.connect(lambda: self.line_edit.insert('8'))
        self.ui.No9.clicked.connect(lambda: self.line_edit.insert('9'))
        self.ui.PlusBtn.clicked.connect(lambda: self.line_edit.insert('+'))
        self.ui.DelBtn.clicked.connect(lambda: self.line_edit.backspace())
        self.ui.doneBtn.clicked.connect(lambda: self.close())
        
        
        
        