import pygame
import Bullet
import Sprite
import Tower
from Utility import Tools


class Tower1(Tower.Tower):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.sprite = Sprite.Sprite((40, 40), position)
        self.sprite.set_texture("Towers/Tower0.png")
        self.range = 100
        self.circle_range = pygame.Surface((self.range * 2, self.range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.range, self.range), self.range)
        self.bullet_speed = 50
        self.cooldown = 0.5
        self.damage = 2
        self.time_last_shoot = 0
        self.kills = 0
        self.rotatable = False

    def shoot_to_target(self, target):
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (1, 0), self.bullet_speed))
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (-1, 0), self.bullet_speed))
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (0, 1), self.bullet_speed))
            self.bullets.append(Bullet.Bullet(Sprite.Sprite((10, 10), self.position), (0, -1), self.bullet_speed))
