from typing import List

import pygame

from utils import Sprite
from Towers import Tower
from DetailsStateService import DetailsStateService
from EventsStateService import EventStateService
from PlayerProgressStateService import PlayerProgressStateService
from Towers.Tower0 import Tower0
from Towers.Tower1 import Tower1
from Towers.Tower2 import Tower2
from Towers.Tower3 import Tower3
from Towers.Tower4 import Tower4
from TowersStateService import TowersStateService


class Structures:

    details_state_service: DetailsStateService = DetailsStateService()
    event_state_service: EventStateService = EventStateService()
    towers_state_service: TowersStateService = TowersStateService()
    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self, position: (int, int)):
        self.position = position
        self.sprite = Sprite.Sprite((200, 200), self.position)
        self.sprite.set_fill_color((232, 121, 111))
        self.structures = [Tower0((825, 175)),
                           Tower1((875, 175)),
                           Tower2((925, 175)),
                           Tower3((975, 175)),
                           Tower4((825, 225))]

    def get_structures(self) -> List[Tower.Tower]:
        return self.structures

    def update(self) -> None:
        for event in self.event_state_service.get_events():
            for structure in self.structures:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if structure.sprite.contains(event.pos):
                        if structure.get_price() <= self.player_progress_state_service.get_money():
                            self.towers_state_service.set_clicked_structure(type(structure))

    def draw(self, window) -> None:
        self.sprite.draw(window)
        for structure in self.structures:
            # indicates selected tower
            if self.towers_state_service.get_clicked_structure() == type(structure):
                pygame.draw.rect(window, (0, 255, 0), (structure.position[0] - 25, structure.position[1] - 25, 50, 50))
            structure.draw(window)

