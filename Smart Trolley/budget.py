
from os import getcwd
from UI.Images.ui_interface import Ui_MainWindow
from Custom_Widgets.Widgets import *
from Model.items import Product

CURRENT_WORKING_DIRECTORY = getcwd()


class Budget():
    def __init__(self,data: Product,ui: Ui_MainWindow):
        self.ui = ui
        self.data = data

        # Create autocomplete options
        self.names = set([product['name'] for product in data ])
        completer = QCompleter(self.names)
        self.ui.item_edit.setCompleter(completer)

        # Add item to list
        self.ui.addToListBtn.clicked.connect(self.add_item)
        

    def add_item(self, name):
        row_count = self.ui.shoppingTable.rowCount()
        name = self.ui.item_edit.displayText()
        quantity = int(self.ui.quantity_edit.displayText())
        unit_cost = [product['price'] for product in self.data if product['name'] == name][0]
        cost = quantity * float(unit_cost)

        # Check if the item already exists in the table
        for row in range(row_count):
            item_name = self.ui.shoppingTable.item(row, 0).text()
            if item_name == name:
                # Item already exists, increment quantity and recalculate cost
                current_quantity = int(self.ui.shoppingTable.item(row, 1).text())
                new_quantity = current_quantity + quantity
                self.ui.shoppingTable.setItem(row, 1, QTableWidgetItem(str(new_quantity)))

                # current_cost = int(self.ui.shoppingTable.item(row, 4).text())
                new_cost = new_quantity * unit_cost
                self.ui.shoppingTable.setItem(row, 2, QTableWidgetItem(str(new_cost)))
                return

        # Item does not exist, add a new row to the table
        self.ui.shoppingTable.setRowCount((row_count + 1))
        self.ui.shoppingTable.setItem(row_count, 0, QTableWidgetItem(name))
        self.ui.shoppingTable.setItem(row_count, 1, QTableWidgetItem(str(quantity)))
        self.ui.shoppingTable.setItem(row_count, 2, QTableWidgetItem(str(unit_cost)))
        self.ui.shoppingTable.setItem(row_count, 3, QTableWidgetItem(str(cost)))

        # Clear text boxes
        self.ui.item_edit.setText("")
        self.ui.quantity_edit.setText("")


