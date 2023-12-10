"""
Single square is drawn on screen
will be made into snake
"""

import pygame
pygame.init()
dis = pygame.display.set_mode((600,500))

pygame.display.set_caption('Snake game by Ziven')

blue = (0, 0, 255)
red = (255, 0, 0)

game_over = False

while not game_over:
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            game_over = True

    pygame.draw.rect(dis, blue, [200,150,10,10])
    pygame.display.update()
pygame.quit()
quit()