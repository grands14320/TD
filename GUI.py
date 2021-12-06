import pygame
import Details
import Progress


class GUI:
    def __init__(self):
        self.position = (900, 0)
        self.details = Details.Details((self.position[0], self.position[1] + 475))
        self.progress = Progress.Progress((900, 75))
        self.active_tower = ""

    def update(self, towers):
        self.details.set_enabled(False)
        for tower in towers:
            tower.active = False
            if tower.get_sprite().contains(pygame.mouse.get_pos()):
                tower.active = True
                self.active_tower = tower
                self.details.set_enabled(True, self.active_tower)

    def draw(self, window, hp, money, wave):
        self.details.show(window)
        self.progress.drawData(window, hp, money, wave)
