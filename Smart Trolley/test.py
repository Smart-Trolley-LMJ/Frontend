import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices

def open_payment_link(payment_link):
    # Try to open the payment link in the default web browser
    if QDesktopServices.openUrl(QUrl(payment_link)):
        print("Payment link opened successfully.")
    else:
        # If there is an error, show an error message to the user
        QMessageBox.critical(None, "Error", "Failed to open the payment link.", QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    payment_link = "https://example.com/payment"  # Replace this with the actual payment link received from the backend
    open_payment_link(payment_link)
    sys.exit(app.exec_())
A