from PyQt5.QtWidgets import QDialog, QLabel, QVBoxLayout, QProgressBar

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