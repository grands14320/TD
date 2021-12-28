import pygame

import Sprite
import Text
from EventsStateService import EventStateService
from PlayerProgressStateService import PlayerProgressStateService


class StartStopButton:

    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()
    event_state_service: EventStateService = EventStateService()

    wave_start_stop_button: Sprite.Sprite
    wave_start_stop_text: Text.Text
    position: (int, int)
    size: (int, int) = (75, 25)

    def __init__(self, position: (int, int)):
        self.position = position
        self.wave_start_stop_button = Sprite.Sprite(self.size, self.position)
        self.wave_start_stop_text = Text.Text((self.position[0] - 18, self.position[1] - 12), 22)
        self.wave_start_stop_text.set_string('Start')

    def draw(self, window) -> None:
        mouse_pos = pygame.mouse.get_pos()

        if self.wave_start_stop_button.contains(mouse_pos):
            if not self.player_progress_state_service.get_is_wave_ongoing():
                self.wave_start_stop_button.set_fill_color(pygame.Color('white'))
                self.wave_start_stop_text.set_color(pygame.Color('black'))
                self.__check_start_stop_button_clicks()
        else:
            self.wave_start_stop_button.set_fill_color(pygame.Color('black'))
            self.wave_start_stop_text.set_color(pygame.Color('white'))

        self.wave_start_stop_button.draw(window)
        self.wave_start_stop_text.draw(window)

    def __check_start_stop_button_clicks(self) -> None:
        for event in self.event_state_service.get_events():
            # check left mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.player_progress_state_service.set_is_wave_ongoing(True)
