import Text
import Sprite
from PlayerProgressStateService import PlayerProgressStateService


class Progress:

    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self, position):
        self.position = position
        self.sprite = Sprite.Sprite((200, 150), self.position)
        self.sprite.set_fill_color((123, 170, 123))
        self.players_health = Text.Text().set_position((position[0] - 100, position[1] - 75))
        self.raised_money = Text.Text().set_position((position[0] - 100, position[1] - 40))
        self.current_wave = Text.Text().set_position((position[0] - 100, position[1] - 5))

    def draw(self, window):
        self.sprite.draw(window)
        self.players_health.set_string("Health: " + str(self.player_progress_state_service.get_hp())).draw(window)
        self.raised_money.set_string("Money: " + str(self.player_progress_state_service.get_money())).draw(window)
        self.current_wave.set_string("Wave: " + str(self.player_progress_state_service.get_current_wave_name())).draw(window)
