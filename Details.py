import Sprite
import Text


class Details:
    def __init__(self, position):
        self.position = position
        self.sprite = Sprite.Sprite((200, 250), self.position)
        self.sprite.set_fill_color((123, 123, 123))
        self.enabled = False
        self.range = Text.Text()
        self.cooldown = Text.Text()
        self.damage = Text.Text()
        self.kills = Text.Text()
        self.set_details_position()

    def get_enabled(self):
        return self.enabled

    def set_enabled(self, enabled, tower=""):
        self.enabled = enabled
        if self.enabled:
            self.range.set_string("Range: " + str(tower.get_range()))
            self.damage.set_string("Damage: " + str(tower.get_damage()))
            self.cooldown.set_string("Cooldown: " + str(tower.get_cooldown()) + "s")
            self.kills.set_string("Kills: " + str(tower.get_kills()))

    def set_details_position(self):
        position = self.sprite.get_global_bounds()
        self.damage.set_position((position[0] + 10, position[1] + 10))
        self.range.set_position((position[0] + 10, position[1] + 70))
        self.cooldown.set_position((position[0] + 10, position[1] + 130))
        self.kills.set_position((position[0] + 10, position[1] + 190))

    def show(self, window):
        self.sprite.draw(window)
        if self.enabled:
            self.damage.draw(window)
            self.range.draw(window)
            self.cooldown.draw(window)
            self.kills.draw(window)
