import time

from Enemies import Enemy
from effects.BulletEffect import BulletEffect


class FreezingBulletEffect(BulletEffect):

    def __init__(self):
        self.applied_at = None
        self.duration = 1
        self.slow_ratio = 0.4

    def on_effect_expired(self, enemy):
        """
        Sets the enemy base speed as his current speed.
        """
        enemy.speed = enemy.base_speed

    def apply_effect(self, enemy: Enemy.Enemy):
        """
        slows down the enemy if the same effect wasn't previously applied
        """
        if self.applied_at is not None:
            return
        self.is_already_applied = True
        self.applied_at = time.perf_counter()
        enemy.speed = enemy.base_speed * self.slow_ratio

