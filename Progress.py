import Sprite
import Text
from PlayerProgressStateService import PlayerProgressStateService
from StartStopButton import StartStopButton


class Progress:

    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self, position):
        self.position = position
        self.start_stop_button = StartStopButton((self.position[0], self.position[1] + 50))
        self.sprite = Sprite.Sprite((200, 150), self.position)
        self.sprite.set_fill_color((123, 170, 123))
        self.players_health = Text.Text((position[0] - 100, position[1] - 75), 22)
        self.raised_money = Text.Text((position[0] - 100, position[1] - 40), 22)
        self.current_wave = Text.Text((position[0] - 100, position[1] - 5), 22)

    def draw(self, window):
        self.sprite.draw(window)
        self.start_stop_button.draw(window)
        self.players_health.set_string("HEALTH: " + str(self.player_progress_state_service.get_hp())).draw(window)
        self.raised_money.set_string("MONEY: " + str(self.player_progress_state_service.get_money())).draw(window)
        self.current_wave.set_string("WAVE: " + str(self.player_progress_state_service.get_current_wave_name())).draw(
            window)
