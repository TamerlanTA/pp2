import pygame
import sys

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Moving Ball")

# Set up the colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the ball
ball_radius = 25
ball_x = screen_width // 2
ball_y = screen_height // 2
ball_speed = 20

clock = pygame.time.Clock()

while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        ball_y -= ball_speed
    elif keys[pygame.K_DOWN]:
        ball_y += ball_speed
    elif keys[pygame.K_LEFT]:
        ball_x -= ball_speed
    elif keys[pygame.K_RIGHT]:
        ball_x += ball_speed

    # Ensure the ball stays within the screen boundaries
    if ball_x < ball_radius:
        ball_x = ball_radius
    elif ball_x > screen_width - ball_radius:
        ball_x = screen_width - ball_radius
    if ball_y < ball_radius:
        ball_y = ball_radius
    elif ball_y > screen_height - ball_radius:
        ball_y = screen_height - ball_radius

    # Draw the ball
    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    pygame.display.flip()
    clock.tick(60)
