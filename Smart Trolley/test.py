import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QListView
from PyQt5.QtCore import Qt, QAbstractListModel, QSortFilterProxyModel
import json
import requests


class JSONListModel(QAbstractListModel):
    def __init__(self, data=None):
        super().__init__()
        self.data = data or []

    def rowCount(self, parent=None):
        return len(self.data)

    def data(self, index, role):
        if role == Qt.DisplayRole:
            return self.data[index.row()]

        return None


class SearchBar(QWidget):
    def __init__(self, json_data):
        super().__init__()
        self.json_data = json_data

        self.model = JSONListModel(json_data)
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()

        self.search_input = QLineEdit()
        self.search_input.textChanged.connect(self.filter_data)

        self.list_view = QListView()
        self.list_view.setModel(self.proxy_model)

        layout.addWidget(self.search_input)
        layout.addWidget(self.list_view)

        self.setLayout(layout)

    def filter_data(self, keyword):
        self.proxy_model.setFilterRegExp(keyword)
        self.list_view.setCurrentIndex(self.proxy_model.index(0, 0))
        self.list_view.scrollTo(self.proxy_model.index(0, 0))


def main():
    url = "https://smtrolley.onrender.com/inventory/get-all"
    response = requests.get(url)
    json_data = response.json()
    print(json_data['products'][0])

    # Create the Qt application
    app = QApplication(sys.argv)

    # Create and show the search bar widget
    search_bar = SearchBar(json_data['products'])
    search_bar.show()

    # Execute the Qt application
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
