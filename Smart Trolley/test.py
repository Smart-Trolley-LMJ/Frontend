import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()

        label = QLabel("Original Label")
        self.layout.addWidget(label)

        clear_button = QPushButton("Clear Layout")
        clear_button.clicked.connect(self.clear_layout)
        self.layout.addWidget(clear_button)

        self.setLayout(self.layout)

    def clear_layout(self):
        for i in reversed(range(self.layout.count())):
            item = self.layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout_recursive(item.layout())
            self.layout.removeItem(item)

    def clear_layout_recursive(self, layout):
        for i in reversed(range(layout.count())):
            item = layout.itemAt(i)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                self.clear_layout_recursive(item.layout())
            layout.removeItem(item)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MyWidget()
    window.show()

    sys.exit(app.exec_())
