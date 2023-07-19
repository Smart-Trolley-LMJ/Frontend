import os
from Custom_Widgets.Widgets import QWidget, QGridLayout, QDialog, QLabel
from UI.Images.checkout import Ui_Dialog
from UI.Images.receiptItem import Ui_Form
import requests
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
        self.url = "https://smtrolley.onrender.com/cart/checkout/"
        # self.ui.foodScrollArea.setLayout(self.grid)
        self.ui.setupUi(self)
        self.grid = QGridLayout()
        self.ui.checkoutScrollAreaWidget.setLayout(self.grid)
        self.display_grid(self.data)
        self.ui.cancelPaymentBtn.clicked.connect(self.close)
        self.ui.proceedBtn.clicked.connect(self.issue_payment)
        self.receipt=[]

    
        


    def display_grid(self, filtered_data):
        row = 0
        column = 0
        self.receipt = []

        # Clear the layout
        for i in reversed(range(self.grid.count())):
            item = self.grid.itemAt(i)
            widget = item.widget()
            if widget:
                self.grid.removeWidget(widget)
                widget.setParent(None)
            # Iterate over the JSON data and create duplicated item card frames
        for item_data in filtered_data:
            item_card = ItemCard(item_data)
            self.grid.addWidget(item_card, row, column)
            column += 1

            if column == 3:
                column = 0
                row += 1
            row += 1
        
    def issue_payment(self):
        response = requests.post(f'{self.url}{self.user_id}',json=self.receipt).content
        print(response)

        