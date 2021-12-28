import pygame
from gui import Details, Structures, Progress
from DetailsStateService import DetailsStateService


class Gui:

    details_state_service = DetailsStateService()

    def __init__(self):
        self.position = (900, 0)
        self.details = Details.Details((self.position[0], self.position[1] + 475))
        self.progress = Progress.Progress((900, 75))
        self.structures = Structures.Structures((900, 250))

    def update(self, towers):
        self.details_state_service.set_is_active(False)

        # update structures that have been already built
        for tower in towers:
            tower.active = False
            if tower.get_sprite().contains(pygame.mouse.get_pos()):
                tower.active = True
                self.details_state_service.set_is_active(True)
                self.details_state_service.set_active_tower(tower)

        # update cursor hover position over structures that can be built
        for tower in self.structures.get_structures():
            if tower.get_sprite().contains(pygame.mouse.get_pos()):
                self.details_state_service.set_is_active(True)
                self.details_state_service.set_active_tower(tower)

    def draw(self, window):
        self.progress.draw(window)
        self.structures.update()
        self.structures.draw(window)
        self.details.update()
        self.details.draw(window)

