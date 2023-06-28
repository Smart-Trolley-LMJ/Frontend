import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QTimer
from mfrc522 import SimpleMFRC522

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.reader = SimpleMFRC522()

    def initUI(self):
        self.setWindowTitle("Automatic Item Scanning")
        self.setGeometry(100, 100, 400, 300)

        self.table = QTableWidget(self)
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Item ID", "Item Name"])

    def readRFID(self):
        id, text = self.reader.read()
        self.addItemToTable(id, text)

    def addItemToTable(self, item_id, item_name):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)

        id_item = QTableWidgetItem(str(item_id))
        name_item = QTableWidgetItem(item_name)

        self.table.setItem(row_count, 0, id_item)
        self.table.setItem(row_count, 1, name_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec_())
