import pygame

from Bullet import Bullet
import Sprite
import Tower
from UnitVectors import UnitVectors


class Tower2(Tower.Tower):

    shot_range = 80
    bullet_speed = 50
    cooldown = 0.5
    damage = 3
    last_shot_time = 0
    kills = 0
    is_rotatable = False
    texture = "Towers/Tower0.png"
    price = 25

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.sprite = Sprite.Sprite((50, 50), position)
        self.sprite.set_transparent_texture("Towers/Tower0.png")
        self.circle_range = pygame.Surface((self.shot_range * 2, self.shot_range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.shot_range, self.shot_range), self.shot_range)

    def shoot_to_target(self, target):
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.RIGHT, self.bullet_speed))
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.LEFT, self.bullet_speed))
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.DOWN, self.bullet_speed))
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.UP, self.bullet_speed))

            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.RIGHT_DOWN, self.bullet_speed))
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.RIGHT_UP, self.bullet_speed))
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.LEFT_UP, self.bullet_speed))
            self.bullets.append(Bullet(Sprite.Sprite((10, 10), self.position), UnitVectors.LEFT_DOWN, self.bullet_speed))

