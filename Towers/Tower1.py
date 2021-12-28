# shots 4 bullets at 4 directions at once

import pygame

import Bullet
from utils import Sprite
from Towers.Tower import Tower


class Tower1(Tower):

    shot_range = 80
    bullet_speed = 15
    cooldown = 0.2
    damage = 3.5
    last_shot_time = 0
    kills = 0
    is_rotatable = False
    texture = "Towers/assets/Tower1.png"
    price = 25

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.sprite = Sprite.Sprite((50, 50), position)
        self.sprite.set_transparent_texture(self.texture)
        self.circle_range = pygame.Surface((self.shot_range * 2, self.shot_range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.shot_range, self.shot_range), self.shot_range)

    def shoot_to_target(self, target):
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (1, 0), self.bullet_speed))
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (-1, 0), self.bullet_speed))
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (0, 1), self.bullet_speed))
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (0, -1), self.bullet_speed))
