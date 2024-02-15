import sys
from PyQt6.QtWidgets import QApplication, QLabel, QMessageBox

app= QApplication(sys.argv)
# label=QLabel("<font color=Blue size=20>Hello World</font>")
label= QMessageBox.information(None,'Information', 'Hello World')
label.show()
app.exec()