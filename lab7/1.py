import pygame
import datetime

def rot_center(image, angle, x, y):
    
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

    return rotated_image, new_rect

pygame.init()
screen = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("MickeyClock")

clock = pygame.image.load('/Users/tamerlan/Pyt/lab7/mainclock.png')
left_a = pygame.image.load('/Users/tamerlan/Pyt/lab7/leftarm.png')
right_a = pygame.image.load('/Users/tamerlan/Pyt/lab7/rightarm.png')

running = True

while running:

    screen.fill((255, 255, 255))

    now = datetime.datetime.now()
    second_angle = now.second * 6 * (-1)
    minute_angle = now.minute * 6 * (-1) 
    
    rotated_right_arm, new_rect_right = rot_center(right_a, second_angle, 500, 375)
    rotated_left_arm, new_rect_left = rot_center(left_a, minute_angle, 500, 375)
    
    screen.blit(clock, (0, 0))
    screen.blit(rotated_right_arm, new_rect_right.topleft)
    screen.blit(rotated_left_arm, new_rect_left.topleft)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()

