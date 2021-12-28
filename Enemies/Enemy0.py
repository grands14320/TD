from utils import Sprite
from Enemies.Enemy import Enemy
from enums.UnitVectors import UnitVectors


class Enemy0(Enemy):

    def __init__(self, start_position):
        super().__init__(Sprite.Sprite((40, 40), start_position))
        self.__initialize()

    def __initialize(self):
        self.base_health = 10
        self.health = self.base_health
        self.base_speed = 7
        self.speed = self.base_speed
        self.next_move = UnitVectors.UP
        self.previous_move = UnitVectors.UP
        self.gold_dropped = 2
        self.is_rotating = False
        self.sprite.set_transparent_texture("Enemies/assets/Enemy-0.png")

    def clone(self):
        return Enemy0(self.sprite.get_position())
