
from os import getcwd
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from Custom_Widgets.Widgets import QPushButton,QMessageBox, QDialog, QTableWidgetItem,QDialogButtonBox, QVBoxLayout,QLabel
from PyQt5.QtCore import pyqtSignal
from Model.rc522 import RC522
from Model.worker import Worker
import time
import json
from threading import Thread
try:
    from mfrc522 import SimpleMFRC522
except:
    pass
from Pages.cart.checkoutPage import checkoutDialog
import requests

CURRENT_WORKING_DIRECTORY = getcwd()
url = "https://smtrolley.onrender.com/"

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

class ShoppingCart():
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
        rfid_worker = Worker()
        rfid_worker.rfidDetected.connect(self.execute)
        
        rfid_worker.start(self.read_RFID)

        # Delete item from cart
        # self.ui.deleteBtn.clicked.connect(lambda: print('Bread'))
        self.ui.deleteBtn.clicked.connect(self.delete)

        
        # Checkout
        self.ui.checkoutBtn.clicked.connect(self.checkout)
    
    def set_UserID(self):
        self.user_id = requests.get(f'{url}users').content.decode('utf-8')
        self.user_id = json.loads(self.user_id)['id']
        print(f"New Session User ID: {self.user_id}")
        

    def read_RFID(self, worker: Worker):
        while True:
            self.id, text = self.reader.read()
            # text.decode('utf-8')
            a = requests.get(f'{url}inventories/{text}').content.decode('utf-8')
            print(a)
            time.sleep(2)
            worker.add_or_remove_item(a)

    def execute(self, item):
        # Query database for item name with the id from the 
        item = json.loads(item)
        print(item)
        self.id = item["id"]
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
        try:
            
            for id in ids:
                self.receipt.append(
                    {
                        "id":id,
                        "quantity":1
                    }
                ) 
            response = requests.post(f'{url}cart/checkout/{self.user_id}', json=self.receipt)
            self.get_all_table_data()
            print(f'Cart Checkout: {response.content} \n user_id:{self.user_id}') 
            
            # dialog = checkoutDialog(self.all_data, self.receipt, self.user_id, self.ui, self.set_UserID)
            dialog = checkoutDialog(self.all_data, self.user_id, self.ui, self.set_UserID)
            dialog.exec_()
        except:
            pass

    def delete(self):
        self.add = False 
        print("Here")
        dialog = DialogBox()
        if dialog.exec_() == QDialog.Accepted:
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
                    



    


