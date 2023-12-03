import pygame
from tools import Vector2
from entities import Entity
from tools import *
from bullet import Bullet

class StationaryEnemy(Entity):
    def __init__(self, main, pos: Vector2):
        super().__init__(main, pos)
        self.size = Vector2(9, 13)
        self.anims = {
            'idle': Animation(load_cut_image('enemies/register.png'), 7),
        }
        self.current_anim = self.anims['idle']
        self.rect = pygame.FRect(pos.x, pos.y, self.size.x, self.size.y)

class Monster(StationaryEnemy):
    def __init__(self, main, pos: Vector2):
        super().__init__(main, pos)
        self.size = Vector2(8, 16)
        self.anims = {
            'idle': Animation(load_cut_image('enemies/monster.png'), 10)
        }
        self.current_anim = self.anims['idle']
        self.rect = pygame.FRect(pos.x, pos.y, self.size.x, self.size.y)
        self.velocity.x = -1

    def update(self):
        super().update()
        self.move()

    def move(self):
        for tile in self.main.tiles['enemy_walls']:
            if self.rect.colliderect(tile.rect):
                self.time_since_switch = 0
                self.velocity.x *= -1

class Register(StationaryEnemy):
    def __init__(self, main, pos: Vector2):
        super().__init__(main, pos)
        self.bullet_direction = Vector2(1, 0)
        self.shoot_cooldown = 60
        self.time_since_shot = 0

    def update(self):
        super().update()
        self.shoot()

    def shoot(self):
        self.time_since_shot += 1
        if self.time_since_shot > self.shoot_cooldown:
            bullet_instance = Bullet(self.main, Vector2(self.rect.x, self.rect.y))
            self.bullet_direction.x *= -1
            bullet_instance.velocity = self.bullet_direction * bullet_instance.speed
            self.main.tiles['bullets'].append(bullet_instance)
            self.time_since_shot = 0
