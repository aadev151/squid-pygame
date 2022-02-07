import pygame
from random import randint
from time import time, sleep
import sqlite3

from setup import width, height
from setup import load_image

import hopscotch_death
import hopscotch_pass


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))
    pygame.display.set_caption('Hopscotch')

    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('g_b_bg2.png'), (width, height))
    screen.blit(bg, (0, 0))

    current_glasses = []
    for i in range(7):
        c = randint(0, 1)
        current_glasses.append([c, 0 if c == 1 else 1])

    glasses = []

    y = 500

    for i in range(6):
        if current_glasses[i][0] == 0:
            glass1 = pygame.draw.rect(screen, pygame.Color(128, 0, 128),
                                      (320, y, 60, 60))
            glass2 = pygame.draw.rect(screen, pygame.Color(20, 70, 160),
                                      (400, y, 60, 60))
        else:
            glass1 = pygame.draw.rect(screen, pygame.Color(20, 70, 160),
                                      (320, y, 60, 60))
            glass2 = pygame.draw.rect(screen, pygame.Color(128, 0, 128),
                                      (400, y, 60, 60))

        glasses.append([glass1, glass2])
        y -= 80

    glass1 = pygame.draw.rect(screen, pygame.Color(20, 70, 160),
                              (320, 25, 60, 60))
    glass2 = pygame.draw.rect(screen, pygame.Color(20, 70, 160),
                              (400, 25, 60, 60))
    glasses.append([glass1, glass2])
    i = 0

    f1 = pygame.font.Font(None, 60)
    text1 = f1.render('?', True, pygame.Color(53, 116, 232))
    screen.blit(text1, (335, 35))
    screen.blit(text1, (415, 35))
    pygame.display.flip()

    sleep(2.5)

    start_time = time()
    k = 7
    sleep_count = 0
    death_lst = [(170, 357), (453, 352)]

    god_mode = False

    fps = 50
    clock = pygame.time.Clock()

    running = True
    while running:
        time_playing = time() - start_time - 2 * sleep_count
        time_remaining = int(31 - time_playing)

        if time_remaining == 0:
            pygame.quit()
            hopscotch_death.main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.mod == pygame.KMOD_CAPS:
                    god_mode = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if glasses[i][current_glasses[i].index(0)].collidepoint(mouse_position):
                    font = pygame.font.Font(None, 40)
                    pass_label = font.render('You got this one', True,
                                                (237, 27, 118))
                    if current_glasses[i].index(0) == 0:
                        screen.blit(pass_label, (180, 400))
                    else:
                        screen.blit(pass_label, (470, 400))
                    pygame.display.flip()
                    sleep(2)
                    sleep_count += 1
                    k -= 1
                    i += 1

                    if k == 0:
                        connection = sqlite3.connect('data/db/time.db')
                        connection.cursor().execute(
                            'UPDATE levels SET time = ? WHERE id = 3',
                            (int(time_playing),))
                        connection.commit()
                        connection.close()
                        pygame.quit()
                        hopscotch_pass.main()
                        break

                elif glasses[i][current_glasses[i].index(1)].collidepoint(
                            mouse_position) and \
                            not god_mode:
                    death = pygame.transform.scale(
                            load_image('glass.png'),
                            (160, 140))
                    screen.blit(death, death_lst[current_glasses[i].index(1)])
                    pygame.display.flip()
                    pygame.quit()
                    hopscotch_death.main()

            try:
                screen.blit(bg, (0, 0))
                glass1 = pygame.draw.polygon(screen, pygame.Color(20, 70, 160),
                                             ((200, 357), (353, 354), (337, 494),
                                              (110, 500)))
                pygame.draw.aalines(screen, pygame.Color(20, 70, 160), True,
                                    ((200, 357), (353, 354), (335, 494),
                                     (110, 500)))
                glass2 = pygame.draw.polygon(screen, pygame.Color(20, 70, 160),
                                             ((447, 352), (591, 350), (693, 484),
                                              (475, 490)))
                pygame.draw.aalines(screen, pygame.Color(20, 70, 160), True,
                                    ((447, 352), (591, 350), (693, 484),
                                     (475, 490)))
                glasses[i] = [glass1, glass2]

                font = pygame.font.Font(None, 50)
                time_label = font.render(str(time_remaining), True,
                                         pygame.Color('white'))
                screen.blit(time_label, (40, 40))
                glasses_label = font.render(f'{k} glass(es) left.', True,
                                            pygame.Color('white'))
                screen.blit(glasses_label, (40, 80))

                clock.tick(fps)
                pygame.display.flip()
            except pygame.error:
                pass

    pygame.quit()
main()