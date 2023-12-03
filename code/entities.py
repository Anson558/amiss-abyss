import pygame
from tools import *

class Entity():
    def __init__(self, main, pos : Vector2):
        self.main = main
        self.anims = {
            'idle': Animation(load_cut_image('enemies/monster.png'), 12),
        }
        self.current_anim = self.anims['idle']
        self.flip = False
        self.size = Vector2(8, 16)
        self.rect = pygame.FRect(pos.x, pos.y, self.size.x, self.size.y)
        self.default_position = self.rect.topleft
        self.velocity = Vector2(0, 0)
        self.gravity = 0.15
        self.grounded = False
        self.show_hitbox = False

    def update(self):
        self.die()
        self.move_and_collide()

    def draw(self, display : pygame.Surface):
        self.animate()
        display.blit(pygame.transform.flip(self.current_anim.image, self.flip, False), (self.rect.centerx - self.current_anim.image.get_width()/2, self.rect.bottom - self.current_anim.image.get_height()) - self.main.scroll)
        if self.show_hitbox:
            pygame.draw.rect(display, pygame.Color(255, 171, 190), self.rect - self.main.scroll)

    def move_and_collide(self):
        self.grounded = False
        self.velocity.y += self.gravity
        self.rect.y += self.velocity.y
        for tile in self.main.tiles['terrain']:
            if self.rect.colliderect(tile.rect):
                if self.velocity.y > 0:
                    self.rect.bottom = tile.rect.top
                    self.velocity.y = 0
                    self.grounded = True
                elif self.velocity.y < 0:
                    self.rect.top = tile.rect.bottom

        self.rect.x += self.velocity.x
        for tile in self.main.tiles['terrain']:
            if self.rect.colliderect(tile):
                if self.velocity.x > 0:
                    self.rect.right = tile.rect.left
                elif self.velocity.x < 0:
                    self.rect.left = tile.rect.right

    def die(self):
        pass

    def animate(self):
        for anim in self.anims:
            self.anims[anim].play()
