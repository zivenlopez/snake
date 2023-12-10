"""
Snake Obstacle Detection Improved
Snake speed reduced for better control
Tolerances introduced so the snake doesn't have to completely overlap food or obstacle in order for it to count as a hit
Now snake can merely graze it and it will detect.
"""

import pygame
import time
import random
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
yellow = (255, 255, 0)

# various game attributes
snake_block = 30   # snake,food,etc size
snake_speed = 20
regular_font = pygame.font.SysFont("bahnschrift", 50)   # declares font
score_font = pygame.font.SysFont("arialsms", 75)   # declares 2nd font
food_p_tol = 35   #how close to target snake has to be to food
food_n_tol = 20
obst_p_tol = 120   #how close to target snake has to be to obstacle
obst_n_tol = 30

clock = pygame.time.Clock()   # declares the game clock
dis = pygame.display.set_mode((game_width, game_height))   # creates game window
pygame.display.set_caption('Snake game by Ziven')   # caption at top of game window

def your_score(score):
    value = score_font.render("Your Score: " + str(score), True, white)
    dis.blit(value, [20, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, green, [x[0], x[1], snake_block, snake_block])

def message(msg, color):     # function to display messages 
    mesg = regular_font.render(msg, True, color)
    dis.blit(mesg, [game_width/2 - 115, game_height/2])

def gameLoop():   # game function
    game_over = False
    game_close = False

    # snake attributes
    snake_x = game_width/2   # x position
    snake_y = game_height/2   # y position
    snk_x_change = 0
    snk_y_change = 0
    snake_list = []
    snake_length = 1

    # food creation               can turn this into an outside function all (returns two integers or a list)
    foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0

    # obstacle creation
    obst1x = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
    obst1y = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0

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

        # display commands
        dis.fill(black)   # makes background black
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])   # draws food
        pygame.draw.rect(dis, red, [obst1x, obst1y, 4*snake_block, 4*snake_block])   # draws obstacles
        #pygame.draw.rect(dis, green, [snake_x, snake_y, snake_block, snake_block])   # draws snake

        snake_head = []
        snake_head.append(snake_x)
        snake_head.append(snake_y)
        snake_list.append(snake_head)
        if len(snake_list) > snake_length:
            del snake_list[0]
        
        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)   # calls our_snake function
        your_score(snake_length - 1)   # calls your_score function (-1 because you start with a head)

        pygame.display.update()

        # this checks if snake has hit a food x and y coordinate location
        if snake_x >= foodx-food_n_tol and snake_x <= foodx+food_p_tol and snake_y >= foody-food_n_tol and snake_y <= foody+food_p_tol:
            print("Yummy!!!")
            # food creation
            foodx = round(random.randrange(0, game_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, game_height - snake_block) / 10.0) * 10.0
            snake_length += 1

        # this checks if snake has hit an obstacle
        if snake_x >= obst1x-obst_n_tol and snake_x <= obst1x+obst_p_tol and snake_y >= obst1y-obst_n_tol and snake_y <= obst1y+obst_p_tol:
            print("OH NO")
            game_close = True

        clock.tick(snake_speed)   # snake's movement

    # executes right before the game quits
    message("GAME OVER", red)
    pygame.display.update()
    time.sleep(2)

    pygame.quit()
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThanks for playing!!!\n\n\n\n\n\n")
    quit()

# this calls the gameLoop function
gameLoop()


##### Ideas for later #####
# increase speed over time
# various powerups
# save highscores in a .txt file
# different maps
# different starting difficulties
# enter name to begin
# sound effects for food, winning, losing

## look into
# importing images
# importing music