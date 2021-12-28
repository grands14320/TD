from utils import Text, Sprite
from buttons.Button import Button


class StartStopButton(Button):

    position: (int, int)
    size: (int, int) = (75, 25)

    def __init__(self, position: (int, int)):
        self.position = position
        super().__init__(Sprite.Sprite(self.size, self.position),
                         Text.Text((self.position[0] - 18, self.position[1] - 12), 22),
                         'Start')

    def react(self):
        self.player_progress_state_service.set_is_wave_ongoing(True)
