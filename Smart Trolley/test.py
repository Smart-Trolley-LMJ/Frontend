import qrcode
import sys
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from io import BytesIO

def generate_qr_code(data):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    buffer = BytesIO()
    img.save(buffer, format="PNG")
    return buffer.getvalue()

class QRCodeDialog(QDialog):
    def __init__(self, qr_data, parent=None):
        super().__init__(parent)
        self.qr_data = qr_data
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        qr_image_data = generate_qr_code(self.qr_data)

        qr_image = QImage.fromData(qr_image_data)
        qr_pixmap = QPixmap.fromImage(qr_image)

        qr_label = QLabel(self)
        qr_label.setPixmap(qr_pixmap.scaled(200, 200, Qt.KeepAspectRatio))

        layout.addWidget(qr_label)

        close_button = QPushButton("Close")
        close_button.clicked.connect(self.close)

        layout.addWidget(close_button)

        self.setLayout(layout)
        self.setWindowTitle("QR Code")
        self.setModal(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    qr_data = "https://www.example.com"  # Replace this with the data you want to encode

    dialog = QRCodeDialog(qr_data)
    dialog.exec_()

    sys.exit(app.exec_())
