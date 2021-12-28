from Enemies.Enemy import Enemy
from utils import Sprite
from enums.UnitVectors import UnitVectors


class Enemy2(Enemy):

    def __init__(self, start_position):
        super().__init__(Sprite.Sprite((40, 40), start_position))
        self.__initialize()

    def __initialize(self):
        self.base_health = 20
        self.health = self.base_health
        self.base_speed = 12
        self.speed = self.base_speed
        self.next_move = UnitVectors.UP
        self.previous_move = UnitVectors.UP
        self.gold_dropped = 4
        self.is_rotating = False
        self.sprite.set_transparent_texture("Enemies/assets/Enemy-2.png")

    def clone(self):
        return Enemy2(self.sprite.get_position())
