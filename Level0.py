import Level
import Sprite
import Tower0
import Tower1
import Tower2


class Level0(Level.Level):
    size_of_tile = (50, 50)

    def __init__(self):
        super().__init__()
        self.map = self.get_map(0)
        self.map_size = (15, 11)
        self.quantity_kind_of_tiles = 3
        self.tiles = [Sprite.Sprite(self.size_of_tile) for i in range(self.quantity_kind_of_tiles)]
        self.tiles[0].set_fill_color((10, 159, 85))
        self.tiles[1].set_fill_color((10, 124, 48))
        self.tiles[2].set_fill_color((103, 110, 110))

        self.enemy_start_position = (125, 625)
        self.enemy_finish_position = (175, -50)

        self.enemies = []
        self.towers = [Tower0.Tower0([225, 225]),
                       Tower1.Tower1([325, 225]),
                       Tower2.Tower2([425, 225])]