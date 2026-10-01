import pygame
import random

# Constants
WIDTH, HEIGHT = 800, 600

class Snake:
    def __init__(self, block_size, speed):
        self.block_size = block_size
        self.speed = speed
        self.reset()
    
    def reset(self):
        self.reset_position()
        self.reset_length()
    
    def reset_position(self):
        # Start in the center
        self.x = WIDTH // 2 - self.block_size
        self.y = HEIGHT // 2 - self.block_size
        self.x_change = 0
        self.y_change = 0
    
    def reset_length(self):
        self.segments = [[0, 0]]
        self.length = 1
    
    def move(self):
        self.x += self.x_change
        self.y += self.y_change
        self.segments.append([self.x, self.y])
        
        # Remove the tail segment if snake is too long
        if len(self.segments) > self.length:
            self.segments.pop(0)
    
    def change_direction(self, direction):
        if direction == 'LEFT' and self.x_change == 0:
            self.x_change = -self.block_size
            self.y_change = 0
        elif direction == 'RIGHT' and self.x_change == 0:
            self.x_change = self.block_size
            self.y_change = 0
        elif direction == 'UP' and self.y_change == 0:
            self.y_change = -self.block_size
            self.x_change = 0
        elif direction == 'DOWN' and self.y_change == 0:
            self.y_change = self.block_size
            self.x_change = 0
    
    def check_collision(self, screen_width, screen_height):
        if self.x >= screen_width or self.x < 0 or self.y >= screen_height or self.y < 0:
            return True
        return False
    
    def check_self_collision(self):
        head = [self.x, self.y]
        for segment in self.segments[:-1]:
            if segment == head:
                return True
        return False
    
    def draw(self, screen):
        for segment in self.segments:
            pygame.draw.rect(screen, (0, 255, 0), [segment[0], segment[1], self.block_size, self.block_size])
