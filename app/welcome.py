
import pygame

from setup import width, height
from setup import button_hover_color
from setup import load_image

import rules
import rlgl_rules
import s_h_rules
import hopscotch_rules


def main():
    button_color = (48, 141, 70)

    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))

    pygame.display.set_caption('Squid Pygame')
    screen = pygame.display.set_mode((width, height))

    image = load_image('welcome_bg.jpg')
    bg = pygame.transform.scale(image, (width, height))
    screen.blit(bg, (0, 0))

    font = pygame.font.Font(None, 70)
    name = font.render("Squid Pygame", True, pygame.Color('white'))
    screen.blit(name, ((width - name.get_width()) // 2, 40))

    font = pygame.font.Font(None, 50)
    start_button_color = button_color
    start_button = pygame.draw.rect(screen, start_button_color,
                                    pygame.Rect(150, 210, width - 300, 60), 0, 25)
    start_label = font.render("Start", True, pygame.Color('white'))
    screen.blit(start_label, (150 + (start_button.width - start_label.get_width()) // 2,
                              210 + (60 - start_label.get_height()) // 2))
    rules_button_color = button_color
    rules_button = pygame.draw.rect(screen, rules_button_color,
                                    pygame.Rect(150, 310, width - 300, 60), 0, 25)
    rules_label = font.render("Rules", True, pygame.Color('white'))
    screen.blit(rules_label, (150 + (rules_button.width - rules_label.get_width()) // 2,
                              310 + (60 - rules_label.get_height()) // 2))

    font = pygame.font.Font(None, 20)
    version_label = font.render("Version 0.1.1", True, pygame.Color('white'))
    screen.blit(version_label, (width - version_label.get_width() - 10,
                                height - version_label.get_height() - 10))

    font = pygame.font.Font(None, 25)
    credentials_label = font.render("Created by Alex Anisimov and Dasha Eremeeva",
                                    True, pygame.Color('white'))
    screen.blit(credentials_label, ((width - credentials_label.get_width()) // 2, height - 50))

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
                                                pygame.Rect(150, 210, width - 300, 60), 0, 25)
                screen.blit(start_label, (150 + (start_button.width - start_label.get_width()) // 2,
                                          210 + (60 - start_label.get_height()) // 2))

                if rules_button.collidepoint(mouse_position):
                    rules_button_color = button_hover_color
                else:
                    rules_button_color = button_color
                rules_button = pygame.draw.rect(screen, rules_button_color,
                                                pygame.Rect(150, 310, width - 300, 60), 0, 25)
                screen.blit(rules_label, (150 + (rules_button.width - rules_label.get_width()) // 2,
                                          310 + (60 - rules_label.get_height()) // 2))

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

                if rules_button.collidepoint(mouse_position):
                    pygame.quit()
                    rules.main()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
