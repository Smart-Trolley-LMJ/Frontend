import sys
from UI.Images.ui_interface import Ui_MainWindow
from inventories import Inventories
from budget import Budget
from cart import ShoppingCart
from Model.items import StoreItems
from Custom_Widgets.Widgets import QMainWindow, QApplication, QAppSettings, loadJsonStyle
import os
from dotenv import load_dotenv
load_dotenv()

CURRENT_WORKING_DIRECTORY = os.getcwd()


class my_app(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        # self.url = "https://smtrolley.onrender.com/users/"
        ip_address = os.environ.get("URL")
        self.url = f"{ip_address}/users"
        print(f'Main:  {self.url}')
    

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.PopupNotificationContainer.collapseMenu())
        self.ui.cancelBtn_2.clicked.connect(lambda: self.ui.PaymentContainer.collapseMenu()) 

        self.items = StoreItems()
        self.data = self.items.response_json
        self.inventories = Inventories(self.data, self.ui)
        self.cart = ShoppingCart(self.ui)
        self.budget = Budget(self.data, self.ui)
        # self.ui.mainPages.setCurrentWidget(self.ui.cartPage)
        
        loadJsonStyle(self, self.ui, jsonFiles = {
        f'{CURRENT_WORKING_DIRECTORY}/json/mainWindow.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/leftSlideMenu.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/centerMenu.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/notificationMenu.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/mainPages.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/centerMenuPages.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/buttonGroups.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/homePage.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/inventories.json',
        f'{CURRENT_WORKING_DIRECTORY}/json/inventoryMenuPages.json',
        # f'{CURRENT_WORKING_DIRECTORY}/json/rightMenu.json',
        })

        self.show()

        QAppSettings.updateAppSettings(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = my_app()

    window.show()

    sys.exit(app.exec_())
