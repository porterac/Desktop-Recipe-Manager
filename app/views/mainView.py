from PyQt6.QtWidgets import QMainWindow, QPushButton
from services.getRecipies import getRecipe

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe Manager App")
        self.button = QPushButton("Recipies")
        self.button.setCheckable(True)
