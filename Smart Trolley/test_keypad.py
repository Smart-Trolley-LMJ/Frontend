from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit
import sys
from virtual_keyboard import VirtualKeyboard
from virtual_numpad import VirtualNumpad
class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 800, 600)
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)

        vbox = QVBoxLayout()
        self.input_field1 = QLineEdit()
        self.input_field2 = QLineEdit()

        vbox.addWidget(self.input_field1)
        vbox.addWidget(self.input_field2)

        central_widget.setLayout(vbox)

        self.virtual_keyboard = VirtualKeyboard()
        self.input_field1.installEventFilter(self)
        self.input_field2.installEventFilter(self)

        self.virtual_numpad = VirtualNumpad()
        self.input_field2.installEventFilter(self)

    def eventFilter(self, obj, event):
        if event.type() == 2 :
            if(obj == self.input_field1) :
                self.virtual_keyboard.line_edit = obj
                self.virtual_keyboard.show()
            if obj == self.input_field2:
                self.virtual_numpad.line_edit = obj
                self.virtual_numpad.show()
            return True
        return super().eventFilter(obj, event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyMainWindow()
    window.show()
    sys.exit(app.exec_())
