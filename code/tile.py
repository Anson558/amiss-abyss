import pygame
from tools import *

class Tile():
    def __init__(self, main, pos : Vector2, image : pygame.Surface):
        self.main = main
        self.image = image
        offset = Vector2(-(self.image.get_width() - 16), -(self.image.get_height() - 16))
        self.default_position = pos
        self.rect = pygame.FRect(self.default_position.x + offset.x, self.default_position.y + offset.y, self.image.get_width(), self.image.get_height())
        self.show_hitbox = False

    def draw(self, display : pygame.Surface):
        display.blit(self.image, self.rect.topleft - self.main.scroll)
        if self.show_hitbox:
            pygame.draw.rect(display, pygame.Color(255, 171, 190), self.rect - self.main.scroll)

    def update(self):
        pass