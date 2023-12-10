"""
2nd (FUNCTIONAL) Attempt at Object Oriented Version
"""

import pygame
import random

class Food:
    def __init__(self, dis_width, dis_height, snake_block):
        self.foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        self.ntol = 20
        self.ptol = 35
    
    def draw_food(self, dis, snake_block, yellow):
        pygame.draw.rect(dis, yellow, [self.foodx, self.foody, snake_block, snake_block])

    def update_position(self, dis_width, dis_height, snake_block):
        self.foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

class Obstacle:
    def __init__(self, dis_width, dis_height, snake_block):
        self.obstx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        self.obsty = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        self.ntol = 20
        self.ptol = 35

    def draw_obstacle(self, dis, snake_block, red):
        pygame.draw.rect(dis, red, [self.obstx, self.obsty, snake_block, snake_block])

    def check_collision(self, x, y, snake_block):
        return x >= self.obstx - self.ntol and x <= self.obstx + self.ptol and y >= self.obsty - self.ntol and y <= self.obsty + self.ptol

class SnakeGame:
    def __init__(self):
        pygame.init()
       
        # color declarations  
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

        self.dis_width = 1500
        self.dis_height = 800

        self.snake_block = 30
        self.snake_change = 10
        self.snake_speed = 20

        # food and obstacle classes utilized
        self.food = Food(self.dis_width, self.dis_height, self.snake_block)  #create food instance
        self.obstacle = Obstacle(self.dis_width, self.dis_height, self.snake_block)  # create obstacle instance

        self.dis = pygame.display.set_mode((self.dis_width, self.dis_height))
        pygame.display.set_caption('Snake Game by Ziven')
        
        self.clock = pygame.time.Clock()  

        # declares fonts
        self.font_style = pygame.font.SysFont("bahnschrift", 55)
        self.score_font = pygame.font.SysFont("arialsms", 75)

    # SnakeGame methods
    def your_score(self, score):
        value = self.score_font.render("Your Score: " + str(score), True, self.white)
        self.dis.blit(value, [20, 20])

    def our_snake(self, snake_list):
        for x in snake_list:
            pygame.draw.rect(self.dis, self.green, [x[0], x[1], self.snake_block, self.snake_block])

    def message(self, msg, color):
        mesg = self.font_style.render(msg, True, color)
        self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 3])

    def game_loop(self):
        game_over = False
        game_close = False

        x1 = self.dis_width / 2
        y1 = self.dis_height / 2

        x1_change = 0
        y1_change = 0

        snake_list = []
        length_of_snake = 1

        ntol = 20
        ptol = 35

        ### starting screen here
        start = False
        while start == False:
            self.dis.fill(self.black)
            # top text
            self.score_font = pygame.font.SysFont("arialsms", 150)
            mesg = self.score_font.render("Hungry Python Reptile", True, self.green)
            self.dis.blit(mesg, [self.dis_width /5 - 90, self.dis_height / 2 - 150])  #the Game!
            self.score_font = pygame.font.SysFont("arialsms", 100)
            mesg = self.score_font.render("the Game", True, self.green)
            self.dis.blit(mesg, [self.dis_width /3 + 85, self.dis_height / 2 - 30])
            # middle text
            self.score_font = pygame.font.SysFont("arialsms", 65)
            mesg2 = self.score_font.render("EECE 2140 Final Project: Ziven Lopez", True, self.white)
            self.dis.blit(mesg2, [self.dis_width /6 + 100, self.dis_height / 2 + 100])
            # bottom text
            self.score_font = pygame.font.SysFont("arialsms", 35)
            mesg3 = self.score_font.render("(Press any key to continue)", True, self.red)
            self.dis.blit(mesg3, [self.dis_width /3 + 85, self.dis_height / 2 + 200])

            pygame.display.update()

            
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    start = True      

        self.font_style = pygame.font.SysFont("bahnschrift", 55)
        self.score_font = pygame.font.SysFont("arialsms", 75)

        while not game_over:
            while game_close:
                self.dis.fill(self.black)
                mesg = self.font_style.render("You Lost! Press C-Play Again or Q-Quit", True, self.red)
                self.dis.blit(mesg, [self.dis_width / 6, self.dis_height / 2])
                self.your_score(length_of_snake - 1)
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            self.game_loop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -self.snake_change
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = self.snake_change
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -self.snake_change
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = self.snake_change
                        x1_change = 0

            if x1 >= self.dis_width or x1 < 0 or y1 >= self.dis_height or y1 < 0:
                game_close = True

            x1 += x1_change
            y1 += y1_change

            self.dis.fill(self.black)

            # Drawing food
            self.food.draw_food(self.dis, self.snake_block, self.yellow)
             # Drawing obstacle
            self.obstacle.draw_obstacle(self.dis, self.snake_block, self.red)
            
            snake_head = []
            snake_head.append(x1)
            snake_head.append(y1)
            snake_list.append(snake_head)
            if len(snake_list) > length_of_snake:
                del snake_list[0]

            for x in snake_list[:-1]:
                if x == snake_head:
                    game_close = True

            self.our_snake(snake_list)
            self.your_score(length_of_snake - 1)

            pygame.display.update()
            
            # Checking collision with food
            if x1 >= self.food.foodx - self.food.ntol and x1 <= self.food.foodx + self.food.ptol and y1 >= self.food.foody - self.food.ntol and y1 <= self.food.foody + self.food.ptol:
                self.food.update_position(self.dis_width, self.dis_height, self.snake_block)
                length_of_snake += 1

            # Check collision with obstacle
            if self.obstacle.check_collision(x1, y1, self.snake_block):
                game_close = True  # Game over due to collision with obstacle

            self.clock.tick(self.snake_speed)

        pygame.quit()
        quit()    

if __name__ == "__main__":

    game = SnakeGame()
    game.game_loop()