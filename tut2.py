import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        label = QLabel('Enter text:')
        input_field = QLineEdit()

        layout.addWidget(label)
        layout.addWidget(input_field)

        self.setLayout(layout)

        self.setWindowTitle('PyQt6 Input Field Example')
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
