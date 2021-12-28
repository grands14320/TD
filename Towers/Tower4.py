# shot bullets that slow down enemies.

import pygame

from Towers.Tower import Tower
from Bullet import Bullet
from utils.Sprite import Sprite
from effects.FreezingBulletEffect import FreezingBulletEffect


class Tower4(Tower):

    shot_range = 100
    bullet_speed = 20
    cooldown = 0.2
    damage = 5
    last_shot_time = 0
    kills = 0
    is_rotatable = False
    texture = "Towers/assets/Tower4.png"
    price = 90

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.sprite = Sprite((50, 50), position)
        self.sprite.set_transparent_texture(self.texture)
        self.circle_range = pygame.Surface((self.shot_range * 2, self.shot_range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.shot_range, self.shot_range), self.shot_range)

    def shoot_to_target(self, target) -> None:
        vector: (float, float) = self.create_target_vector(target)
        bullet: Bullet = Bullet(Sprite((10, 10), self.sprite.get_position()),
                                vector,
                                self.bullet_speed,
                                effects=[FreezingBulletEffect()])
        self.bullets.append(bullet)
