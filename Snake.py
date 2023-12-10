"""
Green square movement, corresponding to arrow keys
"""

import pygame
pygame.init()

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)

dis = pygame.display.set_mode((1000,800))
pygame.display.set_caption('Snake game by Ziven')

game_over = False

x1 = 300
y1 = 300

x1_change = 0
y1_change = 0

clock = pygame.time.Clock()

while not game_over:
    for event in pygame.event.get():
        # if the user clicks QUIT button
        if event.type == pygame.QUIT:
            game_over = True
        
        # if a KEY is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:   # left button pressed
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:   # right button pressed
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:   # up button pressed
                x1_change = 0
                y1_change = -10
            elif event.key == pygame.K_DOWN:   # down button pressed
                x1_change = 0
                y1_change = 10
    
    # movement control
    x1 += x1_change
    y1 += y1_change
    
    dis.fill(black)

    pygame.draw.rect(dis, green, [x1, y1, 20, 20])
    pygame.display.update()

    clock.tick(20)

pygame.quit()
quit()