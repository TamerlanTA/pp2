import pygame
import sys
from random import randint
from time import sleep

pygame.init()

WIDTH = 400
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

BACKGROUND = pygame.image.load("/Users/tamerlan/Pyt/raicer/resourse/AnimatedStreet.png")

# color palette
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

#Setting up FPS
FPS = 60
clock = pygame.time.Clock()

#Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBLACK)
SCORE = 0

done = False

#creating Player 
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/tamerlan/Pyt/raicer/resourse/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH // 2, HEIGHT - 55)

    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_RIGHT] and self.rect[0] + self.rect[2] < WIDTH:
            self.rect.move_ip(5, 0)
        if pressed[pygame.K_LEFT] and self.rect[0] > 0:
            self.rect.move_ip(-5, 0)

#creating Enemy
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/tamerlan/Pyt/raicer/resourse/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (randint(0 + self.rect.w // 2 , WIDTH - self.rect.w // 2), 20)
        self.speed = 5

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > HEIGHT:
            SCORE += 1
            self.rect.center = (randint(0 + self.rect.w // 2 , WIDTH - self.rect.w // 2), 20)

#creating Coin
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("/Users/tamerlan/Pyt/raicer/resourse/coin.png")  # Load coin image
        self.rect = self.image.get_rect()
        self.rect.center = (randint(0 + self.rect.w // 2 , WIDTH - self.rect.w // 2), 20)
        self.speed = 5
        self.value = randint(1, 10)  # Assign a random value to the coin

    def move(self):
        global SCORE
        self.rect.move_ip(0, self.speed)
        if self.rect.bottom > HEIGHT:
            SCORE += self.value
            self.rect.center = (randint(0 + self.rect.w // 2 , WIDTH - self.rect.w // 2), 20)

#Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#Setting up Sprites
P1 = Player()
E1 = Enemy()
C1 = Coin()

#Creating Sprites Groups
enemies = pygame.sprite.Group()
coins = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
enemies.add(E1)
coins.add(C1)
all_sprites.add(P1, E1, C1)

#Game Loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == INC_SPEED:
            N = 15
            if SCORE >= N:
                E1.speed += 1
                N += 10
    
    screen.blit(BACKGROUND, (0, 0))
    scores = font_small.render(str(SCORE), True, colorBLACK)
    screen.blit(scores, (10,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('/Users/tamerlan/Pyt/raicer/resourse/crash.wav').play()
        sleep(0.5)

        print("Collision!")
        screen.blit(game_over, (30, 250))
        screen.fill(colorRED)
        pygame.display.flip()
        sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.flip()

    clock.tick(FPS)

# Removing the event from the timer
pygame.time.set_timer(INC_SPEED, 0)