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
				[100, 100, 10, 10], 0)

# Draws the surface object to the screen.
pygame.display.update()


def move():
	


while True:
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_w:
				print("Move the character forwards")
			elif event.key == pygame.K_s:
				print("Move the character backwards")
			elif event.key == pygame.K_a:
				print("Move the character left")
			elif event.key == pygame.K_d:
				print("Move the character right")


