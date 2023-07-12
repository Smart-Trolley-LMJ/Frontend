
from threading import Thread

from PyQt5.QtCore import pyqtSignal, QObject


class Worker(QObject):
    rfidDetected = pyqtSignal(str)

    def start(self, fn):
        Thread(target=self._execute, args=(fn,), daemon=True).start()

    def _execute(self, fn):
        fn(self)

    def add_or_remove_item(self, item):
        self.rfidDetected.emit(item)