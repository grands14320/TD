from typing import List

import pygame.event

from Singleton import SingletonMeta


class EventStateService(metaclass=SingletonMeta):

    __events: List[pygame.event.Event] = []

    def set_events(self, events: List[pygame.event.Event]):
        self.__events = events

    def get_events(self):
        return self.__events
