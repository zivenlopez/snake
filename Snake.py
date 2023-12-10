"""
Establishes limits for the border
causes snake to teleport to other side and reverse direction
AND Game Over screen is added
"""

import pygame
import time
pygame.init()

# game window dimensions
game_width = 1500
game_height = 800

# color declarations 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# various game attributes
snake_block = 20   # snake,food,etc size
snake_speed = 30
snake_x = game_width/2   # x position
snake_y = game_height/2   # y position
snk_x_change = 0
snk_y_change = 0
font_style = pygame.font.SysFont(None, 50)   # declares font
game_over = False   # tells game when to close

clock = pygame.time.Clock()   # declares the game clock
dis = pygame.display.set_mode((game_width, game_height))   # creates game window
pygame.display.set_caption('Snake game by Ziven')   # caption at top of game window

def message(msg, color):     # function to display messages 
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [game_width/2 - 115, game_height/2])

while not game_over:
    for event in pygame.event.get():
        # if the user clicks QUIT button
        if event.type == pygame.QUIT:
            game_over = True
        
        # if a KEY is pressed
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:   # left button pressed
                snk_x_change = -10
                snk_y_change = 0
            elif event.key == pygame.K_RIGHT:   # right button pressed
                snk_x_change = 10
                snk_y_change = 0
            elif event.key == pygame.K_UP:   # up button pressed
                snk_x_change = 0
                snk_y_change = -10
            elif event.key == pygame.K_DOWN:   # down button pressed
                snk_x_change = 0
                snk_y_change = 10

    if snake_x < 0:
        snake_x = game_width
    elif snake_x > game_width:
        snake_x = 0
    if snake_y < 0:
        snake_y = game_height
    elif snake_y > game_height:
        snake_y = 0
    
    # movement control
    snake_x += snk_x_change
    snake_y += snk_y_change
    
    # game display commands
    dis.fill(black)   # makes background black
    pygame.draw.rect(dis, green, [snake_x, snake_y, snake_block, snake_block])   # draws snake
    pygame.display.update()

    clock.tick(snake_speed)


# executes right before the game quits
message("GAME OVER", red)
pygame.display.update()
time.sleep(2)

pygame.quit()
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLMAO ur bad\n\n\n\n\n\n")
quit()

