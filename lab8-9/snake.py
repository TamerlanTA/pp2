import pygame
import random
import sys
import time

# Initialize Pygame
pygame.init()

#BG = pygame.image.load("grass.png")

# Set up the screen
WIDTH, HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
WHITE = (255, 255, 255)
RED = (226, 73, 26)
GREEN = (0, 255, 0)
WGREEN = (169, 214, 85)
LGREEN = (163, 208, 72)
BLUE = (68, 115, 230)
GRAY = (200, 200, 200)
GOLD = (255,165,0)

# Snake properties
snake_size = 30


# Food properties
food_size = 30
food_color = RED, GOLD 
food_probabilities = [0.6, 0.4]  # Probabilities of each type of food
food_weights = len(food_color)
food_timer_duration = 5

# Font for displaying text
font = pygame.font.Font(None, 36)

CELL = 30

def draw_grid():
    colors = [WGREEN, LGREEN]
    for i in range(HEIGHT // CELL):
        for j in range(WIDTH // CELL):
            pygame.draw.rect(SCREEN, colors [(i+j) % 2], (i * CELL, j * CELL, CELL, CELL))

'''def render(self, screen):
    screen.fill((255,0,0))
    for i, item in enumerate(self.menu_items):'''
        

# Function to generate random position for food
def generate_food_position():
    x = random.randrange(0, WIDTH - food_size, food_size)
    y = random.randrange(0, HEIGHT - food_size, food_size)
    return x, y

def generate_food_color():
    return random.choices(food_color, weights=food_probabilities, k=1)[0]

# Function to display text on the screen
def display_text(text, color, x, y):
    text_surface = font.render(text, True, color)
    SCREEN.blit(text_surface, (x, y))

# Function to check collision with the borders
def check_border_collision(snake):
    x, y = snake[0]
    return x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT

# Function to check if snake collides with itself
def check_self_collision(snake):
    return snake[0] in snake[1:]

# Function to draw the snake
def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(SCREEN, BLUE, (segment[0], segment[1], snake_size, snake_size))

# Function to update the snake's position
def move_snake(snake, direction):
    x, y = snake[0]
    if direction == 'UP':
        y -= snake_size
    elif direction == 'DOWN':
        y += snake_size
    elif direction == 'LEFT':
        x -= snake_size
    elif direction == 'RIGHT':
        x += snake_size
    snake.insert(0, (x, y))
    snake.pop()


# Function to display game over message
def game_over():
    SCREEN.fill(WHITE)
    display_text("Game Over!", RED, WIDTH // 2 - 100, HEIGHT // 2)
    pygame.display.flip()
    pygame.time.delay(2000)
    pygame.quit()
    sys.exit()

# Main game loop
def main():
    snake = [(WIDTH // 2, HEIGHT // 2)]
    food_pos = generate_food_position()
    food_color = generate_food_color()  # Randomly choose the color of the first food
    food_timer_start = time.time()  # Start time for food timer
    direction = 'RIGHT'
    score = 0
    level = 1
    snake_speed = 10
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        draw_grid()

        keys = pygame.key.get_pressed()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != 'DOWN':
                direction = 'UP'
            elif event.key == pygame.K_DOWN and direction != 'UP':
                direction = 'DOWN'
            elif event.key == pygame.K_LEFT and direction != 'RIGHT':
                direction = 'LEFT'
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = 'RIGHT'

        move_snake(snake, direction)
        # Check for collision with border
        if check_border_collision(snake) or check_self_collision(snake):
            game_over()

        # Check if snake eats food
        if snake[0] == food_pos:
            snake.append((food_pos[0], food_pos[1]))
            score += 1
            food_pos = generate_food_position()
            food_color = generate_food_color()  
            food_timer_start = time.time()  # Reset the food timer
            if score % 3 == 0:  # Increase level every 3 foods eaten
                level += 1  
                snake_speed += 1/5  # Increase speed with each level

        # Check if food timer has expired
        if time.time() - food_timer_start >= food_timer_duration:
            food_pos = generate_food_position()
            food_color = generate_food_color()
            food_timer_start = time.time()  # Reset the food timer


        # Clear the screen
        #SCREEN.fill(WHITE)
        #SCREEN.blit(BG, (0, 0))

        # Draw the snake and food
        draw_snake(snake)
        
        pygame.draw.rect(SCREEN, food_color, (food_pos[0], food_pos[1], food_size, food_size))

        # Display score and level
        display_text(f"Score: {score}", WHITE, 10, 10)
        display_text(f"Level: {level}", WHITE, 10, 50)

        # Update the display
        pygame.display.update()

        # Control the snake's speed
        clock.tick(snake_speed)

if __name__ == "__main__":
    main()
