import pygame

class GameWindow:
    def __init__(self, width, height, fps_counter):
        self.width = width
        self.height = height
        self.fps_counter = fps_counter
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Snake Game')
    
    def update_fps(self, clock):
        self.fps_counter = f"Snake Game | {int(clock.get_fps())} fps"
        pygame.display.set_caption(self.fps_counter)
    
    def draw(self):
        self.screen.fill((22, 22, 22))
        # Don't call pygame.display.update() here - let the game loop do it
