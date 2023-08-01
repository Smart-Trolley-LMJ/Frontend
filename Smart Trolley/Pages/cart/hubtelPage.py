import qrcode
# from Custom_Widgets.Widgets import QWidget, QVBoxLayout, QDialog, QObject, QEvent
from PyQt5.QtWidgets import QApplication, QLabel, QVBoxLayout, QPushButton, QDialog
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import Qt
from io import BytesIO
from UI.Images.qrCodeGenerator import Ui_IssuePayment

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
    def __init__(self, payment_link, payment_orderID):
        super().__init__()
        self.payment_link = payment_link
        self.ui = Ui_IssuePayment()
        self.ui.setupUi(self)
        self.ui.confirmPaymentBtn.clicked.connect(self.close)
        self.add_qrcode_widget()

    def add_qrcode_widget(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        qr_image_data = generate_qr_code(self.payment_link)

        qr_image = QImage.fromData(qr_image_data)
        qr_pixmap = QPixmap.fromImage(qr_image)

        qr_label = QLabel(self)
        qr_label.setPixmap(qr_pixmap.scaled(200, 200, Qt.KeepAspectRatio))

        layout.addWidget(qr_label)

        self.ui.qrCodeWidget.setLayout(layout)
        self.setWindowTitle("QR Code")
        self.setModal(True)


