import os
from Custom_Widgets.Widgets import QWidget, QVBoxLayout, QDialog, QObject, QEvent, QMessageBox
from UI.Images.checkout import Ui_Dialog
from UI.Images.receiptItem import Ui_Form
from virtual_numpad import VirtualNumpad
from Pages.cart.hubtelPage import QRCodeDialog
from Pages.cart.paymentConfirmed import ConfirmPayment
from Pages.cart.succesful import Success
from Pages.cart.failed import Failed
from PyQt5.QtCore import Qt
import requests
import json
import threading
from utils.loader import Loader
import os

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
    def __init__(self, array_data, user_id, main_ui, new_userID):
        super(QWidget, self).__init__()
        self.ui = Ui_Dialog()
        self.user_id = user_id
        self.new_userID = new_userID #function to create a new userID
        self.setWindowFlags(Qt.FramelessWindowHint)
        # self.receipt = receipt
        self.data = array_data
        self.main_ui = main_ui
        self.url = os.environ.get("URL")
        self.ui.setupUi(self)

        # Create a QHBoxLayout for the items layout
        self.items_layout = QVBoxLayout()
        self.ui.checkoutScrollAreaWidget.setLayout(self.items_layout)
        self.ui.paymentCostLabel.setText(self.main_ui.displayCost.toPlainText())

        self.display_items(self.data)

        self.ui.cancelPaymentBtn.clicked.connect(self.close)
        self.ui.proceedBtn.clicked.connect(self.issue_payment)
        # self.receipt = []

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
        momoNum = self.ui.lineEdit.text()
        if momoNum == '' or len(momoNum)<10:
            QMessageBox.warning(self, 'Error', 'Please Check the length of the Number')
            return
        # response = requests.post(f'{self.url}{self.user_id}', json=
        #                          {
        #                              "mobile_number": self.ui.lineEdit.text()
        #                          })
        self.start_loading()
        if self.response.status_code != 200:
            QMessageBox.warning(self, 'Error', 'Please Enter a Valid Mobile Money Number')
            return
        self.response = self.response.content.decode("utf-8")
        self.response = json.loads(self.response)
        keys = ['pay_link', 'id']
        payment_order = {key: self.response[key] for key in keys if key in self.response}
        print(f'Checkout: {self.response} UserId: {self.user_id}')
        if self.response:
            hubtelPage = QRCodeDialog(payment_order['pay_link'], payment_order['id'])
            hubtelPage.exec_()

            paymentConfirm = ConfirmPayment(payment_order['id'])
            message, status = paymentConfirm.start_loading()

            print(f"{message}, status_code:{status}")
            pass

        if status == 400:
            failedDialog = Failed()
            failedDialog.exec_()

        if status == 200:
            successDialog = Success(self.main_ui,self.new_userID)
            successDialog.exec_()
            self.close()

    def start_loading(self):
        loader_dialog = Loader()
        loading_thread = threading.Thread(target=self.perform_request, args=(loader_dialog,))
        loading_thread.start()

        # Show the loader dialog while waiting for the thread to finish
        loader_dialog.exec_()
        return 

    def perform_request(self, loader_dialog):
        # Simulate a backend request that takes some time
        try:
            self.response = requests.post(f'{self.url}/payment/{self.user_id}', json=
                                    {
                                        "mobile_number": self.ui.lineEdit.text()
                                    })
        except:
            print("Error occured in perfor")
        # if self.response.status_code != 200:
        #     QMessageBox.warning(self, 'Error', 'Please Enter a Valid Mobile Money Number')
        #     return
        # self.response = self.response.content.decode("utf-8")
        # self.response = json.loads(self.response)

        # The request is completed; close the loader dialog
        loader_dialog.accept()
