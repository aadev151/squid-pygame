import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        return -1
    image = pygame.image.load(fullname)
    return image


def cover(screen, color, label_coords, label_size):
    bg = pygame.Surface((label_size[0] + 20, label_size[1] + 20))
    bg.set_alpha(170)
    bg.fill(color)
    screen.blit(bg, (label_coords[0] - 10, label_coords[1] - 10))


size = width, height = 800, 600
button_color = (50, 116, 102)
button_hover_color = (244, 71, 134)
