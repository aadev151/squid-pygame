import pygame

from setup import width, height
from setup import button_color, button_hover_color
from setup import load_image

import hopscotch


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))

    pygame.mixer.music.load('data/rules.mp3')
    pygame.mixer.music.play(-1)

    pygame.display.set_caption('Squid Pygame - Game #3')
    screen = pygame.display.set_mode((width, height))

    screen.fill(pygame.Color('black'))

    font = pygame.font.Font(None, 70)
    name = font.render("Hopscotch", True, (237, 27, 118))
    screen.blit(name, ((width - name.get_width()) // 2, 40))

    font = pygame.font.Font(None, 30)
    label1 = font.render('You will be playing Hopscotch.', True, pygame.Color('white'))
    label2 = font.render('You will see two sheets of glass.', True, pygame.Color('white'))
    label3 = font.render('One of them is click-proof, and the other one is fake.',
                         True, pygame.Color('white'))
    label4 = font.render('You will have to click on the correct sheet of glass.',
                         True, pygame.Color('white'))
    label5 = font.render('You will have 20 seconds to play the game.',
                         True, pygame.Color('white'))
    screen.blit(label1, (65, 130))
    screen.blit(label2, (65, 160))
    screen.blit(label3, (65, 190))
    screen.blit(label4, (65, 220))
    screen.blit(label5, (65, 250))

    start_button_color = button_color
    start_button = pygame.draw.rect(screen, start_button_color,
                                    pygame.Rect(300, 310, width - 600, 60), 0, 25)
    start_label = font.render("Start", True, pygame.Color('white'))
    screen.blit(start_label, (300 + (start_button.width - start_label.get_width()) // 2,
                              310 + (60 - start_label.get_height()) // 2))

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
                                                pygame.Rect(300, 310, width - 600, 60), 0, 25)
                screen.blit(start_label, (300 + (start_button.width - start_label.get_width()) // 2,
                                          310 + (60 - start_label.get_height()) // 2))

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_position):
                    pygame.quit()
                    hopscotch.main()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
