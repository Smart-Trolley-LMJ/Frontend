from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QProgressBar
from PyQt5.QtCore import Qt

class Loader(QDialog):
    def __init__(self):
        super().__init__()

        # self.setWindowTitle("Loading...")
        self.setFixedSize(300, 100)
        self.setWindowFlags(Qt.FramelessWindowHint)
        layout = QVBoxLayout(self)
        self.progress_bar = QProgressBar(self)
        layout.addWidget(self.progress_bar)
        self.progress_bar.setRange(0, 0)  # Indeterminate progress bar

        # Make the dialog modal to prevent interaction with the main window
        self.setModal(True)