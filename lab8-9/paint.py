import pygame
import sys

pygame.init()

WIDTH = 960
HEIGHT = 640 

#collor
colorBLACK = (0, 0, 0)
colorWHITE = (255, 255, 255)
colorRED = (255, 0, 0)
colorGREEN = (0, 255, 0)
colorBLUE = (0, 0, 255)
colorYELLOW = (255, 255, 0)

mode = colorWHITE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))

done = False

LMBpressed = False
prevX, prevY = 0, 0
currX, currY = 0, 0

radius = 5

def calculate_radius(x1, y1, x2, y2):
    return max(abs(x2 - x1), abs(y2 - y1)) // 2

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x2 - x1), abs(y2 - y1))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            print("LMB pressed")
            LMBpressed = True


        if event.type == pygame.MOUSEMOTION:
            print(event.pos)
            currX = event.pos[0]
            currY = event.pos[1]

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            print("LMB released")
            LMBpressed = False

        if event.type == pygame.KEYDOWN:
            #choose color
            if event.key == pygame.K_r:
                mode = colorRED
                radius = 5
            elif event.key == pygame.K_g:
                mode = colorGREEN
                radius = 5
            elif event.key == pygame.K_b:
                mode = colorBLUE
                radius = 5
            elif event.key == pygame.K_y:
                mode = colorYELLOW
                radius = 5
            elif event.key == pygame.K_w:
                mode = colorWHITE
                radius = 5
            elif event.key == pygame.K_e:
                mode = colorBLACK
                radius = 50

            if event.key == pygame.K_1:
                screen.fill(colorBLACK)

            # Обработка клавиш стрелок
            if event.key == pygame.K_UP:
                radius += 5  # Увеличиваем радиус кисти при нажатии стрелки вверх
            elif event.key == pygame.K_DOWN:
                radius = max(5, radius - 5)  # Уменьшаем радиус кисти при нажатии стрелки вниз

        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 4:
            # Обработка колеса мыши вверх
            radius += 5  # Увеличиваем радиус кисти при прокрутке колеса мыши вверх
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 5:
            # Обработка колеса мыши вниз
            radius = max(5, radius - 5)  # Уменьшаем радиус кисти при прокрутке колеса мыши вниз


            #drow rec
            #rec = True
            """if event.key == pygame.K_0:
                while rec:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                rec = False
                        #choose color
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                mode = colorRED
                            elif event.key == pygame.K_g:
                                mode = colorGREEN
                            elif event.key == pygame.K_b:
                                mode = colorBLUE
                            elif event.key == pygame.K_y:
                                mode = colorYELLOW
                            elif event.key == pygame.K_w:
                                mode = colorWHITE       
                            
                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            print("LMB pressed")
                            LMBpressed = True
                            prevX = event.pos[0]
                            prevY = event.pos[1]

                        if event.type == pygame.MOUSEMOTION:
                            print(event.pos)
                            currX = event.pos[0]
                            currY = event.pos[1]

                        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            print("LMB released")
                            LMBpressed = False
                            pygame.draw.rect(screen, mode, calculate_rect(prevX, prevY, currX, currY), 2)
                            base_layer.blit(screen, (0, 0))
                                

                    if LMBpressed:
                        screen.blit(base_layer, (0, 0))
                        pygame.draw.rect(screen, mode, calculate_rect(prevX, prevY, currX, currY), 2)

                    pygame.display.flip()"""
                    
                    
            #draw circle
            #cir = True
            """if event.key == pygame.K_9:
                while cir:
                    for event in pygame.event.get():
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_q:
                                cir = False
                        #choose color
                        if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_r:
                                mode = colorRED
                            elif event.key == pygame.K_g:
                                mode = colorGREEN
                            elif event.key == pygame.K_b:
                                mode = colorBLUE
                            elif event.key == pygame.K_y:
                                mode = colorYELLOW
                            elif event.key == pygame.K_w:
                                mode = colorWHITE       

                        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                            print("LMB pressed")
                            LMBpressed = True
                            prevX, prevY = event.pos

                        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                            print("LMB released")
                            LMBpressed = False
                            pygame.draw.circle(screen, mode, (prevX, prevY), radius, 2)
                            base_layer.blit(screen, (0, 0))
                        
                    if LMBpressed:
                        screen.blit(base_layer, (0, 0))
                        mouseX, mouseY = pygame.mouse.get_pos()
                        radius = calculate_radius(prevX, prevY, mouseX, mouseY)
                        pygame.draw.circle(screen, mode, (prevX, prevY), radius, 2)

                    pygame.display.flip()"""

#dont touch
    if LMBpressed:
        pygame.draw.line(screen, mode, (prevX, prevY), (currX, currY), radius)
        #pygame.draw.circle(screen, mode, (prevX, prevY), (currX, currY), radius)

    prevX = currX
    prevY = currY

    pygame.display.flip()

        

