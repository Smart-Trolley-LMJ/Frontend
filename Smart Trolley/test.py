import sys
from PyQt5.QtWidgets import QApplication, QDialog, QVBoxLayout, QLabel, QPushButton, QMainWindow


class MyDialog(QDialog):
    def __init__(self, parent=None):
        super(MyDialog, self).__init__(parent)
        self.setWindowTitle("Dialog Box")
        self.setModal(True)

        layout = QVBoxLayout()
        self.label = QLabel("Dialog Box is displayed")
        layout.addWidget(self.label)

        self.close_button = QPushButton("Close Dialog")
        self.close_button.clicked.connect(self.accept)
        layout.addWidget(self.close_button)

        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("Main Window")

        self.add_value = True

        button = QPushButton("Open Dialog")
        button.clicked.connect(self.open_dialog)
        self.setCentralWidget(button)

    def open_dialog(self):
        self.add_value = False  # Set add_value to False

        dialog = MyDialog(self)
        if dialog.exec_() == QDialog.Accepted:
            self.add_value = True  # Set add_value back to True

        # Optional: Display add_value state after the dialog is closed
        print("add_value:", self.add_value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
