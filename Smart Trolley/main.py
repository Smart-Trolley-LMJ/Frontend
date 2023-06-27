import sys
import os
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from inventories import Inventories
from budget import Budget
from cart import ShoppingCart
from Custom_Widgets.Widgets import *
from PyQt5.QtCore import QTimer

CURRENT_WORKING_DIRECTORY = os.getcwd()


class my_app(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        
        self.ui.setupUi(self)
    
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.PopupNotificationContainer.collapseMenu())
        self.ui.cancelBtn_2.clicked.connect(lambda: self.ui.PaymentContainer.collapseMenu()) 

        with open(f'{CURRENT_WORKING_DIRECTORY}/json/image.json') as json_file:
            self.data = json.load(json_file)
        self.inventories = Inventories(self.data, self.ui)
        self.cart = ShoppingCart(self.ui)
        self.budget = Budget(self.ui)
        
        loadJsonStyle(self, self.ui, jsonFiles = {
        f'{CURRENT_WORKING_DIRECTORY}/json/mainWindow.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/leftSlideMenu.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/centerMenu.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/notificationMenu.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/mainPages.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/centerMenuPages.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/buttonGroups.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/homePage.json',
        # f'{CURRENT_WORKING_DIRECTORY}/json/rightMenu.json',
        })

        self.show()

        QAppSettings.updateAppSettings(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ########################################################################
    ## 
    ########################################################################
    window = my_app()
    window.show()

    timer = QTimer()
    timer.timeout.connect(window.cart.readRFID)
    timer.start(1000)  # Scan every 1 second


    sys.exit(app.exec_())
