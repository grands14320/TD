from typing import List

import pygame

import Sprite
import Tower
from DetailsStateService import DetailsStateService
from EventsStateService import EventStateService
from Tower0 import Tower0
from Tower1 import Tower1
from Tower2 import Tower2
from TowersStateService import TowersStateService


class Structures:

    details_state_service: DetailsStateService = DetailsStateService()
    event_state_service: EventStateService = EventStateService()
    towers_state_service: TowersStateService = TowersStateService()

    def __init__(self, position: (int, int)):
        self.position = position
        self.sprite = Sprite.Sprite((200, 200), self.position)
        self.sprite.set_fill_color((232, 121, 111))
        self.structures = [Tower0((825, 175)), Tower1((875, 175)), Tower2((925, 175))]

    def get_structures(self) -> List[Tower.Tower]:
        return self.structures

    def update(self):
        for event in self.event_state_service.get_events():
            for structure in self.structures:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if structure.sprite.contains(event.pos):
                        print('clicked ' + str(type(structure)))
                        self.towers_state_service.set_clicked_structure(type(structure))

    def draw(self, window):
        self.sprite.draw(window)
        for structure in self.structures:
            structure.draw(window)

