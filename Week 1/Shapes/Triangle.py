# Triangle.py

# Importing packages
import pygame
import random

# Defining the colors RED, GREEN, and BLUE
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

class Triangle:
    def __init__(self, window, maxWidth, maxHeight):
        # Initializing the triangle object
        self.window = window
        self.color = random.choice([RED, GREEN, BLUE])
        self.width = random.randint(10, 100)
        self.height = random.randint(10, 100)
        self.left = random.randint(1, maxWidth - 100)
        self.top = random.randint(25, maxHeight - 100)
        self.shapeType = "Triangle"

    def clickedInside(self, mouseX, mouseY):
        # Calculate barycentric coordinates to determine if the point is inside the triangle
        detT = (self.top - self.top - self.height) * (self.left + self.width - self.left) - (self.left - self.left) * (self.top + self.height - self.top)
        alpha = ((mouseY - self.top - self.height) * (self.left + self.width - self.left) - (mouseX - self.left) * (self.top + self.height - self.top)) / detT
        beta = ((mouseY - self.top) * (self.left - self.left) - (mouseX - self.left - self.width) * (self.top - self.top)) / detT
        gamma = 1 - alpha - beta

        # Check if the barycentric coordinates are within the range [0, 1]
        return 0 <= alpha <= 1 and 0 <= beta <= 1 and 0 <= gamma <= 1


        # Calculate offset from the upper left corner of the triangle
        xOffset = mouseX - self.left
        yOffset = mouseY - self.top

        # Calculate slope from the Y-intercept
        triangleSlope = self.height / self.width
        pointSlope = yOffset / xOffset

        return pointSlope <= triangleSlope

    def getType(self):
        # Defining a method which returns the information that the item clicked is a triangle
        return self.shapeType

    def getArea(self):
        # Defining a method which calculates the area of the triangle
        return 0.5 * self.width * self.height

    def draw(self):
        # Defining a method to draw the triangle in a randomly chosen color
        points = [(self.left, self.top + self.height),
                  (self.left + self.width, self.top + self.height),
                  (self.left + self.width // 2, self.top)]
        pygame.draw.polygon(self.window, self.color, points)
