# Circle.py

# Importing packages
import pygame
import random
import math

# Defining the colors RED, GREEN, and BLUE
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Circle:
    def __init__(self, window, maxWidth, maxHeight):
        # Initializing the circle object
        self.window = window
        self.color = random.choice([RED, GREEN, BLUE])
        self.radius = random.randint(10, 50)
        self.center = (random.randint(1, maxWidth - 100), random.randint(25, maxHeight - 100))
        self.shapeType = "Circle"

    def clickedInside(self, mouseX, mouseY):
        # Defining a method to check if the location clicked is inside the circle
        distance = math.sqrt((mouseX - self.center[0])**2 + (mouseY - self.center[1])**2)
        return distance <= self.radius

    def getType(self):
        # Defining a method which returns the information that the item clicked is a circle
        return self.shapeType

    def getArea(self):
        # Defining a method which calculates the area of the circle
        return math.pi * self.radius ** 2

    def draw(self):
        # Defining a method to draw the circle in a randomly chosen color
        pygame.draw.circle(self.window, self.color, self.center, self.radius)
