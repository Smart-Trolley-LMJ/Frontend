import sys
from PyQt5 import QtWidgets

class OnScreenKeyboard(QtWidgets.QWidget):
    def __init__(self, search_bar):
        super().__init__()
        self.search_bar = search_bar
        self.init_ui()

    def init_ui(self):
        layout = QtWidgets.QGridLayout()

        keyboard_layout = [
            ['Q', 'W', 'E', 'R', 'T', 'Y', 'U', 'I', 'O', 'P'],
            ['A', 'S', 'D', 'F', 'G', 'H', 'J', 'K', 'L'],
            ['Z', 'X', 'C', 'V', 'B', 'N', 'M']
        ]

        for row_idx, row in enumerate(keyboard_layout):
            for col_idx, key in enumerate(row):
                button = QtWidgets.QPushButton(key)
                button.clicked.connect(lambda _, key=key: self.on_key_press(key))
                layout.addWidget(button, row_idx, col_idx)

        self.setLayout(layout)
        self.setWindowTitle('On-Screen Keyboard')

    def on_key_press(self, key):
        current_text = self.search_bar.text()
        self.search_bar.setText(current_text + key)

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.init_ui()

    def init_ui(self):
        self.search_bar = QtWidgets.QLineEdit()
        self.search_bar.returnPressed.connect(self.on_search)
        self.setCentralWidget(self.search_bar)
        self.search_bar.installEventFilter(self)

        self.keyboard = None

    def eventFilter(self, obj, event):
        if obj == self.search_bar and event.type() == QtWidgets.QEvent.MouseButtonPress:
            if not self.keyboard:
                self.keyboard = OnScreenKeyboard(self.search_bar)
                self.keyboard.show()
            else:
                self.keyboard.close()
                self.keyboard = None

        return super().eventFilter(obj, event)

    def on_search(self):
        search_text = self.search_bar.text()
        # Perform search operation with search_text
        print("Search:", search_text)
        self.search_bar.clear()

# Create the main application
app = QtWidgets.QApplication(sys.argv)
window = MainWindow()

# Show the main window
window.show()

# Start the application event loop
sys.exit(app.exec_())
