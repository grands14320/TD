from abc import ABC, abstractmethod

import pygame

from EventsStateService import EventStateService
from PlayerProgressStateService import PlayerProgressStateService
from utils.Sprite import Sprite
from utils.Text import Text


class Button(ABC):

    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()
    event_state_service: EventStateService = EventStateService()

    wave_start_stop_button: Sprite
    wave_start_stop_text: Text

    def __init__(self, button: Sprite, text: Text, content: str):
        self.wave_start_stop_button = button
        self.wave_start_stop_text = text
        self.wave_start_stop_text.set_string(content)

    def draw(self, window):
        mouse_pos = pygame.mouse.get_pos()

        if self.wave_start_stop_button.contains(mouse_pos):
            self.wave_start_stop_button.set_fill_color(pygame.Color('white'))
            self.wave_start_stop_text.set_color(pygame.Color('black'))
            self.__check_click_events()
        else:
            self.wave_start_stop_button.set_fill_color(pygame.Color('black'))
            self.wave_start_stop_text.set_color(pygame.Color('white'))

        self.wave_start_stop_button.draw(window)
        self.wave_start_stop_text.draw(window)

    def __check_click_events(self):
        for event in self.event_state_service.get_events():
            # check left mouse button click
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.react()

    @abstractmethod
    def react(self):
        """
        Should contain logic which will be executed when the button is clicked.
        """
        raise NotImplementedError()
