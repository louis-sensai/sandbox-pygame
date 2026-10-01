import pygame

class GameUtils:
    def __init__(self):
        self.font_style = pygame.font.SysFont("bahnschrift", 25)
        self.score_font = pygame.font.SysFont("comicsansms", 35)
    
    def draw_score(self, score, screen):
        value = self.score_font.render(f"Score: {score}", True, (50, 153, 213))
        screen.blit(value, [0, 0])
    
    def draw_message(self, msg, color, screen):
        mesg = self.font_style.render(msg, True, color)
        screen.blit(mesg, [screen.get_width()/6, screen.get_height()/3])
