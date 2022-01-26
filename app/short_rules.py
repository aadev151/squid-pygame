import pygame

from setup import width, height
from setup import button_color, button_hover_color
from setup import load_image

import rlgl_rules
import s_h_rules
import hopscotch_rules


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))

    pygame.display.set_caption('Rules')
    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('card.jpeg'), (width, height))
    screen.blit(bg, (0, 0))

    font = pygame.font.Font(None, 70)
    name = font.render("Rules", True, (237, 27, 118))
    screen.blit(name, ((width - name.get_width()) // 2, 40))

    font = pygame.font.Font(None, 30)
    label1 = font.render('So you\'re in huge debt.', True, pygame.Color('white'))
    label2 = font.render('You have received the card which has a phone number on its back.',
                         True, pygame.Color('white'))
    label3 = font.render('You have called the number, and the voice offered you to play a game.',
                         True, pygame.Color('white'))
    label4 = font.render('If you win, you\'ll have a prize of 45.6 billion won ($38m).',
                         True, pygame.Color('white'))
    label5 = font.render('So you immediately agree, and now have to play three games.',
                         True, pygame.Color('white'))
    label6 = font.render('If you fail at any of them, you\'ll be eliminated, meaning you\'ll have no',
                         True, pygame.Color('white'))
    label7 = font.render('chance of getting the prize.',
                         True, pygame.Color('white'))
    screen.blit(label1, (35, 130))
    screen.blit(label2, (35, 160))
    screen.blit(label3, (35, 190))
    screen.blit(label4, (35, 220))
    screen.blit(label5, (35, 250))
    screen.blit(label6, (35, 280))
    screen.blit(label7, (35, 310))

    start_button_color = button_color
    start_button = pygame.draw.rect(screen, start_button_color,
                                    pygame.Rect(300, 350, width - 600, 60), 0, 25)
    start_label = font.render("Start", True, pygame.Color('white'))
    screen.blit(start_label, (300 + (start_button.width - start_label.get_width()) // 2,
                              350 + (60 - start_label.get_height()) // 2))

    fps = 10
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEMOTION:
                mouse_position = pygame.mouse.get_pos()

                if start_button.collidepoint(mouse_position):
                    start_button_color = button_hover_color
                else:
                    start_button_color = button_color
                start_button = pygame.draw.rect(screen, start_button_color,
                                                pygame.Rect(300, 350, width - 600, 60), 0, 25)
                screen.blit(start_label, (300 + (start_button.width - start_label.get_width()) // 2,
                                          350 + (60 - start_label.get_height()) // 2))

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_position):
                    pygame.quit()
                    levels = {
                        '': rlgl_rules,
                        '1': rlgl_rules,
                        '2': s_h_rules,
                        '3': hopscotch_rules
                    }
                    with open('data/db/last.txt') as last_file:
                        levels[last_file.read()].main()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()