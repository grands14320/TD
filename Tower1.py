import pygame

import Bullet
import Sprite
import Tower


class Tower1(Tower.Tower):

    shot_range = 100
    bullet_speed = 50
    cooldown = 0.5
    damage = 2
    last_shot_time = 0
    kills = 0
    is_rotatable = False
    texture = "Towers/Tower0.png"

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
