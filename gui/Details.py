from utils import Text, Sprite
from DetailsStateService import DetailsStateService
from PlayerProgressStateService import PlayerProgressStateService


class Details:

    details_state_service: DetailsStateService = DetailsStateService()
    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self, position):
        self.position = position
        self.sprite = Sprite.Sprite((200, 250), self.position)
        self.sprite.set_fill_color((123, 123, 123))
        self.range = Text.Text()
        self.cooldown = Text.Text()
        self.damage = Text.Text()
        self.kills = Text.Text()
        self.price = Text.Text()
        self.set_details_position()
        self.active = False

    def update(self):
        self.active = self.details_state_service.is_active()
        if self.active:
            tower = self.details_state_service.get_active_tower()
            self.range.set_string("Range: " + str(tower.get_range()))
            self.damage.set_string("Damage: " + str(tower.get_damage()))
            self.cooldown.set_string("Cooldown: " + str(tower.get_cooldown()) + "s")
            self.kills.set_string("Kills: " + str(tower.get_kills()))
            self.price.set_string("Price: " + str(tower.get_price()))
            if self.player_progress_state_service.get_money() < tower.get_price():
                self.price.set_color((255, 0, 0))
            else:
                self.price.set_color((0, 0, 0))

    def set_details_position(self):
        position = self.sprite.get_global_bounds()
        self.damage.set_position((position[0], position[1] + 10))
        self.range.set_position((position[0], position[1] + 50))
        self.cooldown.set_position((position[0], position[1] + 90))
        self.kills.set_position((position[0], position[1] + 130))
        self.price.set_position((position[0], position[1] + 170))

    def draw(self, window):
        self.sprite.draw(window)
        if self.active:
            self.damage.draw(window)
            self.range.draw(window)
            self.cooldown.draw(window)
            self.kills.draw(window)
            self.price.draw(window)
