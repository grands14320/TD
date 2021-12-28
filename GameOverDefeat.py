from Text import Text
from buttons.PlayAgainButton import PlayAgainButton


class GameOverDefeat:
    game_over_text: Text
    position: (int, int)

    def __init__(self):
        self.position = (425, 250)
        self.game_over_text = Text((self.position[0], self.position[1]), 30, (255, 255, 255))
        self.game_over_text.set_string('Game Over')
        self.play_again_button = PlayAgainButton((self.position[0] + 65, self.position[1] + 100))

    def draw(self, window):
        window.fill((0, 0, 0))
        self.game_over_text.draw(window)
        self.play_again_button.draw(window)
