import pygame

from setup import width, height
from setup import button_color, button_hover_color
from setup import load_image

import welcome


def main(message='You broke the cookie:('):
    with open('data/db/last.txt', 'w') as last_file:
        last_file.write('1')

    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))

    eliminated_sound = pygame.mixer.Sound('data/eliminated.mp3')
    eliminated_sound.set_volume(.1)
    eliminated_sound.play()

    pygame.display.set_caption(message)
    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('s_h_death.png'), (width, height))
    screen.blit(bg, (0, 0))

    font = pygame.font.Font(None, 70)
    name = font.render(message, True, (237, 27, 118))
    screen.blit(name, ((width - name.get_width()) // 2, 40))

    font = pygame.font.Font(None, 40)
    start_button_color = button_color
    start_button = pygame.draw.rect(screen, start_button_color,
                                    pygame.Rect(250, 110, width - 500, 60), 0, 25)
    start_label = font.render("Main Menu", True, pygame.Color('white'))
    screen.blit(start_label, (250 + (start_button.width - start_label.get_width()) // 2,
                              110 + (60 - start_label.get_height()) // 2))

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
                                                pygame.Rect(250, 110, width - 500, 60), 0, 25)
                screen.blit(start_label, (250 + (start_button.width - start_label.get_width()) // 2,
                                          110 + (60 - start_label.get_height()) // 2))

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_position):
                    pygame.quit()
                    welcome.main()

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
