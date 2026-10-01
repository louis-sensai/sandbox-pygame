import pygame
import random

class Food:
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.reset()
    
    def reset(self):
        self.x = round(random.randrange(0, self.width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, self.height - self.block_size) / self.block_size) * self.block_size
    
    def draw(self, screen):
        pygame.draw.circle(screen, (213, 50, 80), [self.x + self.block_size//2, self.y + self.block_size//2], self.block_size//2)
    
    def check_collision(self, snake_x, snake_y):
        return snake_x == self.x and snake_y == self.y
