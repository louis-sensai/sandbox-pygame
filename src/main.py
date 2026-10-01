import pygame
import random

# Import local modules
from snake import Snake
from food import Food
from game_window import GameWindow
from utils import GameUtils

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
BLOCK_SIZE = 20
SPEED = 20

# Colors
WHITE = (255, 255, 255)
BLACK = (22, 22, 22)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
YELLOW = (255, 255, 0)  # Pear color

def game_loop():
    game_over = False
    game_close = False
    
    # Create game objects
    snake = Snake(BLOCK_SIZE, SPEED)
    food = Food(WIDTH, HEIGHT, BLOCK_SIZE)
    game_window = GameWindow(WIDTH, HEIGHT, "Snake Game")
    utils = GameUtils()
    clock = pygame.time.Clock()
    
    # Set initial positions
    snake.reset()
    food.reset()
    pearx = -1
    pearly = -1
    pear_spawn_chance = 0.005
    
    while not game_over:
        while game_close:
            game_window.draw()
            utils.draw_message("You lost! Press Q-Quit or C-Play Again", RED, game_window.screen)
            utils.draw_score(snake.length - 1, game_window.screen)
            game_window.update_fps()
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                elif event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')
        
        if snake.check_collision(WIDTH, HEIGHT):
            game_close = True
        
        snake.move()
        
        # Check self-collision
        for segment in snake.segments[:-1]:
            if segment == [snake.x, snake.y]:
                game_close = True
        
        # Clear screen
        game_window.screen.fill((22, 22, 22))
        
        for segment in snake.segments:
            pygame.draw.rect(game_window.screen, GREEN, [segment[0], segment[1], BLOCK_SIZE, BLOCK_SIZE])
        
        # Draw food
        food.draw(game_window.screen)
        
        # Draw pear if it exists
        if pearx != -1 and pearly != -1:
            pygame.draw.circle(game_window.screen, YELLOW, [pearx + BLOCK_SIZE//2, pearly + BLOCK_SIZE//2], BLOCK_SIZE//2)
        
        utils.draw_score(snake.length - 1, game_window.screen)
        
        # Update display
        clock.tick(SPEED)
        game_window.update_fps(clock)
        pygame.display.update()
        
        # Handle pear spawning - only spawn if not currently on screen
        # Don't spawn pear if it was just eaten (avoid immediate respawn)
        if pearx == -1 and pearly == -1:
            if random.random() < pear_spawn_chance:
                pearx = round(random.randrange(0, WIDTH - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
                pearly = round(random.randrange(0, HEIGHT - BLOCK_SIZE) / BLOCK_SIZE) * BLOCK_SIZE
        
        # Check if snake eats food
        if snake.x == food.x and snake.y == food.y:
            food.reset()
            snake.length += 1
            utils.draw_score(snake.length - 1, game_window.screen)
        
        # Check if snake hits pear (removes body parts, no score)
        elif snake.x == pearx and snake.y == pearly:
            # Remove 1-3 segments from snake body
            segments_to_remove = random.randint(1, 3)
            if snake.length > segments_to_remove:
                snake.length -= segments_to_remove
            # Pear is eaten, hide it
            pearx = -1
            pearly = -1
        
        clock.tick(SPEED)
    
    pygame.quit()

game_loop()
