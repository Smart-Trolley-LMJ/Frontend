import sys
import threading
from PyQt5.QtWidgets import QApplication, QDialog, QLabel, QVBoxLayout, QPushButton, QProgressBar

class LoaderDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Loading...")
        self.setFixedSize(300, 100)

        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar(self)
        layout.addWidget(QLabel("Please wait while loading..."))
        layout.addWidget(self.progress_bar)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress bar

        # Make the dialog modal to prevent interaction with the main window
        self.setModal(True)

class MainWindow(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Main Window")
        self.setGeometry(100, 100, 400, 200)

        layout = QVBoxLayout(self)
        self.load_button = QPushButton("Load Data", self)
        layout.addWidget(self.load_button)

        self.load_button.clicked.connect(self.start_loading)

    def start_loading(self):
        loader_dialog = LoaderDialog()
        loading_thread = threading.Thread(target=self.perform_request, args=(loader_dialog,))
        loading_thread.start()

        # Show the loader dialog while waiting for the thread to finish
        loader_dialog.exec_()

    def perform_request(self, loader_dialog):
        # Simulate a backend request that takes some time
        import time
        time.sleep(5)

        # The request is completed; close the loader dialog
        loader_dialog.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())
