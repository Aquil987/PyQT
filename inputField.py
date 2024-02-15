# import sys
# from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton

# class MyWindow(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.setGeometry(200,200,100,200)

#         self.init_ui()

#     def init_ui(self):
#         layout = QVBoxLayout()

#         label = QLabel('Enter text:')
#         label.move(50,50)
#         self.input_field = QLineEdit()
#         submit_button = QPushButton('Submit')

#         submit_button.clicked.connect(self.submit_clicked)  # Connect the button click event to a function

#         layout.addWidget(label)
#         layout.addWidget(self.input_field)
#         layout.addWidget(submit_button)

#         self.setLayout(layout)

#         self.setWindowTitle('PyQt6 Input Field Example')
#         # self.show()

#     def submit_clicked(self):
#         # This function will be called when the submit button is clicked
#         input_value = self.input_field.text()
#         print(f"Submitted Value: {input_value}")

# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     window = MyWindow()
#     window.show()
#     sys.exit(app.exec())
import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QVBoxLayout, QPushButton, QFrame

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(200,200,175,200)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        frame = QFrame()  # Create a frame to wrap the label and input field
        frame_layout = QVBoxLayout(frame)

        label = QLabel('Enter text:')
        self.input_field = QLineEdit()
        submit_button = QPushButton('Submit')

        submit_button.clicked.connect(self.submit_clicked)  # Connect the button click event to a function

        frame_layout.addWidget(label)
        frame_layout.addWidget(self.input_field)

        layout.addWidget(frame)  # Add the frame to the main layout
        layout.addWidget(submit_button)

        self.setLayout(layout)

        self.setWindowTitle('PyQt6 Input Field Example')
        self.show()

    def submit_clicked(self):
        # This function will be called when the submit button is clicked
        input_value = self.input_field.text()
        print(f"Submitted Value: {input_value}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    sys.exit(app.exec())
