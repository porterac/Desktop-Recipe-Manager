import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt6.QtCore import QSize, Qt
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.button_is_checked =  True
        self.setWindowTitle("Practice App")

        self.button = QPushButton("Press Me")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.the_button_was_pushed)
            # The clicked method is what generates the signal that 
            # gets passed into the 'the_button_was_pushed' slot
            # the connect method is how you connect a signal to a slot
        self.button.clicked.connect(self.the_button_was_toggled)
        self.button.setChecked(self.button_is_checked)

        self.setFixedSize(QSize(400,300))
        self.setCentralWidget(self.button)

    def the_button_was_pushed(self,checked):
        if not checked:
            self.button_is_checked = checked
            self.button.setText("Made you Push me!")
        #self.button.setEnabled(False)
        else:
            self.button_is_checked = checked
            self.button.setText("Push ME!")
        print("Button Pushed")
    
    def the_button_was_toggled(self, checked):
        self.button_is_checked = checked
        print(self.button_is_checked)
        # in this case we need to have checked as a variable because
        # we have set checkable eqaul to true and this specific widget
        # (the clicked widget) returns the state of the button. So checked
        # tells us the state of the button

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
