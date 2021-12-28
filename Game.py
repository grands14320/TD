import pygame

import Level0
import Time
from EventsStateService import EventStateService
from GameOver import GameOver
from Utility import Tools


class Game:
    current_level = 0
    levels = []
    time = Time.Time()
    event_state_service: EventStateService = EventStateService()

    def __init__(self):
        pygame.init()
        config = Tools.get_config()
        self.HEIGHT = int(config['window']['HEIGHT'])
        self.WIDTH = int(config['window']['WIDTH'])
        self.FPS = int(config['window']['fps'])
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        self.levels.append(Level0.Level0())
        pygame.display.set_caption('TEDE')
        self.running = True
        self.game_over = GameOver()

    def run(self):
        while self.running:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            if not self.levels[self.current_level].is_game_over:
                self.levels[self.current_level].update(self.window)
            else:
                self.game_over.draw(self.window)
            self.time.update()
            pygame.display.flip()
            self.check_events()
        pygame.quit()

    def check_events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            self.event_state_service.set_events(events)
