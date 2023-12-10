"""
1st Attempt at Object Oriented Version
"""

import pygame

class Game:
    def __init__(self):
        pygame.init()

        std_block = 50
        self.window_x = 1500
        self.window_y = 800

        self.size = (std_block)
        
        # color declarations  
        self.white = (255, 255, 255)
        self.black = (0, 0, 0)
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)
        self.yellow = (255, 255, 0)

        self.dis = pygame.display.set_mode((self.window_x, self.window_y))
        pygame.display.set_caption('Snake Game by Ziven')
        self.game_over = False
        self.clock = pygame.time.Clock()
        self.snake = Movement()

    def handle_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            self.snake.handle_input(event)

    def game_loop(self):
        while not self.game_over:
            self.handle_input()
            self.snake.move()
            self.dis.fill(self.black)
            pygame.draw.rect(self.dis, self.green, [self.snake.x, self.snake.y, self.size, self.size])
            pygame.display.update()
            self.clock.tick(30)

        pygame.quit()
        quit()

class Movement:
    def __init__(self, x=300, y=300):
        self.x = x
        self.y = y
        self.x_change = 0
        self.y_change = 0

    def handle_input(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.x_change = -10
                self.y_change = 0
            elif event.key == pygame.K_RIGHT:
                self.x_change = 10
                self.y_change = 0
            elif event.key == pygame.K_UP:
                self.y_change = -10
                self.x_change = 0
            elif event.key == pygame.K_DOWN:
                self.y_change = 10
                self.x_change = 0

    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        if self.x < 0:
            self.x = Game().window_x
        elif self.x > Game().window_x:
            self.x = 0
        if self.y < 0:
            self.y = Game().window_y
        elif self.y > Game().window_y:
            self.y = 0

def main():
    snake_game = Game()
    snake_game.game_loop()

if __name__ == "__main__":
    main()
