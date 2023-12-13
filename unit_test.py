import unittest
from Snake import Food, PowerUp, Obstacle

class TestSnakeGame(unittest.TestCase):
    def setUp(self):
        self.dis_width = 1500
        self.dis_height = 800
        self.snake_block = 30

    def test_food_initialization(self):
        food = Food(self.dis_width, self.dis_height, self.snake_block)
        print(f'Food Initialization: foodx={food.foodx}, foody={food.foody}')
        self.assertTrue(0 <= food.foodx < self.dis_width)
        self.assertTrue(0 <= food.foody < self.dis_height)

    def test_food_update_position(self):
        food = Food(self.dis_width, self.dis_height, self.snake_block)
        initial_position = (food.foodx, food.foody)
        print(f'Food Update Position - Before: foodx={food.foodx}, foody={food.foody}')
        food.update_position(self.dis_width, self.dis_height, self.snake_block)
        updated_position = (food.foodx, food.foody)
        print(f'Food Update Position - After: foodx={food.foodx}, foody={food.foody}')
        self.assertNotEqual(initial_position, updated_position)

    def test_powerup_initialization(self):
        powerup = PowerUp(self.dis_width, self.dis_height, self.snake_block)
        print(f'PowerUp Initialization: foodx={powerup.foodx}, foody={powerup.foody}')
        self.assertTrue(0 <= powerup.foodx < self.dis_width)
        self.assertTrue(0 <= powerup.foody < self.dis_height)

    def test_obstacle_initialization(self):
        num_obstacles = 5
        obstacle = Obstacle(self.dis_width, self.dis_height, self.snake_block, num_obstacles)
        print(f'Obstacle Initialization: Number of Obstacles={len(obstacle.obstacles)}')
        self.assertEqual(len(obstacle.obstacles), num_obstacles)

    def test_obstacle_collision(self):
        num_obstacles = 1
        obstacle = Obstacle(self.dis_width, self.dis_height, self.snake_block, num_obstacles)
        obstacle_x = obstacle.obstacles[0]['x']
        obstacle_y = obstacle.obstacles[0]['y']
        print(f'Obstacle Collision Check: x={obstacle_x}, y={obstacle_y}')
        self.assertTrue(obstacle.check_collision(obstacle_x, obstacle_y, self.snake_block))

if __name__ == '__main__':
    unittest.main()
