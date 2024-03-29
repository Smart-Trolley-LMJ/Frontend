
from os import getcwd
from UI.Images.ui_interface import Ui_MainWindow
from Custom_Widgets.Widgets import *
from virtual_keyboard import VirtualKeyboard
from virtual_numpad import VirtualNumpad
from Model.items import Product
import math

CURRENT_WORKING_DIRECTORY = getcwd()


class Budget(QWidget):
    def __init__(self,data: Product,ui: Ui_MainWindow):
        super().__init__()
        self.ui = ui
        self.data = data
        print(data)
        # Create autocomplete options
        self.names = set([product['name'].lower() for product in data ])
        completer = QCompleter(self.names)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        self.ui.item_edit.setCompleter(completer)


        # Add item to list
        self.ui.addToListBtn.clicked.connect(self.add_item)
        self.ui.deleteFromListBtn.clicked.connect(self.delete_row)

        #Pop Up Keyboard
        self.keyboard = VirtualKeyboard()
        self.ui.item_edit.installEventFilter(self)

        self.numpad = VirtualNumpad()
        self.ui.quantity_edit.installEventFilter(self)
    
    def eventFilter(self, obj, event):
        if event.type() == 2:
            if obj == self.ui.item_edit:
                self.keyboard.line_edit = obj
                self.keyboard.show()
            elif obj == self.ui.quantity_edit:
                self.numpad.line_edit = obj
                self.numpad.show()
            return True
        return super().eventFilter(obj, event)

    def add_item(self):

        row_count = self.ui.shoppingTable.rowCount()
        name = self.ui.item_edit.displayText()
        quantity = self.ui.quantity_edit.displayText()

        if name == '' and quantity == '':
            QMessageBox.warning(self, 'Error', 'Please enter an item and quantity')
            return
        try:
            quantity = int(quantity)
            if math.isnan(quantity) :
                self.ui.item_edit.setText("")
                self.ui.quantity_edit.setText("")
                QMessageBox.warning(self, 'Error', 'Please enter a valid quantity')
                return
        except:
            self.ui.quantity_edit.setText("")
            QMessageBox.warning(self, 'Error', 'Please enter a valid quantity')
            return
        # Validate item existence
        
        selected_item = next((item for item in self.data if name == item['name'].lower()), None)
        print(selected_item)
        if selected_item is None:
            self.ui.item_edit.setText("")
            self.ui.quantity_edit.setText("")
            QMessageBox.warning(self, 'Error', 'Item not found in the shop.')
            return
        

        quantity = int(quantity)
        unit_cost = selected_item["price"]
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
                self.ui.item_edit.setText("")
                self.ui.quantity_edit.setText("")

                self.calculate_total()
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
        self.calculate_total()


    def delete_row(self):
        row = self.ui.shoppingTable.currentRow()
        self.ui.shoppingTable.removeRow(row)
        self.calculate_total()

    def reset_table(self):
        # Clear all data from the table
        self.ui.shoppingTable.clearContents()
        self.ui.shoppingTable.setRowCount(0)
        self.ui.shoppingTable.setColumnCount(0)
    

    def calculate_total(self):
        total_cost = 0
        for row in range(self.ui.shoppingTable.rowCount()):
            cost_item = self.ui.shoppingTable.item(row, 3)
            if cost_item is not None:
                cost_str = cost_item.text()
                try:
                    cost_value = float(cost_str)
                    total_cost += cost_value
                except ValueError:
                    pass

        self.ui.budgetCostLabel.setText(f"GHC{total_cost:.2f}")
        



