import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QListWidget

class ShoppingListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Shopping List")
        self.layout = QVBoxLayout()

        self.item_layout = QHBoxLayout()
        self.item_label = QLabel("Item:")
        self.item_input = QLineEdit()
        self.add_button = QPushButton("Add")
        self.add_button.clicked.connect(self.add_item)

        self.item_layout.addWidget(self.item_label)
        self.item_layout.addWidget(self.item_input)
        self.item_layout.addWidget(self.add_button)

        self.shopping_list = QListWidget()

        self.layout.addLayout(self.item_layout)
        self.layout.addWidget(self.shopping_list)

        self.setLayout(self.layout)

    def add_item(self):
        item = self.item_input.text()
        if item:
            self.shopping_list.addItem(item)
            self.item_input.clear()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    shopping_list_app = ShoppingListApp()
    shopping_list_app.show()
    sys.exit(app.exec_())
