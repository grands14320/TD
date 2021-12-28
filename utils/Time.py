import pygame


class Time:

    def __init__(self):
        self.getTicksLastFrame = 0
        self.deltaTime = 1

    def update(self):
        t = pygame.time.get_ticks()
        self.deltaTime = (t - self.getTicksLastFrame) / 60.0
        self.getTicksLastFrame = t
