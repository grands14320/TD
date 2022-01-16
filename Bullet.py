import Game


class Bullet:
    """
    Class representing bullet object.
    """

    def __init__(self, bullet_sprite, vector_move, speed, effects=None):
        if effects is None:
            effects = []
        self.vector_move = vector_move
        self.sprite = bullet_sprite
        self.sprite.set_transparent_texture("assets/bullet.png")
        self.speed = speed
        self.effects = effects

    def get_sprite(self):
        return self.sprite

    def update(self):
        """
        Moves the bullet.
        """
        self.sprite.move((self.vector_move[0] * self.speed * Game.Game.time.deltaTime,
                          self.vector_move[1] * self.speed * Game.Game.time.deltaTime))

    def draw(self, window):
        self.sprite.draw(window)
