import pygame
from entities import Entity
from tools import *

class Player(Entity):
    def __init__(self, main, pos: Vector2):
        super().__init__(main, pos)
        self.size = Vector2(9, 13)
        self.anims = {
            'idle': Animation(load_cut_image('player/idle.png'), 12),
            'run': Animation(load_cut_image('player/run.png'), 10),
            'jump': Animation(load_cut_image('player/jump.png'), 1),
            'fall': Animation(load_cut_image('player/fall.png'), 1)
        }
        self.current_anim = self.anims['idle']
        self.rect = pygame.FRect(pos.x, pos.y, self.size.x, self.size.y)
        self.hurtboxes = [self.main.tiles['spikes'], self.main.tiles['registers'], self.main.tiles['monsters'], self.main.tiles['bullets']]
        self.speed = 1.5
        self.jump_height = -4

    def update(self):
        super().update()
        self.move()

    def move(self):
        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_d]:
            self.velocity.x = self.speed
        elif keys[pygame.K_a]:
            self.velocity.x = -self.speed
        else:
            self.velocity.x = 0

        if self.grounded:
            if keys[pygame.K_w]:
                self.velocity.y = self.jump_height

    def animate(self):
        super().animate()
        if self.velocity.x > 0:
            if self.grounded:
                self.current_anim = self.anims['run']
            self.flip = False
        elif self.velocity.x < 0:
            if self.grounded:
                self.current_anim = self.anims['run']
            self.flip = True
        elif self.velocity.x == 0:
            if self.grounded:
                self.current_anim = self.anims['idle']
            
        if self.velocity.y > self.gravity + 1:
            self.current_anim = self.anims['fall']
        if self.velocity.y < 0:
            self.current_anim = self.anims['jump']
    
    def die(self):
        for types in self.hurtboxes:
            for tile in types:
                if self.rect.colliderect(tile.rect):
                    self.rect.topleft = self.default_position
        if (self.rect.y > 500):
            self.rect.topleft = self.default_position
