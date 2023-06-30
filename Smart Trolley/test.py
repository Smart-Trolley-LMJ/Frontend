import sys
import json
from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QWidget
from PyQt5.QtGui import QPixmap
from UI.Images.item_card import Ui_ItemCard  # Import the generated Python code for the item card UI


class ItemCard(QWidget):
    def __init__(self, data):
        super().__init__()
        self.ui = Ui_ItemCard()
        self.ui.setupUi(self)
        self.populate_data(data)

    def populate_data(self, data):
        # Set the data values to the widgets in the item card frame
        pixmap = QPixmap(data['image_path'])
        self.ui.label_68.setPixmap(pixmap)
        self.ui.label_69.setText(data['label'])


if __name__ == '__main__':
    app = QApplication(sys.argv)

    # Load JSON data
    with open('image.json') as f:
        json_data = json.load(f)

    main_window = QMainWindow()
    main_widget = QWidget()
    main_layout = QGridLayout()

    row = 0
    col = 0

    # Iterate over the JSON data and create duplicated item card frames
    for item_data in json_data:
        item_card = ItemCard(item_data)
        main_layout.addWidget(item_card, row, col)
        col += 1

        if col == 3:
            col = 0
            row += 1

    main_widget.setLayout(main_layout)
    main_window.setCentralWidget(main_widget)
    main_window.show()

    sys.exit(app.exec_())
