import Enemy
import Sprite
from enums.UnitVectors import UnitVectors


class Enemy3(Enemy.Enemy):

    def __init__(self, start_position):
        super().__init__(Sprite.Sprite((40, 40), start_position))
        self.__initialize()

    def __initialize(self):
        self.max_health = 30
        self.health = self.max_health
        self.speed = 13
        self.next_move = UnitVectors.UP
        self.previous_move = UnitVectors.UP
        self.gold_dropped = 10
        self.is_rotating = True
        self.sprite.set_transparent_texture("Enemies/Enemy-3.png")

    def clone(self):
        return Enemy3(self.sprite.get_position())
