
from Custom_Widgets.Widgets import QLabel, QPushButton,QDialog, QVBoxLayout
from utils.loaderDialog import LoaderDialog
import requests
import json
import threading


class ConfirmPayment():
    def __init__(self, order_id):
        super().__init__()
        self.order_id = order_id
        self.payment= ''
        self.status = 0

    def start_loading(self):
        loader_dialog = LoaderDialog()
        loading_thread = threading.Thread(target=self.perform_request, args=(loader_dialog,))
        loading_thread.start()

        # Show the loader dialog while waiting for the thread to finish
        loader_dialog.exec_()
        return self.payment, self.status

    def perform_request(self, loader_dialog):
        # Simulate a backend request that takes some time
        self.check_payment_completed()

        # The request is completed; close the loader dialog
        loader_dialog.accept()

    def check_payment_completed(self):
        payment = requests.get(f'https://smtrolley.onrender.com/payment/check/{self.order_id}'
                               )
        self.status = payment.status_code
        self.payment = json.loads(payment.content.decode('utf-8'))
        
        if self.status == 400:
            print("Error with request")
        elif self.status:
            print("Payment Succesful, You may exit with your items")
            pass
        


# Page Loaded: {'id': 'df24fb33-fa6c-4cf6-8620-85bece51c19a', 'pay_link_id': '854c24e27ba844a4825ea9c1daf5b2d9', 'date_created': '2023-07-29T21:30:39.752683', 'is_paid': True, 'total_cost': 1.0, 'user_id': '013855c6-a0ad-4fab-8d36-fa7a43628576', 'pay_link': 
# 'https://p.hbtl.co/G4E5eS'}
