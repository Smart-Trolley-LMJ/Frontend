from Custom_Widgets.Widgets import QDialog, QVBoxLayout, QLabel, QPushButton

class Failed(QDialog):
    def __init__(self):
        super().__init__()
        self.add = False
        self.setModal(True)

        self.setWindowTitle("Transaction Failed")

        self.layout = QVBoxLayout()
        message = QLabel("There was an error with your payment, please try again")
        done_button = QPushButton("Done")
        done_button.clicked.connect(self.close)
        
        self.layout.addWidget(message)
        self.layout.addWidget(done_button)
        self.setLayout(self.layout)