import pygame

pygame.init()
screen = pygame.display.set_mode((800, 400))

playlist = ['sounds/1.mp3', 'sounds/2.mp3', 'sounds/3.mp3']
current_song = 0

def play_next_song():
    global current_song
    current_song = (current_song + 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play(-1)

def play_previous_song():
    global current_song
    current_song = (current_song - 1) % len(playlist)
    pygame.mixer.music.load(playlist[current_song])
    pygame.mixer.music.play(-1)


pygame.mixer.music.load(playlist[current_song])

running = True
paused = False

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_m:
                pygame.mixer.music.play()
            if event.key == pygame.K_SPACE:
                if paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    pygame.mixer.music.pause()
                    paused = True
            if event.key == pygame.K_d:
                play_next_song()
            if event.key == pygame.K_a:
                play_previous_song() 
    pygame.display.update()

pygame.mixer.music.stop()
pygame.quit()
