import pygame

import Sprite
import Tower


class Tower0(Tower.Tower):

    shot_range = 200
    bullet_speed = 100
    cooldown = 0.5
    damage = 2
    last_shot_time = 0
    kills = 0
    is_rotatable = True
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
