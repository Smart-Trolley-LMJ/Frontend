import os
from Custom_Widgets.Widgets import QWidget, QGridLayout, QLabel, QPixmap
from UI.Images.ui_interface import Ui_MainWindow

CURRENT_WORKING_DIRECTORY = os.getcwd()

class foodPage(QWidget):
    def __init__(self, json_data, ui):
        super(QWidget, self).__init__()
        self.ui : Ui_MainWindow = ui
        self.data = json_data

        self.grid = QGridLayout()
        self.ui.foodScrollArea.setLayout(self.grid)
        # self.ui.scrollAreaWidgetContents_4.setLayout(self.grid)
        self.display_grid(self.data)
        self.ui.searchBar.textChanged.connect(self.filter_data)


    def display_grid(self, filtered_data):
        row = 0
        column = 0

        # Clear the layout
        for i in reversed(range(self.grid.count())):
            item = self.grid.itemAt(i)
            widget = item.widget()
            if widget:
                self.grid.removeWidget(widget)
                widget.setParent(None)


        for item in filtered_data:
            # Get image path and label text from JSON
            image_path = f'{CURRENT_WORKING_DIRECTORY}/UI/Images/food and drinks/{item["image_path"]}'
            label_text = item['label']

            # Create QPixmap from image path
            pixmap = QPixmap(image_path)

            # Create QLabel for the image
            image_label = QLabel()
            image_label.setPixmap(pixmap)
            self.grid.addWidget(image_label, row, column)

            # Create QLabel for the text
            text_label = QLabel(label_text)
            self.grid.addWidget(text_label, row+1, column)

            column += 1

            # If the current row is filled, move to the next row and reset column to 0
            if column == 3:
                column = 0
                row += 2

    def filter_data(self):
        search_text = self.ui.searchBar.toPlainText().lower()
        filtered_data = [item for item in self.data if search_text in item["label"].lower()]
        # print(filtered_data)
        self.display_grid(filtered_data)
        