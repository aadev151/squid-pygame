import pygame
from time import time, sleep
import sqlite3

from setup import size, width, height
from setup import load_image

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
        def __init__(self, sheet, columns, rows, x):
            super().__init__(all_sprites)
            self.frames = []
            self.cut_sheet(sheet, columns, rows)
            self.cur_frame = 0
            self.image = self.frames[self.cur_frame]
            self.x = x
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect().move(x, 300)

        def cut_sheet(self, sheet, columns, rows):
            self.rect = pygame.Rect(0, 0, sheet.get_width() // columns,
                                    sheet.get_height() // rows)
            for j in range(rows):
                for i in range(columns):
                    frame_location = (self.rect.w * i, self.rect.h * j)
                    self.frames.append(sheet.subsurface(pygame.Rect(
                        frame_location, self.rect.size)))

        def move(self, x):
            self.x = x
            self.rect = self.image.get_rect().move(x, 300)

        def update(self):
            self.cur_frame = (self.cur_frame + 1) % len(self.frames)
            self.image = self.frames[self.cur_frame]

    class FinishLine(pygame.sprite.Sprite):
        def __init__(self):
            super().__init__(finish_group, all_sprites)
            self.image = load_image('finish_line.png')
            self.mask = pygame.mask.from_surface(self.image)
            self.rect = self.image.get_rect().move(width - 150, 380)

    player = Player(load_image('player copy.png'), 2, 1, 20)
    finish = FinishLine()

    screen = pygame.display.set_mode((width, height))

    screen.blit(bg, (0, 0))

    screen.blit(doll_back, (width - 150, 100))
    green.play()

    transp_rect = pygame.Surface(size)
    transp_rect.set_alpha(0)
    transp_rect.fill((0, 0, 0))
    screen.blit(transp_rect, (0, 0))

    god_mode = False

    fps = 50
    clock = pygame.time.Clock()
    running = playing = True

    blink_event = pygame.USEREVENT + 1
    pygame.time.set_timer(blink_event, 2500)

    start_time = time()
    has_36, has_33, has_29, has_27, has_25, has_23, has_22, has_21, has_19, \
        has_17, has_15, has_11, has_10, has_9, has_7, has_5, has_4, has_2 = (False,) * 18

    pygame.key.set_repeat(10, 10)

    red_time = blink_time = death_time = None
    leave_the_game = False

    while running:
        time_playing = time() - start_time
        time_remaining = int(31 - time_playing)

        if leave_the_game and transp_rect.get_alpha() >= 190:
            pygame.quit()
            rlgl_death.main()

        elif playing:
            if blink_time and time() - blink_time >= 0.3:
                player.update()
                blink_time = None

            if time_remaining == 0:
                death_time = time()
                leave_the_game = True
                playing = False

            if time_playing >= 36 and not has_36:
                green_light()
                has_36 = True

            elif time_playing >= 33 and not has_33:
                red_light()
                red_time = time()
                has_33 = True

            elif time_playing >= 29 and not has_29:
                green_light()
                has_29 = True

            elif time_playing >= 27 and not has_27:
                red_light()
                red_time = time()
                has_27 = True

            elif time_playing >= 25 and not has_25:
                green_light()
                has_25 = True

            elif time_playing >= 23 and not has_23:
                red_light()
                red_time = time()
                has_23 = True

            elif time_playing >= 22 and not has_22:
                green_light()
                has_22 = True

            elif time_playing >= 21 and not has_21:
                red_light()
                red_time = time()
                has_21 = True

            elif time_playing >= 19 and not has_19:
                green_light()
                has_19 = True

            elif time_playing >= 17 and not has_17:
                red_light()
                red_time = time()
                has_17 = True

            elif time_playing >= 15 and not has_15:
                green_light()
                has_15 = True

            elif time_playing >= 11 and not has_11:
                red_light()
                red_time = time()
                has_11 = True

            elif time_playing >= 10 and not has_10:
                green_light()
                has_10 = True

            elif time_playing >= 9 and not has_9:
                red_light()
                red_time = time()
                has_9 = True

            elif time_playing >= 7 and not has_7:
                green_light()
                has_7 = True

            elif time_playing >= 5 and not has_5:
                red_light()
                red_time = time()
                has_5 = True

            elif time_playing >= 4 and not has_4:
                green_light()
                has_4 = True

            elif time_playing >= 2 and not has_2:
                red_light()
                red_time = time()
                has_2 = True

            if pygame.sprite.collide_mask(player, finish):
                connection = sqlite3.connect('data/db/time.db')
                connection.cursor().execute('UPDATE levels SET time = ? WHERE id = 1', (int(time_playing),))
                connection.commit()
                connection.close()
                pygame.quit()
                rlgl_pass.main()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == blink_event:
                    player.update()
                    blink_time = time()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        player.move(player.x + 1)
                    if event.mod == pygame.KMOD_CAPS:
                        god_mode = True

                    if event.key == pygame.K_RIGHT and is_red and time() - red_time >= 0.5 and \
                            not god_mode:
                        death_time = time()
                        leave_the_game = True
                        playing = False

            screen.blit(bg, (0, 0))
            if is_red and time() - red_time >= 0.5:
                screen.blit(doll_front, (width - 150, 100))
            else:
                screen.blit(doll_back, (width - 150, 100))

            screen.blit(player.image, player.rect)
            screen.blit(finish.image, finish.rect)

            font = pygame.font.Font(None, 50)
            time_label = font.render(str(time_remaining), True, pygame.Color('black'))
            screen.blit(time_label, (40, 40))

        if leave_the_game:
            transp_rect.set_alpha(0 + int(40 * (time() - death_time)))
            screen.blit(transp_rect, (0, 0))

        clock.tick(fps)
        pygame.display.flip()

    pygame.quit()
