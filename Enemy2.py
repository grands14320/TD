import Enemy
import Sprite
from enums.UnitVectors import UnitVectors


class Enemy2(Enemy.Enemy):

    def __init__(self, start_position):
        super().__init__(Sprite.Sprite((40, 40), start_position))
        self.__initialize()

    def __initialize(self):
        self.max_health = 20
        self.health = self.max_health
        self.speed = 10
        self.next_move = UnitVectors.UP
        self.previous_move = UnitVectors.UP
        self.gold_dropped = 7
        self.is_rotating = False
        self.sprite.set_transparent_texture("Enemies/Enemy-2.png")

    def clone(self):
        return Enemy2(self.sprite.get_position())
