# Sniper long range tower

import pygame

from utils import Sprite
from Towers.Tower import Tower


class Tower2(Tower):

    shot_range = 180
    bullet_speed = 100
    cooldown = 0.8
    damage = 11
    last_shot_time = 0
    kills = 0
    is_rotatable = True
    texture = "Towers/assets/Tower2.png"
    price = 65

    def __init__(self, position):
        super().__init__()
        self.position = position
        self.sprite = Sprite.Sprite((50, 50), position)
        self.sprite.set_transparent_texture(self.texture)
        self.circle_range = pygame.Surface((self.shot_range * 2, self.shot_range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.shot_range, self.shot_range), self.shot_range)

