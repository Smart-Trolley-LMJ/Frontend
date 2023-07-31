from Custom_Widgets.Widgets import QDialog, QVBoxLayout, QLabel, QPushButton
from UI.Images.ui_interface import Ui_MainWindow

class Success(QDialog):
    def __init__(self, main_ui: Ui_MainWindow, new_userID):
        super().__init__()
        self.main_ui :Ui_MainWindow = main_ui
        self.new_userID = new_userID
        self.setModal(True)
        
        self.setWindowTitle("Payment Complete")


        self.layout = QVBoxLayout()
        message = QLabel("Thank you for shopping with us")
        done_button = QPushButton("Done")
        done_button.clicked.connect(self.end_shopping)
        
        self.layout.addWidget(message)
        self.layout.addWidget(done_button)
        self.setLayout(self.layout)

    def end_shopping(self):
        # self.main_ui.shoppingTable.clearContents() #clear contents of budget table
        self.main_ui.displayCost.setText('0.00')
        while self.main_ui.shoppingTable.rowCount() > 0:
            self.main_ui.shoppingTable.removeRow(0)
        # self.main_ui.itemTable_2.clearContents() #clear contents of cart table
        while self.main_ui.itemTable_2.rowCount() > 0:
            self.main_ui.itemTable_2.removeRow(0)
        # self.main_ui.mainPages.setCurrentWidget(0)
        self.new_userID()
        self.close()
        
