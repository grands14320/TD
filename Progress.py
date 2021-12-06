import Text
import Sprite


class Progress:
    def __init__(self, position):
        self.position = position
        self.sprite = Sprite.Sprite((200, 150), self.position)
        self.sprite.set_fill_color((123, 170, 123))
        self._playersHealth = Text.Text().set_position((position[0] - 100, position[1] - 75))
        self._raisedMoney = Text.Text().set_position((position[0] - 100, position[1] - 20))
        self._currentWave = Text.Text().set_position((position[0] - 100, position[1] + 30))

    def drawData(self, window, hp, money, wave):
        self.sprite.draw(window)
        self._playersHealth.set_string("Health: " + str(hp)).draw(window)
        self._raisedMoney.set_string("Money: " + str(money)).draw(window)
        self._currentWave.set_string("Wave: " + str(wave)).draw(window)
