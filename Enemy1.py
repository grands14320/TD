import Enemy
import Sprite


class Enemy1(Enemy.Enemy):
    def __init__(self, start_position):
        super().__init__()
        self.max_health = 10
        self.health = self.max_health
        self.speed = 10
        self.sprite = Sprite.Sprite((40, 40), start_position)
        self.next_move = self.Direction.UP
        self.previous_move = self.Direction.UP
        self.gold_dropped = 10
        self.sprite.set_fill_color((50, 50, 120))

    def clone(self):
        return Enemy1(self.sprite.get_position())
