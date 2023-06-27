
from os import getcwd
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *
# from mfrc522 import SimpleMFRC522

CURRENT_WORKING_DIRECTORY = getcwd()
products = [{
    "image_path": "nutrisnax.jfif",
    "label": "nutrisnax",
    "category": "food and drinks",
    "location": "Aisle ",
    "cost": "10.00"
},
{
    "image_path": "coca cola.jfif",
    "label": "Coke",
    "category": "food and drinks",
    "location": "Aisle ",
    "cost": "10.00"
}]

class DialogBox(QDialog):
    def __init__(self):
        super().__init__()
        self.setModal(True)

        self.setWindowTitle("Proceed to Payment")

        QBtn = QDialogButtonBox.Yes | QDialogButtonBox.No

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        message = QLabel("Do you want to proceed to payment?")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


class ShoppingCart():
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        # Add item to cart
        self.ui.addItemBtn.clicked.connect(lambda: self.add_item('Bread'))
        self.ui.checkoutBtn.clicked.connect(self.checkout)
        try:
            self.reader = SimpleMFRC522()
        except:
            pass

    def readRFID(self):
        try:
            id, text = self.reader.read()
            self.add_item("Waakye")
        except: pass 
        

    def add_item(self, name):
        row_count = self.ui.itemTable_2.rowCount()
        quantity = 2
        unit_cost = 5
        cost = quantity * unit_cost

        # Check if the item already exists in the table
        for row in range(row_count):
            item_name = self.ui.itemTable_2.item(row, 0).text()
            if item_name == name:
                # Item already exists, increment quantity and recalculate cost
                current_quantity = int(self.ui.itemTable_2.item(row, 1).text())
                new_quantity = current_quantity + quantity
                self.ui.itemTable_2.setItem(row, 1, QTableWidgetItem(str(new_quantity)))

                current_cost = int(self.ui.itemTable_2.item(row, 3).text())
                new_cost = new_quantity * unit_cost
                self.ui.itemTable_2.setItem(row, 3, QTableWidgetItem(str(new_cost)))

                self.calculate(cost)
                return

        # Item does not exist, add a new row to the table
        self.ui.itemTable_2.setRowCount(row_count + 1)
        self.ui.itemTable_2.setItem(row_count, 0, QTableWidgetItem(name))
        self.ui.itemTable_2.setItem(row_count, 1, QTableWidgetItem(str(quantity)))
        self.ui.itemTable_2.setItem(row_count, 2, QTableWidgetItem(str(unit_cost)))
        self.ui.itemTable_2.setItem(row_count, 3, QTableWidgetItem(str(cost)))

        self.calculate(cost)
    
    def calculate(self, cost):
        total_cost = float(self.ui.displayCost.toPlainText()) + float(cost)

        self.ui.displayCost.setText(f'{total_cost}')

    def checkout(self):
        self.ui.displayCost.setText(f'{0.00}')        
        dialog = DialogBox()
        dialog.exec_()

    


