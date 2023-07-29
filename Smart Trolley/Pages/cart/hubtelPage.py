
from PyQt5.QtWebEngineWidgets import QWebEngineView
from Custom_Widgets.Widgets import QUrl, QApplication,QDialog, QVBoxLayout, QWidget, QDesktopWidget, QTimer
import requests
import json


class WebPageViewer(QDialog):
    def __init__(self, hubtel_url: str, id:str):
        super().__init__()
        self.url = hubtel_url
        self.order_id = id
        self.initUI()
        self.time = QTimer(self)
        self.time.start(120000)
        self.time.timeout.connect(self.close)

    def initUI(self):
        self.setWindowTitle("Web Page Viewer")
        x,y = 0, 0
        self.setGeometry(0, 0, 800, 600)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # Create the QWebEngineView widget
        self.web_view = QWebEngineView(self)
        layout.addWidget(self.web_view)

        # Load the initial web page 
        self.web_view.setUrl(QUrl(self.url))

        # self.web_view.loadFinished.connect(self.check_payment_completed)

    def showEvent(self, event):
        # This event is triggered just before the dialog is shown
        # We will center the dialog here
        self.center_on_screen()

    def center_on_screen(self):
        # Get the geometry of the screen
        screen_geometry = QDesktopWidget().screenGeometry()

        # Calculate the position to center the dialog
        x = (screen_geometry.width() - self.width()) // 2
        y = (screen_geometry.height() - self.height()) // 2

        # Move the dialog to the center position
        self.move(x, y)

