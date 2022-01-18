import pygame
from setup import width, height
from setup import button_color, button_hover_color
from setup import load_image
from random import choice, randint
from time import time
import s_h_death

COOKIES = ['cookie_circle1.png', 'cookie_star1.png', 'cookie_triange1.png']

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
    while x < 500 and x > 100 and y > 100 and y < 500:
        x, y = randint(70, 600), randint(70, 400)
    font = pygame.font.Font(None, 170)
    text = font.render(
        LETTERS[key], True,
        (randint(30, 220), randint(30, 225), randint(30, 212)))
    place = text.get_rect(
        center=(x, y))
    screen.blit(text, place)
    return key


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))
    pygame.display.set_caption('Sugar honeycombs')

    screen = pygame.display.set_mode((width, height))

    bg = pygame.transform.scale(load_image('s_h_bg.png'), (width, height))
    screen.blit(bg, (0, 0))
    type = randint(0, 1)

    cookie = pygame.transform.scale(load_image(COOKIES[type]),
                                    (200, 200))
    k = 0
    screen.blit(cookie, (300, 200))
    running = True

    fps = 50
    clock = pygame.time.Clock()
    count = 1
    key = new_letter(screen)

    all_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == key:
                    if count == 1:
                        if type == 0:
                            next_cookie = pygame.transform.scale(
                                load_image(COOKIES_CIRCLE[k]),
                                (200, 200))
                        elif type == 1:
                            next_cookie = pygame.transform.scale(
                                load_image(COOKIES_STAR[k]),
                                (200, 200))
                        elif type == 2:
                            next_cookie = pygame.transform.scale(
                                load_image(COOKIES_STAR[k]),
                                (200, 200))
                        k += 1
                        screen.blit(bg, (0, 0))
                        screen.blit(next_cookie, (300, 200))
                        key = new_letter(screen)
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
                        elif type == 2:
                            next_cookie = pygame.transform.scale(
                                load_image(COOKIES_STAR[k]),
                                (200, 200))
                        screen.blit(bg, (0, 0))
                        screen.blit(next_cookie, (300, 200))
                        key = new_letter(screen)
                        count += 1

                else:
                    pygame.quit()
                    s_h_death.main()

        clock.tick(fps)

        pygame.display.flip()


if __name__ == "__main__":
    main()
