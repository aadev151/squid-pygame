import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    if not os.path.isfile(fullname):
        print(f"Файл с изображением '{fullname}' не найден")
        return -1
    image = pygame.image.load(fullname)
    return image


size = width, height = 800, 600
button_color = (48, 141, 70)
button_hover_color = (255, 141, 70)
