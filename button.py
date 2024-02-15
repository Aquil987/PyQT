import sys
from PyQt6.QtWidgets import QApplication, QPushButton

def say_hello(): # define the function
    print("Button Clicked")

# Create the Qt Application
app= QApplication(sys.argv)


# Create a button, connect it and show it
button= QPushButton('Button')
button.clicked.connect(say_hello)
button.show()
app.exec()
