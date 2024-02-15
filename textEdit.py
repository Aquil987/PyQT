import sys

from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        text_edit = QTextEdit()
        submit_button = QPushButton('Submit')

        submit_button.clicked.connect(lambda: self.submit_clicked(text_edit.toPlainText()))

        layout.addWidget(QLabel('Enter text:'))
        layout.addWidget(text_edit)
        layout.addWidget(submit_button)

        self.setLayout(layout)

        self.setWindowTitle('PyQt6 TextEdit Example')
        self.show()

    def submit_clicked(self, text):
        print(f"Submitted Text:\n{text}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
