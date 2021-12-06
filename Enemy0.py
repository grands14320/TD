import Enemy
import Sprite


class Enemy0(Enemy.Enemy):
    def __init__(self, start_position):
        super().__init__()
        self.max_health = 10
        self.health = self.max_health
        self.speed = 7
        self.sprite = Sprite.Sprite((30, 30), start_position)
        self.next_move = self.Direction.UP
        self.previous_move = self.Direction.UP
        self.gold_dropped = 5
        self.sprite.set_fill_color((50, 50, 20))

    def clone(self):
        return Enemy0(self.sprite.get_position())
