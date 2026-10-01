import pygame
import random

YELLOW = (255, 255, 0)  # Pear color

class Pear:
    """Class to handle the pear (bonus item)"""
    
    def __init__(self, width, height, block_size):
        self.width = width
        self.height = height
        self.block_size = block_size
        self.x = -1
        self.y = -1
    
    def reset(self):
        """Reset pear position (hide it)"""
        self.x = -1
        self.y = -1
    
    def spawn(self):
        """Spawn pear at random position"""
        self.x = round(random.randrange(0, self.width - self.block_size) / self.block_size) * self.block_size
        self.y = round(random.randrange(0, self.height - self.block_size) / self.block_size) * self.block_size
    
    def draw(self, screen):
        """Draw pear on screen"""
        if self.x != -1 and self.y != -1:
            pygame.draw.circle(screen, YELLOW, [self.x + self.block_size//2, self.y + self.block_size//2], self.block_size//2)

    def is_eaten(self, snake_x, snake_y):
        """Check if pear is eaten"""
        return self.x == snake_x and self.y == snake_y
