# Importing pygame module
import pygame
from time import sleep
from pygame.locals import *

# initiate pygame and give permission
# to use pygame's functionality.
pygame.init()

# create the display surface object
# of specific dimension.
window = pygame.display.set_mode((600, 600))

# Fill the scree with white color
window.fill((255, 255, 255))

# Using draw.rect module of
# pygame to draw the solid rectangle
pygame.draw.rect(window, (66, 115, 18),
				[100, 100, 100, 100], 0)

# Draws the surface object to the screen.
pygame.display.update()
sleep(4444)

