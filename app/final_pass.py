import pygame
from random import choice
import csv
import sqlite3
import os
import easygui


from setup import width, height
from setup import button_color, button_hover_color
from setup import load_image

import welcome


screen_rect = (0, 0, width, height)
all_sprites = pygame.sprite.Group()
GRAVITY = 5


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("coin.png")]
    for scale in (25, 35, 50):
        fire.append(pygame.transform.scale(fire[0], (scale, scale)))

    def __init__(self, pos, dx, dy):
        super().__init__(all_sprites)
        self.image = choice(self.fire)
        self.rect = self.image.get_rect()

        # у каждой частицы своя скорость — это вектор
        self.velocity = [dx, dy]
        # и свои координаты
        self.rect.x, self.rect.y = pos

        # гравитация будет одинаковой (значение константы)
        self.gravity = GRAVITY

    def update(self):
        # применяем гравитационный эффект:
        # движение с ускорением под действием гравитации
        self.velocity[1] += self.gravity
        # перемещаем частицу
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
        # убиваем, если частица ушла за экран
        if not self.rect.colliderect(screen_rect):
            self.kill()


def create_particles(position):
    # количество создаваемых частиц
    particle_count = 20
    # возможные скорости
    numbers = range(-10, 16)
    for _ in range(particle_count):
        Particle(position, choice(numbers), choice(numbers))


def export():
    connection = sqlite3.connect('data/db/time.db')
    times = connection.cursor().execute('SELECT time FROM levels').fetchall()
    connection.close()

    os.chdir(os.path.expanduser('~') + '/Desktop')
    with open('SquidPygameRes.csv', 'w', newline='') as csvfile:
        writer = csv.writer(
            csvfile, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Level 1. Red Light, Green Light', 'Level 2. Sugar Honeycombs', 'Level 3. Hopscotch'])
        results = []
        for res in times:
            results.append(res[0])
        writer.writerow(results)

    easygui.msgbox("The results are saved onto your desktop", title="Saved")


def main():
    with open('data/db/last.txt', 'w') as last_file:
        last_file.write('1')

    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))

    pygame.display.set_caption('You passed')
    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('pass.jpg'), (width, height))
    screen.blit(bg, (0, 0))

    font = pygame.font.Font(None, 70)
    name = font.render("You passed", True, (237, 27, 118))
    screen.blit(name, ((width - name.get_width()) // 2, 40))

    font = pygame.font.Font(None, 40)
    info_label = font.render('Tap anywhere on the screen', True, pygame.Color('white'))
    screen.blit(info_label, ((width - info_label.get_width()) // 2, 100))

    start_button_color = button_color
    start_button = pygame.draw.rect(screen, start_button_color,
                                    pygame.Rect(250, 170, width - 500, 60), 0, 25)
    start_label = font.render("Main Menu", True, pygame.Color('white'))
    screen.blit(start_label, (250 + (start_button.width - start_label.get_width()) // 2,
                              170 + (60 - start_label.get_height()) // 2))

    or_label = font.render('or', True, pygame.Color('white'))
    screen.blit(or_label, ((width - or_label.get_width()) // 2, 250))

    export_button_color = button_color
    export_button = pygame.draw.rect(screen, export_button_color,
                                    pygame.Rect(150, 290, width - 300, 60), 0, 25)
    export_label = font.render("Export my results to CSV", True, pygame.Color('white'))
    screen.blit(export_label, (150 + (export_button.width - export_label.get_width()) // 2,
                               290 + (60 - export_label.get_height()) // 2))

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
                                                pygame.Rect(250, 170, width - 500, 60), 0, 25)
                screen.blit(start_label, (250 + (start_button.width - start_label.get_width()) // 2,
                                          170 + (60 - start_label.get_height()) // 2))

                if export_button.collidepoint(mouse_position):
                    export_button_color = button_hover_color
                else:
                    export_button_color = button_color

                export_button = pygame.draw.rect(screen, export_button_color,
                                                 pygame.Rect(150, 290, width - 300, 60), 0, 25)
                screen.blit(export_label, (150 + (export_button.width - export_label.get_width()) // 2,
                                           290 + (60 - export_label.get_height()) // 2))

            if event.type == pygame.MOUSEBUTTONUP:
                mouse_position = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_position):
                    pygame.quit()
                    welcome.main()
                elif export_button.collidepoint(mouse_position):
                    export()
                else:
                    create_particles(mouse_position)

        screen.blit(bg, (0, 0))
        screen.blit(name, ((width - name.get_width()) // 2, 40))
        screen.blit(info_label, ((width - info_label.get_width()) // 2, 100))

        start_button = pygame.draw.rect(screen, start_button_color,
                                        pygame.Rect(250, 170, width - 500, 60), 0, 25)
        screen.blit(start_label, (250 + (start_button.width - start_label.get_width()) // 2,
                                  170 + (60 - start_label.get_height()) // 2))

        screen.blit(or_label, ((width - or_label.get_width()) // 2, 250))

        export_button = pygame.draw.rect(screen, export_button_color,
                                         pygame.Rect(150, 290, width - 300, 60), 0, 25)
        screen.blit(export_label, (150 + (export_button.width - export_label.get_width()) // 2,
                                   290 + (60 - export_label.get_height()) // 2))

        all_sprites.update()
        all_sprites.draw(screen)

        clock.tick(fps)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
