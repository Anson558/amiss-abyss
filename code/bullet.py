import pygame
from tools import *
from entities import Entity
from tools import *

class Bullet(Entity):
    def __init__(self, main, pos: Vector2):
        super().__init__(main, pos)
        self.size = Vector2(4, 4)
        self.anims = {
            'idle': Animation(load_cut_image('bullet.png'), 12),
        }
        self.current_anim = self.anims['idle']
        self.rect = pygame.FRect(pos.x, pos.y, self.size.x, self.size.y)
        self.hurtboxes = [self.main.tiles['spikes'], self.main.tiles['terrain']]
        self.gravity = 0
        self.speed = 1.5

    def die(self):
        for types in self.hurtboxes:
            for tile in types:
                if self.rect.colliderect(tile.rect):
                    self.main.tiles['bullets'].remove(self)