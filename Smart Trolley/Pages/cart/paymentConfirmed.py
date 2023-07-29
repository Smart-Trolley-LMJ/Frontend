
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Custom_Widgets.Widgets import QLabel, QPushButton,QDialog, QVBoxLayout
import requests
import json


class ConfirmPayment(QDialog):
    def __init__(self, order_id):
        super().__init__()
        self.setModal(True)
        self.order_id = order_id

        self.setWindowTitle("Delete Item from Cart")
        
        self.layout = QVBoxLayout()
        message = QLabel("Please scan an item to remove from cart")
        done_button = QPushButton("Done")
        done_button.clicked.connect(self.check_payment_completed)
        
        self.layout.addWidget(message)
        self.layout.addWidget(done_button)
        self.setLayout(self.layout)

    def check_payment_completed(self):
        payment = requests.get(f'https://smtrolley.onrender.com/payment/check/{self.order_id}'
                               ).content.decode('utf-8')
        payment = json.loads(payment)
        print(f"Page Loaded: {payment}")

        return payment


# Page Loaded: {'id': 'df24fb33-fa6c-4cf6-8620-85bece51c19a', 'pay_link_id': '854c24e27ba844a4825ea9c1daf5b2d9', 'date_created': '2023-07-29T21:30:39.752683', 'is_paid': True, 'total_cost': 1.0, 'user_id': '013855c6-a0ad-4fab-8d36-fa7a43628576', 'pay_link': 
# 'https://p.hbtl.co/G4E5eS'}
