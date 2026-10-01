import pygame
import random

# Import local modules
from snake import Snake
from food import Food
from pear import Pear
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
    pear = Pear(WIDTH, HEIGHT, BLOCK_SIZE)
    game_window = GameWindow(WIDTH, HEIGHT, "Snake Game")
    utils = GameUtils()
    clock = pygame.time.Clock()
    
    # Set initial positions
    snake.reset()
    food.reset()
    pear.reset()
    pear_spawn_chance = 0.005
    
    while not game_over:
        while game_close:
            game_window.draw()
            utils.draw_message("You lost! Press Q-Quit or C-Play Again", RED, game_window.screen)
            utils.draw_score(snake.length - 1, game_window.screen)
            game_window.update_fps(clock)
            pygame.display.update()
            
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        # Reset game objects instead of creating new ones
                        snake.reset()
                        food.reset()
                        pear.reset()
                        game_close = False
        
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
        
        # Draw pear
        pear.draw(game_window.screen)
        
        utils.draw_score(snake.length - 1, game_window.screen)
        
        # Update display
        clock.tick(SPEED)
        game_window.update_fps(clock)
        pygame.display.update()
        
        # Handle pear spawning - only spawn if not currently on screen
        # Don't spawn pear if it was just eaten (avoid immediate respawn)
        if pear.x == -1 and pear.y == -1:
            if random.random() < pear_spawn_chance:
                pear.spawn()
        
        # Check if snake eats food
        if snake.x == food.x and snake.y == food.y:
            food.reset()
            snake.length += 1
            utils.draw_score(snake.length - 1, game_window.screen)
        
        # Check if snake hits pear (removes body parts, no score)
        elif pear.is_eaten(snake.x, snake.y):
            # Remove 1-3 segments from snake body
            segments_to_remove = random.randint(1, 3)
            if snake.length > segments_to_remove:
                snake.length -= segments_to_remove
            # Pear is eaten, hide it
            pear.reset()
        
        clock.tick(SPEED)
    
    pygame.quit()

game_loop()
