import pygame

import Level0
import Time
import time
from Utility import Tools


class Game:
    current_level = 0
    levels = [Level0.Level0()]
    time = Time.Time()

    def __init__(self):
        pygame.init()
        config = Tools.get_config()
        self.HEIGHT = int(config['window']['HEIGHT'])
        self.WIDTH = int(config['window']['WIDTH'])
        self.FPS = int(config['window']['fps'])
        self.window = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('TEDE')
        self.running = True

    def run(self):
        while self.running:
            clock = pygame.time.Clock()
            clock.tick(self.FPS)
            self.window.fill((0, 0, 0))
            self.levels[self.current_level].update(self.window)
            self.time.update()
            pygame.display.flip()
            self.check_events()
        pygame.quit()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False