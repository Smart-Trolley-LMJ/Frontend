import os
from Custom_Widgets.Widgets import QWidget, QVBoxLayout, QDialog, QObject, QEvent
from UI.Images.checkout import Ui_Dialog
from UI.Images.receiptItem import Ui_Form
from virtual_numpad import VirtualNumpad
from Pages.cart.hubtelPage import WebPageViewer
from Pages.cart.paymentConfirmed import ConfirmPayment
import requests
import json

CURRENT_WORKING_DIRECTORY = os.getcwd()

class ItemCard(QWidget):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.populate_data(data)

    def populate_data(self, data):
        self.ui.item_name.setText(data[0])
        self.ui.item_cost.setText(data[3])
        self.ui.item_qty.setText(data[1])

class checkoutDialog(QDialog):
    def __init__(self, array_data, receipt, user_id):
        super(QWidget, self).__init__()
        self.ui = Ui_Dialog()
        self.user_id = user_id
        self.receipt = receipt
        self.data = array_data
        self.url = "https://smtrolley.onrender.com/payment/"
        self.ui.setupUi(self)

        # Create a QHBoxLayout for the items layout
        self.items_layout = QVBoxLayout()
        self.ui.checkoutScrollAreaWidget.setLayout(self.items_layout)

        self.display_items(self.data)

        self.ui.cancelPaymentBtn.clicked.connect(self.close)
        self.ui.proceedBtn.clicked.connect(self.issue_payment)
        self.receipt = []

        # Pop up Numpad
        self.numpad = VirtualNumpad()
        self.ui.lineEdit.installEventFilter(self)

    def eventFilter(self, obj: QObject, event: QEvent) -> bool:
        if event.type() == 2 and obj == self.ui.lineEdit:
            self.numpad.line_edit = obj
            self.numpad.show()
            return True
        return super().eventFilter(obj, event)

    def display_items(self, filtered_data):
        for item_data in filtered_data:
            item_card = ItemCard(item_data)
            self.items_layout.addWidget(item_card)

    def issue_payment(self):
        response = requests.post(f'{self.url}{self.user_id}', json=
                                 {
                                     "mobile_number": self.ui.lineEdit.text()
                                 }).content.decode("utf-8")
        response = json.loads(response)
        keys = ['pay_link', 'id']
        payment_order = {key: response[key] for key in keys if key in response}
        print(f'Checkout: {response} UserId: {self.user_id}')
        if response:
            hubtelPage = WebPageViewer(payment_order['pay_link'], payment_order['id'])
            hubtelPage.exec_()

            paymentConfirm = ConfirmPayment(payment_order['id'])
            message, status = paymentConfirm.start_loading()

            print(f"{message}, status_code:{status}")

        if status == 400:
            print("There was a problem with your payment, Please try again")
            pass

        self.close()

