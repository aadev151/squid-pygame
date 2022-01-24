import pygame
import sqlite3

from setup import width, height
from setup import load_image
from random import randint, choice
from time import time

import s_h_death
import s_h_pass


screen_rect = (0, 0, width, height)
all_sprites = pygame.sprite.Group()
GRAVITY = 5


class Particle(pygame.sprite.Sprite):
    # сгенерируем частицы разного размера
    fire = [load_image("star.png")]
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


k = 0
count = 1
COOKIES = ['cookie_circle1.png', 'cookie_star1.png']

COOKIES_CIRCLE = ['cookie_circle1.png', 'cookie_circle2.png',
                  'cookie_circle3.png',
                  'cookie_circle3.png', 'cookie_circle4.png',
                  'cookie_circle5.png', 'cookie_circle6.png',
                  'cookie_circle7.png', 'cookie_circle8.png',
                  'cookie_circle9.png', 'cookie_circle10.png']

COOKIES_STAR = ['cookie_star1.png', 'cookie_star2.png', 'cookie_star3.png',
                'cookie_star3.png', 'cookie_star4.png',
                'cookie_star5.png', 'cookie_star6.png',
                'cookie_star7.png', 'cookie_star8.png',
                'cookie_star9.png', 'cookie_star10.png', 'cookie_star11.png']

LETTERS = {97: 'A', 98: 'B', 99: 'C', 100: 'D', 101: 'E', 102: 'F', 103: 'G',
           104: 'H', 105: 'I', 106: 'J', 107: 'K', 108: 'L', 109: 'M', 110: 'N',
           111: 'O', 112: 'P', 113: 'Q', 114: 'R', 115: 'S', 116: 'T', 117: 'U',
           118: 'V', 119: 'W', 120: 'X', 121: 'Y', 122: 'Z'}


def new_letter(screen):
    key = randint(97, 122)
    x, y = randint(70, 600), randint(70, 400)
    while (x < 520 and x > 200 and y > 180 and y < 400) or (
            x > 400 and x < 470):
        x, y = randint(70, 600), randint(100, 400)
    font = pygame.font.Font(None, 120)
    text = font.render(
        LETTERS[key], True,
        (randint(30, 220), randint(30, 225), randint(30, 212)))
    place = text.get_rect(
        center=(x, y))
    screen.blit(text, place)
    return key, place, text


def new_cookie(screen, type):
    global k, count
    if count == 1:
        if type == 0:
            next_cookie = pygame.transform.scale(
                load_image(COOKIES_CIRCLE[k]),
                (200, 200))
        elif type == 1:
            next_cookie = pygame.transform.scale(
                load_image(COOKIES_STAR[k]),
                (200, 200))
        k += 1
        key, place, text = new_letter(screen)
        count = 0
    else:
        if type == 0:
            next_cookie = pygame.transform.scale(
                load_image(COOKIES_CIRCLE[k]),
                (200, 200))
        elif type == 1:
            next_cookie = pygame.transform.scale(
                load_image(COOKIES_STAR[k]),
                (200, 200))
        key, place, text = new_letter(screen)
        count += 1
    return key, place, text, next_cookie


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))
    pygame.display.set_caption('Sugar Honeycombs')

    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('s_h_bg.png'), (width, height))
    screen.blit(bg, (0, 0))
    type = randint(0, 1)

    next_cookie = pygame.transform.scale(load_image(COOKIES[type]),
                                         (200, 200))
    screen.blit(next_cookie, (300, 200))
    running = True

    fps = 50
    key, place, text = new_letter(screen)

    clock = pygame.time.Clock()
    start_time = time()

    while running:
        time_playing = time() - start_time
        time_remaining = int(21 - time_playing)

        if time_remaining == 0:
            running = False
            pygame.quit()
            s_h_death.main(message='Time left')
            break

        correct_tap = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if k == 10 and type == 0 or k == 11 and type == 1:
                    running = False
                    connection = sqlite3.connect('data/db/time.db')
                    connection.cursor().execute('UPDATE levels SET time = ? WHERE id = 1', (int(time_playing),))
                    connection.commit()
                    connection.close()
                    pygame.quit()
                    s_h_pass.main()
                    break

                if event.key == key:
                    key, place, text, next_cookie = new_cookie(screen, type)
                    correct_tap = True
                else:
                    running = False
                    pygame.quit()
                    s_h_death.main()
                    break
            if event.type == pygame.MOUSEBUTTONUP:

                if k == 10 and type == 0 or k == 11 and type == 1:
                    running = False
                    connection = sqlite3.connect('data/db/time.db')
                    connection.cursor().execute('UPDATE levels SET time = ? WHERE id = 1', (int(time_playing),))
                    connection.commit()
                    connection.close()
                    pygame.quit()
                    s_h_pass.main()
                    break

                mouse_position = pygame.mouse.get_pos()
                if place.collidepoint(mouse_position):
                    key, place, text, next_cookie = new_cookie(screen, type)
                    correct_tap = True
                else:
                    running = False
                    pygame.quit()
                    s_h_death.main()
                    break

            if correct_tap:
                create_particles(place.center)

        try:
            screen.blit(bg, (0, 0))
            screen.blit(next_cookie, (300, 200))
            screen.blit(text, place)
            font = pygame.font.Font(None, 60)
            time_label = font.render(str(time_remaining), True,
                                     pygame.Color('green'))
            screen.blit(time_label, (400, 30))

            all_sprites.update()
            all_sprites.draw(screen)

            clock.tick(fps)

            pygame.display.flip()
        except pygame.error:
            running = False
