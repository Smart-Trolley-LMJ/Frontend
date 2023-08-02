import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QLabel, QVBoxLayout
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Dialog Example")
        self.setGeometry(100, 100, 300, 200)

        self.button = QPushButton("Open Dialog", self)
        self.button.clicked.connect(self.open_dialog)
        self.setCentralWidget(self.button)

    def open_dialog(self):
        self.dialog = QDialog(self)
        self.dialog.setWindowTitle("Dialog")
        
        layout = QVBoxLayout()
        label = QLabel("This is a dialog.")
        layout.addWidget(label)
        self.dialog.setLayout(layout)
        
        self.dialog.show()

        # Automatically close the dialog after 2 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.close_dialog)
        self.timer.start(2000)  # 2000 milliseconds = 2 seconds

    def close_dialog(self):
        self.dialog.close()
        self.timer.stop()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())
