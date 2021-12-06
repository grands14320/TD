import Game


class Bullet:
    def __init__(self, bullet_sprite, vector_move, speed):
        self.vector_move = vector_move
        self.sprite = bullet_sprite
        self.speed = speed

    def get_sprite(self):
        return self.sprite

    def update(self):
        self.sprite.move((self.vector_move[0] * self.speed * Game.Game.time.deltaTime,
                          self.vector_move[1] * self.speed * Game.Game.time.deltaTime))

    def draw(self, window):
        self.sprite.draw(window)