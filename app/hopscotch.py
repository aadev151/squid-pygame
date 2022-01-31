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

    next = pygame.transform.scale(
        load_image('glass2.png'),
        (200, 200))

    next = pygame.transform.scale(
        load_image('glass2.png'),
        (500, 200))


    count = 9

    font = pygame.font.Font(None, 50)
    text = font.render(
        f'Remaining glasses: {count - 1}', True,
        (200, 130, 200))
    place = text.get_rect(
        center=(400, 100))
    screen.blit(text, place)

    rand1 = randint(0, 1)
    if rand1 == 0:
        rand2 = 1
    else:
        rand2 = 0

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if count == 0:
                running = False
                pygame.quit()
                hopscotch_pass.main()
                break

            if event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if 270 < x < 370 and 370 > y > 250 and rand1 == 0:
                    count -= 1
                    screen.blit(bg, (0, 0))

                    next = pygame.transform.scale(
                        load_image('glass2.png'),
                        (200, 200))
                    next = pygame.transform.scale(
                        load_image('glass2.png'),
                        (500, 200))


                    rand1 = randint(0, 1)
                    if rand1 == 0:
                        rand2 = 1
                    else:
                        rand2 = 0

                    font = pygame.font.Font(None, 50)
                    text = font.render(
                        f'Remaining glasses: {count - 1}', True,
                        (200, 130, 200))
                    place = text.get_rect(
                        center=(400, 100))
                    screen.blit(text, place)

                elif 430 < x < 530 and 370 > y > 250 and rand2 == 0:
                    count -= 1
                    screen.blit(bg, (0, 0))

                    next = pygame.transform.scale(
                        load_image('glass2.png'),
                        (200, 200))

                    next = pygame.transform.scale(
                        load_image('glass2.png'),
                        (500, 200))

                    rand1 = randint(0, 1)
                    if rand1 == 0:
                        rand2 = 1
                    else:
                        rand2 = 0

                    font = pygame.font.Font(None, 50)
                    text = font.render(
                        f'Remaining glasses: {count - 1}', True,
                        (200, 130, 200))
                    place = text.get_rect(
                        center=(400, 100))
                    screen.blit(text, place)
                else:
                    running = False
                    pygame.quit()
                    hopscotch_death.main()
                    break
    try:
        pygame.display.flip()
    except pygame.error:
        pass