# Main_ShapesExample.py

# Import packages
import pygame
import sys
import random
from pygame.locals import *
from pygwidgets import *
from Circle import Circle
from Triangle import Triangle
from Square import Square  


# Define constants
N_SHAPES = 10
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Initialize the pygame environment
pygame.init()
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Shapes Example')

# Initialize variables
shapesList = []
shapeClassesTuple = (Circle, Triangle, Square)

for _ in range(N_SHAPES):
    shapeClass = random.choice(shapeClassesTuple)
    shape = shapeClass(window, WINDOW_WIDTH, WINDOW_HEIGHT)
    shapesList.append(shape)


oStatusLine = DisplayText(window, (50, 10), "Click on shapes", fontSize=30)

# Main game loop
while True:
    # Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            mouseX, mouseY = pygame.mouse.get_pos()
            for shape in shapesList:
                if shape.clickedInside(mouseX, mouseY):
                    shapeType = shape.getType()
                    area = shape.getArea()
                    message = f"Clicked on {shapeType}, Area: {area}"
                    oStatusLine.setValue(message)
                    break

    # Clear the window before drawing again
    window.fill((255, 255, 255))

    # Draw all window elements
    for shape in shapesList:
        shape.draw()

    # Draw the status line
    oStatusLine.draw()

    # Update the window
    pygame.display.update()

    # Slow things down a bit
    pygame.time.delay(30)


