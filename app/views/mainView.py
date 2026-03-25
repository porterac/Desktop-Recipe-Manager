from PyQt6.QtWidgets import QMainWindow, QPushButton, QGridLayout, QWidget
from PyQt6.QtCore import QSize
from services import getRecipe

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Recipe Manager App")

        # Buttons
        self.recipe_button = QPushButton("Recipies")
        self.random_recipe_button = QPushButton("Get Random Recipe")

        # Grid-layout
        button_grid = QGridLayout()

        # Add buttons to layout
        button_grid.addWidget(self.recipe_button,0,0)
        button_grid.addWidget(self.random_recipe_button,0,1)

        # Button Add-ons
        self.recipe_button.setCheckable(True)
        self.random_recipe_button.setCheckable(True)
        self.recipe_button.clicked.connect(getRecipe.fetchRequestedRecipe)
        self.random_recipe_button.clicked.connect(getRecipe.getRandomRecipe)

        # Create Central Widget
        container = QWidget()
        container.setLayout(button_grid)
        self.setCentralWidget(container)

    def initWidgets():
        return
    
    def initLayout():
        return
    
    def initConnections():
        return
