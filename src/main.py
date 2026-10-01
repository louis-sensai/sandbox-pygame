import pygame

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake Game")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Game logic here

    # Drawing code here
    screen.fill((0, 0, 0))  # Fill the screen with black
    pygame.display.flip()

# Quit Pygame
pygame.quit()