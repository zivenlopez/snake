"""
Creates food for the snake to eat
"""

import pygame
import time
import random
pygame.init()

# game window dimensions
game_width = 1550
game_height = 800

# color declarations 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)

# various game attributes
snake_block = 20   # snake,food,etc size
snake_speed = 30
font_style = pygame.font.SysFont(None, 50)   # declares font

clock = pygame.time.Clock()   # declares the game clock
dis = pygame.display.set_mode((game_width, game_height))   # creates game window
pygame.display.set_caption('Snake game by Ziven')   # caption at top of game window

def message(msg, color):     # function to display messages 
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [game_width/2 - 115, game_height/2])

def gameLoop():   # game function
    game_over = False
    game_close = False

    # snake attributes
    snake_x = game_width/2   # x position
    snake_y = game_height/2   # y position
    snk_x_change = 0
    snk_y_change = 0

    # food creation
    foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0

    # obstacle creation
    obstx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    obsty = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0

    while not game_over:
        # this only runs AFTER the game has been played --- asks the user to replay or quit
        while game_close == True:
            message("YOU LOSE! Press Q-Quit or C-Play Again", red)
            pygame.display.update()

            for event in pygame.event.get():
                
                if event.type == pygame.KEYDOWN:   # if a key is pressed
                    
                    if event.key == pygame.K_q:   # q is pressed
                        game_over = True
                        game_close = False   
                    if event.key == pygame.K_c:   # c is pressed
                        gameLoop()
        
        # runs the game
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
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])   # draws food
        pygame.draw.rect(dis, red, [obstx, obsty, 4*snake_block, 4*snake_block])   # draws obstacles
        pygame.draw.rect(dis, green, [snake_x, snake_y, snake_block, snake_block])   # draws snake
        pygame.display.update()

        # this checks if snake has hit a food x and y coordinate location
        if snake_x == foodx and snake_y == foody:
            print("Yummy!!!")
        # this checks if snake has hit an obstacle
        if snake_x >= obstx-20 and snake_x <= obstx+80 and snake_y >= obsty-20 and snake_y <= obsty+80:
            print("OH NO")
            game_close = True

        clock.tick(snake_speed)   # snake's movement

    # executes right before the game quits
    message("GAME OVER", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLMAO ur bad\n\n\n\n\n\n")
    quit()

# this calls the gameLoop function
gameLoop()
