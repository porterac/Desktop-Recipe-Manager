from PyQt6.QtWidgets import QMainWindow, QPushButton
from PyQt6.QtCore import QSize
from services.getRecipies import getRecipe

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe Manager App")
        self.recipe_button = QPushButton("Recipies")
        self.recipe_button.setCheckable(True)
        #self.button.clicked.connect(getRecipe.fetchAllRecipes())
        self.setFixedSize(QSize(400,300))
        self.recipe_button.setFixedSize(QSize(200,100))
        self.setCentralWidget(self.recipe_button)
