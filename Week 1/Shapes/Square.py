import pygame
import random

class Square:
    def __init__(self, window, max_width, max_height):
        self.window = window
        self.width = random.randint(10, 100)
        self.height = self.width
        self.left = random.randint(1, max_width - self.width)
        self.top = random.randint(25, max_height - self.height)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.shapeType = "Square"

    def clickedInside(self, mouseX, mouseY):
        return self.left <= mouseX <= self.left + self.width and self.top <= mouseY <= self.top + self.height

    def getType(self):
        return self.shapeType

    def getArea(self):
        return self.width * self.height

    def draw(self):
        pygame.draw.rect(self.window, self.color, (self.left, self.top, self.width, self.height))
