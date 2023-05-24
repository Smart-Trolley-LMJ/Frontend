import sys
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PyQt5.QtGui import QPixmap
import json

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Load JSON data from a file
        with open('data.json') as json_file:
            data = json.load(json_file)

        grid = QGridLayout()
        self.setLayout(grid)

        row = 0
        column = 0

        for item in data:
            # Get image path and label text from JSON
            image_path = item['image_path']
            label_text = item['label']

            # Create QLabel for the image
            image_label = QLabel(self)
            pixmap = QPixmap(image_path)
            image_label.setPixmap(pixmap)
            grid.addWidget(image_label, row, column)

            # Create QLabel for the text
            text_label = QLabel(label_text, self)
            grid.addWidget(text_label, row+1, column)

            column += 1

            # If the current row is filled, move to the next row and reset column to 0
            if column == 3:
                column = 0
                row += 2

        self.setWindowTitle('Image Grid')
        self.setGeometry(200, 200, 600, 400)
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = MyWidget()
    sys.exit(app.exec_())
