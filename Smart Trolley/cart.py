
from os import getcwd
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from Custom_Widgets.Widgets import QPushButton,QMessageBox, QDialog, QTableWidgetItem, QVBoxLayout,QLabel, QWidget
from PyQt5.QtCore import pyqtSignal
from Model.rc522 import RC522
from Model.worker import Worker
import time
import json
import threading
try:
    from mfrc522 import SimpleMFRC522
except:
    pass
from Pages.cart.checkoutPage import checkoutDialog
from utils.loader import Loader
import requests
import os

CURRENT_WORKING_DIRECTORY = getcwd()
# self.url = "https://smtrolley.onrender.com/"



class DialogBox(QDialog):
    def __init__(self):
        super().__init__() 
        self.add = False
        self.setModal(True)

        self.setWindowTitle("Delete Item from Cart")

        self.layout = QVBoxLayout()
        message = QLabel("Please scan an item to remove from cart")
        done_button = QPushButton("Done")
        done_button.clicked.connect(self.close)
        
        self.layout.addWidget(message)
        self.layout.addWidget(done_button)
        self.setLayout(self.layout)

        

       
ids = []

class ShoppingCart(QWidget):
    def __init__(self, ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui
        self.add = True
        self.user_id = 0
        self.receipt = []
        try:
            self.reader = SimpleMFRC522()
        except:
            self.reader = RC522()
        self.set_UserID()
        self.url = os.environ.get("URL")
        rfid_worker = Worker()
        rfid_worker.rfidDetected.connect(self.execute)
        
        rfid_worker.start(self.read_RFID)

        # Delete item from cart
        # self.ui.deleteBtn.clicked.connect(lambda: print('Bread'))
        self.ui.deleteBtn.clicked.connect(self.delete)

        
        # Checkout
        self.ui.checkoutBtn.clicked.connect(self.checkout)
        self.checkoutFlag = False
    
    def set_UserID(self):
        try:
            self.user_id = requests.get(f'{self.url}/users').content.decode('utf-8')
            self.user_id = json.loads(self.user_id)['id']
            print(f"New Session User ID: {self.user_id}")
        except:
            print("An error occured in getting user id")
            pass
        

    def read_RFID(self, worker: Worker):
        while True:
            self.id, text = self.reader.read()
            text = text[:36]
            try:
                a = requests.get(f'{self.url}/inventories/{text}')
                print(f'Status code:{a.status_code}')
                if a.status_code != 200:
                    QMessageBox.warning(self, 'Error', 'ID is not in our database')
                    pass
                else:
                    a = a.content.decode('utf-8')
                    time.sleep(0.5)
                    worker.add_or_remove_item(a)
            except:
                print("Error occured in retrieving item")
                pass

    def execute(self, item):
        # Query database for item name with the id from the 
        item = json.loads(item)
        print(item)
        self.id = item["id"]
        if self.checkoutFlag:
            return
        if self.add: self.add_item(item)
        else: self.remove_item(item)
        

    def add_item(self, item):
        print("Adding an Item")
        name = item["name"]
        unit_cost = item["product_info"]["price"]
        row_count = self.ui.itemTable_2.rowCount()

        # Check if the item already exists in the table
        if self.id not in ids: ####  Use dictionary key value instead
            for row in range(row_count):
                item_name = self.ui.itemTable_2.item(row, 0).text()
                if item_name == name and self.id not in ids:
                    # Item already exists, increment quantity and recalculate cost
                    current_quantity = int(self.ui.itemTable_2.item(row, 1).text())
                    new_quantity = current_quantity + 1
                    self.ui.itemTable_2.setItem(row, 1, QTableWidgetItem(str(new_quantity)))

                    current_cost = float(self.ui.itemTable_2.item(row, 3).text())
                    new_cost = current_cost + unit_cost
                    self.ui.itemTable_2.setItem(row, 3, QTableWidgetItem(str(new_cost)))
                    ids.append(self.id)
                    self.calculate(unit_cost)
                    return
    
            # Item does not exist, add a new row to the table
            self.ui.itemTable_2.setRowCount(row_count + 1)
            self.ui.itemTable_2.setItem(row_count, 0, QTableWidgetItem(name))
            self.ui.itemTable_2.setItem(row_count, 1, QTableWidgetItem(str(1)))
            self.ui.itemTable_2.setItem(row_count, 2, QTableWidgetItem(str(unit_cost)))
            self.ui.itemTable_2.setItem(row_count, 3, QTableWidgetItem(str(unit_cost)))
            ids.append(self.id)
            self.calculate(unit_cost)
        print(ids)
        
    
    def calculate(self, cost):
        total_cost = float(self.ui.displayCost.toPlainText()) + float(cost)
        print(total_cost, float(cost))

        self.ui.displayCost.setText(f'{total_cost}')
    
    def get_all_table_data(self):
        self.all_data = []

        for row in range(self.ui.itemTable_2.rowCount()):
            row_data = []
            for col in range(self.ui.itemTable_2.columnCount()):
                item = self.ui.itemTable_2.item(row, col)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")

            self.all_data.append(row_data)


    def checkout(self):
        # self.ui.displayCost.setText(f'{0.00}')
        self.checkoutFlag=True
        if self.ui.itemTable_2.rowCount() == 0:
            QMessageBox.warning(self, 'Error', 'Table is empty. Add items before checking out.')
            return

        try:
            
            for id in ids:
                self.receipt.append(
                    {
                        "id":id,
                        "quantity":1
                    }
                ) 
            # response = requests.post(f'{self.url}cart/checkout/{self.user_id}', json=self.receipt)
            self.start_loading()
            self.get_all_table_data()
            print(f'Cart Checkout: {self.response.content} \n user_id:{self.user_id}') 
            
            # dialog = checkoutDialog(self.all_data, self.receipt, self.user_id, self.ui, self.set_UserID)
            dialog = checkoutDialog(self.all_data, self.user_id, self.ui, self.set_UserID)
            dialog.exec_()
            self.checkoutFlag = False
        except:
            pass

    def delete(self):
        if self.ui.itemTable_2.rowCount() == 0:
            QMessageBox.warning(self, 'Error', 'Table is empty.')
            return
        self.add = False 
        print("Here")
        dialog = DialogBox()
        dialog.exec_()
        self.add = True
    

    def remove_item(self, item):
        
        row_count = self.ui.itemTable_2.rowCount()
        print("Removing Item")
        name = item["name"]
        unit_cost = item["product_info"]["price"]
        if self.id in ids: ####  Use dictionary key value instead
            for row in range(row_count):
                item_name = self.ui.itemTable_2.item(row, 0).text()
                if item_name == name :
                    print(f'{item_name} is being removed, price: Ghs{unit_cost}')
                    # Item already exists, increment quantity and recalculate cost
                    current_quantity = int(self.ui.itemTable_2.item(row, 1).text())
                    current_cost = float(self.ui.itemTable_2.item(row, 3).text())
                    if current_quantity >1:
                        self.ui.itemTable_2.setItem(row, 1, QTableWidgetItem(str(current_quantity - 1)))                        
                        current_cost -= unit_cost
                        self.ui.itemTable_2.setItem(row, 3, QTableWidgetItem(str(current_cost)))
                    else:
                        self.ui.itemTable_2.removeRow(row)
                    self.calculate(-unit_cost)
                    break
                    
                
            ids.remove(self.id)
                    
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
            self.response = requests.post(f'{self.url}/cart/checkout/{self.user_id}', json=self.receipt)
            loader_dialog.accept()
        # The request is completed; close the loader dialog
        except:
            print("Error occured in performing requests")
            pass
        



    


