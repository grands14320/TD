import Sprite
import Text
from buttons.Button import Button
from enums.CurrentScreen import CurrentScreen


class PlayAgainButton(Button):

    position: (int, int)
    size: (int, int) = (125, 25)

    def __init__(self, position: (int, int)):
        self.position = position
        super().__init__(Sprite.Sprite(self.size, self.position),
                         Text.Text((self.position[0] - 45, self.position[1] - 12), 22),
                         'Play Again?')

    def react(self):
        self.player_progress_state_service.set_current_screen(CurrentScreen.LEVEL)
        self.player_progress_state_service.restart_progress()

