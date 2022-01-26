import pygame
from setup import width, height
from setup import load_image
from random import randint
import time

import hopscotch_pass
import hopscotch_death


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))
    pygame.display.set_caption('Hopscotch')

    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('g_b_bg.png'), (width, height))
    screen.blit(bg, (0, 0))

    pygame.draw.rect(screen, pygame.Color(50, 239, 255), (270, 250, 100, 120))
    pygame.draw.rect(screen, pygame.Color(0, 239, 255), (430, 250, 100, 120))

    rand1 = randint(0, 1)
    if rand1 == 0:
        rand2 = 1
    else:
        rand2 = 0

    count = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if count == 9:
                running = False
                pygame.quit()
                hopscotch_pass.main()
                break

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 270 < x < 370 and 370 > y > 250 and rand1 == 0:
                    count += 1

                    pygame.draw.rect(screen, pygame.Color(50, 239, 255),
                                     (270, 250, 100, 120))
                    pygame.draw.rect(screen, pygame.Color(50, 239, 255),
                                     (430, 250, 100, 120))

                    rand1 = randint(0, 1)
                    if rand1 == 0:
                        rand2 = 1
                    else:
                        rand2 = 0

                elif 430 < x < 530 and 370 > y > 250 and rand2 == 0:
                    count += 1

                    pygame.draw.rect(screen, pygame.Color(50, 239, 255),
                                     (270, 250, 100, 120))
                    pygame.draw.rect(screen, pygame.Color(50, 239, 255),
                                     (430, 250, 100, 120))

                    rand1 = randint(0, 1)
                    if rand1 == 0:
                        rand2 = 1
                    else:
                        rand2 = 0
                else:
                    running = False
                    pygame.quit()
                    hopscotch_death.main()
                    break
    try:
        screen.blit(bg, (0, 0))

        pygame.draw.rect(screen, pygame.Color(50, 239, 255), (270, 250, 100, 120))
        pygame.draw.rect(screen, pygame.Color(0, 239, 255), (430, 250, 100, 120))
        pygame.display.flip()
    except pygame.error:
        pass
