from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLineEdit, QHBoxLayout

class VirtualKeyboard(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        vbox = QVBoxLayout()

        self.line_edit = QLineEdit()
        vbox.addWidget(self.line_edit)

        hbox = QHBoxLayout()
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        for btn_text in buttons:
            btn = QPushButton(btn_text)
            btn.clicked.connect(lambda ch=btn_text: self.on_keyboard_button_clicked(btn_text))
            hbox.addWidget(btn)

        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def on_keyboard_button_clicked(self, char):
        # if char == '=':
        #     try:
        #         result = eval(self.line_edit.text())
        #         self.line_edit.setText(str(result))
        #     except:
        #         self.line_edit.setText("Error")
        # else:
        #     self.line_edit.insert(char)
        print(char)