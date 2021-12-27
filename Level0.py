import Level
import Sprite


class Level0(Level.Level):
    def __init__(self):
        self.size_of_tile = (50, 50)
        self.enemy_start_position: (int, int) = (125, 625)
        self.enemy_finish_position: (int, int) = (175, -50)
        self.map_size: (int, int) = (15, 11)
        self.towers = []
        super().__init__(self.get_map(0), self.get_level_tiles())

    def get_level_tiles(self) -> [Sprite.Sprite]:
        types_of_tiles: int = 3
        tiles: [Sprite.Sprite] = [Sprite.Sprite(self.size_of_tile) for _ in range(types_of_tiles)]
        tiles[0].set_fill_color((10, 159, 85))
        tiles[1].set_fill_color((10, 124, 48))
        tiles[2].set_fill_color((103, 110, 110))
        return tiles
