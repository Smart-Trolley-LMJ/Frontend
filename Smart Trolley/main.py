import sys
import os
from UI.Images.ui_interface import Ui_MainWindow
# IMPORT Custom widgets
from Custom_Widgets.Widgets import *


class my_app(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Expand Center Menu Widget
        self.ui.settingsBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.infoBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())
        self.ui.helpBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.expandMenu())

        # Collapse Center Menu Widget
        self.ui.closeCenterMenuBtn.clicked.connect(lambda: self.ui.CenterMenuContainer.collapseMenu())

        # Expand Right Menu Widget
        self.ui.moreMenuBtn.clicked.connect(lambda: self.ui.RightMenuContainer.expandMenu())
        self.ui.profileMenuBtn.clicked.connect(lambda: self.ui.RightMenuContainer.expandMenu())
        # Collapse Right Menu Widget
        self.ui.closeRightMenuBtn.clicked.connect(lambda: self.ui.RightMenuContainer.collapseMenu())

        # # Expand Notification Menu Widget
        # self.ui.notificationBtn.clicked.connect(lambda: self.ui.PopupNotificationContainer.expandMenu())

        # Collapse Right Menu Widget
        self.ui.closeNotificationBtn.clicked.connect(lambda: self.ui.PopupNotificationContainer.collapseMenu())
        

        
        loadJsonStyle(self, self.ui, jsonFiles = {
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\mainWindow.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\leftSlideMenu.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\centerMenu.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\rightMenu.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\notificationMenu.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\mainPages.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\centerMenuPages.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\rightMenuPages.json',
        'C:\\Users\\dlsar\\Documents\\GitHub\\Frontend\\Smart Trolley\\json\\buttonGroups.json',
        })




        

def create_app():
    app = QApplication(sys.argv)
    win = my_app()
    win.show()
    
     
    sys.exit(app.exec_())

create_app() 