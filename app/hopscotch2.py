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

    bg = pygame.transform.scale(load_image('g_b_bg.png'), (width, height))
    screen.blit(bg, (0, 0))
    death_lst = [(270, 250), (430, 250)]

    glass1 = pygame.draw.rect(screen, pygame.Color(50, 239, 255), (270, 250, 120, 140))
    glass2 = pygame.draw.rect(screen, pygame.Color(50, 239, 255), (430, 250, 120, 140))

    glasses = [glass1, glass2]
    current_glass = randint(0, 1)

    start_time = time()
    k = 8
    sleep_count = 0

    god_mode = False

    fps = 50
    clock = pygame.time.Clock()
    running = True
    while running:
        time_playing = time() - start_time - 2 * sleep_count
        time_remaining = int(31 - time_playing)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.mod == pygame.KMOD_CAPS:
                    god_mode = True

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if glasses[current_glass].collidepoint(mouse_position):
                    font = pygame.font.Font(None, 40)
                    pass_label = font.render('You got this one', True, (237, 27, 118))
                    screen.blit(pass_label, ((width - pass_label.get_width()) // 2,
                                             (height - pass_label.get_height()) // 2))
                    pygame.display.flip()
                    sleep(2)
                    sleep_count += 1
                    k -= 1
                    current_glass = randint(0, 1)

                    if k == 0:
                        connection = sqlite3.connect('data/db/time.db')
                        connection.cursor().execute('UPDATE levels SET time = ? WHERE id = 3', (int(time_playing),))
                        connection.commit()
                        connection.close()
                        pygame.quit()
                        hopscotch_pass.main()

                elif glasses[int(not current_glass)].collidepoint(mouse_position) and \
                        not god_mode:
                    death = pygame.transform.scale(
                        load_image('glass.png'),
                        (120, 140))
                    screen.blit(death, death_lst[not current_glass])
                    pygame.display.flip()
                    pygame.quit()
                    hopscotch_death.main()

        try:
            screen.blit(bg, (0, 0))
            glass1 = pygame.draw.rect(screen, pygame.Color(50, 239, 255), (270, 250, 120, 140))
            glass2 = pygame.draw.rect(screen, pygame.Color(50, 239, 255), (430, 250, 120, 140))
            glasses = [glass1, glass2]

            font = pygame.font.Font(None, 50)
            time_label = font.render(str(time_remaining), True, pygame.Color('white'))
            screen.blit(time_label, (40, 40))
            glasses_label = font.render(f'{k} glass(es) left.', True, pygame.Color('white'))
            screen.blit(glasses_label, (40, 80))

            clock.tick(fps)
            pygame.display.flip()
        except pygame.error:
            pass

    pygame.quit()

main()