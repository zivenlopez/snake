"""
This creates a basic 500x400 window
also tracks position of mouse and click state
"""

import pygame
pygame.init()

dis = pygame.display.set_mode((500,400))

pygame.display.update()
pygame.display.set_caption('Snake game by Ziven')

game_over = False

while not game_over:
    for event in pygame.event.get():
        print(event)     #prints out all the actions that take place on screen

        if event.type == pygame.QUIT:
            game_over=True

pygame.quit()
quit()