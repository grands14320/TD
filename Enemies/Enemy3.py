from utils import Sprite
from Enemies.Enemy import Enemy
from enums.UnitVectors import UnitVectors


class Enemy3(Enemy):

    def __init__(self, start_position):
        super().__init__(Sprite.Sprite((40, 40), start_position))
        self.__initialize()

    def __initialize(self):
        self.base_health = 35
        self.health = self.base_health
        self.base_speed = 15
        self.speed = self.base_speed
        self.next_move = UnitVectors.UP
        self.previous_move = UnitVectors.UP
        self.gold_dropped = 5
        self.is_rotating = True
        self.sprite.set_transparent_texture("Enemies/assets/Enemy-3.png")

    def clone(self):
        return Enemy3(self.sprite.get_position())
