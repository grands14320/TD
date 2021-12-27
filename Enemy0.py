import Enemy
import Sprite
from UnitVectors import UnitVectors


class Enemy0(Enemy.Enemy):

    def __init__(self, start_position):
        super().__init__(Sprite.Sprite((30, 30), start_position))
        self.__initialize()

    def __initialize(self):
        self.max_health = 10
        self.health = self.max_health
        self.speed = 7
        self.next_move = UnitVectors.UP
        self.previous_move = UnitVectors.UP
        self.gold_dropped = 5
        self.is_rotating = False
        self.sprite.set_transparent_texture("Enemies/Enemy-0.png")

    def clone(self):
        return Enemy0(self.sprite.get_position())
