import pygame

from setup import width, height
from setup import button_color, button_hover_color
from setup import load_image

from random import choice, randint
from time import time

import rlgl_death
import rlgl_pass


is_red = False


def main():
    pygame.init()

    pygame.display.set_icon(load_image('icon.png'))
    pygame.display.set_caption('Red Light, Green Light')

    bg = pygame.transform.scale(load_image('rlgl_bg.png'), (width, height))
    green = pygame.mixer.Sound('data/green_light.mp3')
    red = pygame.mixer.Sound('data/red_light.mp3')
    doll_front = pygame.transform.scale(load_image('doll_front.png'), (130, 293))
    doll_back = pygame.transform.scale(load_image('doll_back.png'), (130, 293))

    all_sprites = pygame.sprite.Group()
    player_group = pygame.sprite.Group()
    finish_group = pygame.sprite.Group()

    def green_light():
        global is_red
        screen.blit(bg, (0, 0))
        screen.blit(doll_back, (width - 150, 100))
        screen.blit(player.image, player.rect)
        green.play()
        is_red = False

    def red_light():
        global is_red
        screen.blit(bg, (0, 0))
        screen.blit(doll_front, (width - 150, 100))
        screen.blit(player.image, player.rect)
        red.play()
        is_red = True

    class Player(pygame.sprite.Sprite):
        def __init__(self, x):
            super().__init__(player_group, all_sprites)
            self.image = load_image('player.png')
            self.x = x
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect().move(x, 300)

        def update(self, x):
            self.x = x
            self.rect = self.image.get_rect().move(x, 300)

    class FinishLine(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__(finish_group, all_sprites)
            self.image = load_image('finish_line.png')
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect().move(width - 150, 380)

    player = Player(20)
    finish = FinishLine()

    screen = pygame.display.set_mode((width, height))

    screen.blit(bg, (0, 0))

    screen.blit(doll_back, (width - 150, 100))
    green.play()

    fps = 50
    clock = pygame.time.Clock()
    running = True

    start_time = time()
    has_29, has_27, has_25, has_23, has_22, has_21, has_19, \
        has_17, has_15, has_11, has_10, has_9, has_7, has_5, has_4, has_2 = (False,) * 16

    while running:
        time_playing = time() - start_time
        time_remaining = int(31 - time_playing)

        if time_remaining == 0:
            pygame.quit()
            rlgl_death.main()

        if time_playing >= 29 and not has_29:
            green_light()
            has_29 = True

        elif time_playing >= 27 and not has_27:
            red_light()
            has_27 = True

        elif time_playing >= 25 and not has_25:
            green_light()
            has_25 = True

        elif time_playing >= 23 and not has_23:
            red_light()
            has_23 = True

        elif time_playing >= 22 and not has_22:
            green_light()
            has_22 = True

        elif time_playing >= 21 and not has_21:
            red_light()
            has_21 = True

        elif time_playing >= 19 and not has_19:
            green_light()
            has_19 = True

        elif time_playing >= 17 and not has_17:
            red_light()
            has_17 = True

        elif time_playing >= 15 and not has_15:
            green_light()
            has_15 = True

        elif time_playing >= 11 and not has_11:
            red_light()
            has_11 = True

        elif time_playing >= 10 and not has_10:
            green_light()
            has_10 = True

        elif time_playing >= 9 and not has_9:
            red_light()
            has_9 = True

        elif time_playing >= 7 and not has_7:
            green_light()
            has_7 = True

        elif time_playing >= 5 and not has_5:
            red_light()
            has_5 = True

        elif time_playing >= 4 and not has_4:
            green_light()
            has_4 = True

        elif time_playing >= 2 and not has_2:
            red_light()
            has_2 = True

        if pygame.sprite.collide_mask(player, finish):
            pygame.quit()
            rlgl_pass.main()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.update(player.x + 10)

            if event.type == pygame.KEYUP and event.key == pygame.K_RIGHT and is_red:
                pygame.quit()
                rlgl_death.main()

        screen.blit(bg, (0, 0))
        if is_red:
            screen.blit(doll_front, (width - 150, 100))
        else:
            screen.blit(doll_back, (width - 150, 100))

        screen.blit(player.image, player.rect)
        screen.blit(finish.image, finish.rect)

        font = pygame.font.Font(None, 50)
        time_label = font.render(str(time_remaining), True, pygame.Color('black'))
        screen.blit(time_label, (40, 40))

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()        
