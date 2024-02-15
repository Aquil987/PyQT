#*******Frame Container***********#

from PyQt6.QtWidgets import QLabel, QVBoxLayout, QPushButton, QWidget, QFrame, QApplication
import sys

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        frame = QFrame(self)
        layout = QVBoxLayout(self)

        label = QLabel("This is inside Frame.")
        btn = QPushButton("Click Me")

        layout.addWidget(label)
        layout.addWidget(btn)

        frame.setLayout(layout)

app = QApplication(sys.argv)
window = MyWindow()
window.show()
sys.exit(app.exec())