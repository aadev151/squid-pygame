import pygame
from setup import width, height
from setup import load_image
from random import randint
from time import time
import s_h_death, s_h_pass

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
    pygame.display.set_caption('Sugar honeycombs')

    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('s_h_bg.png'), (width, height))
    screen.blit(bg, (0, 0))
    type = randint(0, 1)

    next_cookie = pygame.transform.scale(load_image(COOKIES[type]),
                                         (200, 200))
    screen.blit(next_cookie, (300, 200))
    running = True

    fps = 50
    clock = pygame.time.Clock()

    key, place, text = new_letter(screen)

    clock = pygame.time.Clock()
    start_time = time()

    while running:
        time_playing = time() - start_time
        time_remaining = int(20 - time_playing)

        if time_remaining == 0:
            running = False
            pygame.quit()
            s_h_death.main()
            break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if k == 10 and type == 0 or k == 11 and type == 1:
                    running = False
                    pygame.quit()
                    s_h_pass.main()
                    break

                if event.key == key:
                    key, place, text, next_cookie = new_cookie(screen, type)
                else:
                    running = False
                    pygame.quit()
                    s_h_death.main()
                    break
            if event.type == pygame.MOUSEBUTTONUP:

                if k == 10 and type == 0 or k == 11 and type == 1:
                    running = False
                    pygame.quit()
                    s_h_pass.main()
                    break

                mouse_position = pygame.mouse.get_pos()
                if place.collidepoint(mouse_position):
                    key, place, text, next_cookie = new_cookie(screen, type)
                else:
                    running = False
                    pygame.quit()
                    s_h_death.main()
                    break
        try:
            screen.blit(bg, (0, 0))
            screen.blit(next_cookie, (300, 200))
            screen.blit(text, place)
            font = pygame.font.Font(None, 60)
            time_label = font.render(str(time_remaining), True,
                                     pygame.Color('green'))
            screen.blit(time_label, (400, 30))

            clock.tick(fps)

            pygame.display.flip()
        except pygame.error:
            running = False


main()
