from PyQt5.QtCore import Qt, QStringListModel, QSortFilterProxyModel
from PyQt5.QtWidgets import QApplication, QMainWindow, QLineEdit, QVBoxLayout, QWidget, QCompleter

class LowercaseFilterProxyModel(QSortFilterProxyModel):
    def filterAcceptsRow(self, source_row, source_parent):
        source_model = self.sourceModel()
        source_index = source_model.index(source_row, 0, source_parent)
        item_data = source_model.data(source_index, Qt.DisplayRole)
        filter_str = self.filterRegExp().pattern()
        return filter_str.lower() in item_data.lower()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        central_widget = QWidget()
        layout = QVBoxLayout()
        self.item_edit = QLineEdit()

        self.names = ["Apple", "Banana", "Cherry", "Grape", "Lemon"]
        model = QStringListModel(self.names)

        completer = QCompleter()
        completer.setModel(LowercaseFilterProxyModel(completer))
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        completer.setModelSorting(QCompleter.CaseInsensitivelySortedModel)
        completer.setModel(model)

        self.item_edit.setCompleter(completer)

        layout.addWidget(self.item_edit)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
