import pygame

import Sprite
import Tower


class Tower0(Tower.Tower):
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.sprite = Sprite.Sprite((40, 40), position)
        self.sprite.set_texture("Towers/Tower0.png")
        self.range = 200
        self.circle_range = pygame.Surface((self.range * 2, self.range * 2))
        self.circle_range.set_colorkey((0, 0, 0))
        self.circle_range.set_alpha(100)
        pygame.draw.circle(self.circle_range, (218, 161, 6), (self.range, self.range), self.range)
        self.bullet_speed = 100
        self.cooldown = 0.5
        self.damage = 2
        self.time_last_shoot = 0
        self.kills = 0
        self.rotatable = True
