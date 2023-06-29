import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import QThread, pyqtSignal
import MFRC522

class RFIDReaderThread(QThread):
    tag_detected = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.reader = MFRC522.MFRC522()

    def run(self):
        while True:
            (status, tag_data) = self.reader.MFRC522_Request(self.reader.PICC_REQIDL)
            if status == self.reader.MI_OK:
                (status, uid) = self.reader.MFRC522_SelectTagSN()
                if status == self.reader.MI_OK:
                    uid_str = ''.join(str(x) for x in uid)
                    self.tag_detected.emit(uid_str)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("RFID Table Example")
        self.table = QTableWidget()
        self.table.setColumnCount(1)
        self.table.setHorizontalHeaderLabels(["RFID Tag"])
        self.setCentralWidget(self.table)

        self.rfid_reader_thread = RFIDReaderThread()
        self.rfid_reader_thread.tag_detected.connect(self.add_row)
        self.rfid_reader_thread.start()

    def add_row(self, uid):
        row_count = self.table.rowCount()
        self.table.setRowCount(row_count + 1)
        tag_item = QTableWidgetItem(uid)
        self.table.setItem(row_count, 0, tag_item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
