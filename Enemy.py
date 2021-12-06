import pygame

import Game
from Utility import Tools


class Enemy:
    class Direction:
        UP = [0, -1]
        DOWN = [0, 1]
        LEFT = [-1, 0]
        RIGHT = [1, 0]

    def __init__(self):
        self.distance_travelled = 0

    def __del__(self):
        print("dyntka")

    def get_distance_travelled(self):
        return self.distance_travelled

    def get_sprite(self):
        return self.sprite

    def get_health(self):
        return self.health

    def get_gold_dropped(self):
        return self.gold_dropped

    def move(self, map, map_size):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        x = int(self.sprite.get_position()[0] / size_of_tile[0])
        y = int(self.sprite.get_position()[1] / size_of_tile[1])

        moveOffset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

        if not self.is_on_center_tile(x, y, map_size):

            position_of_tile = (x * size_of_tile[0] + size_of_tile[0] / 2,
                                y * size_of_tile[1] + size_of_tile[1] / 2)

            length_from_tile_vector = [(position_of_tile[0] - self.sprite.get_position()[0]),
                                       (position_of_tile[1] - self.sprite.get_position()[1])]

            length_from_tile = Tools.get_length_point_to_point(position_of_tile, self.sprite.get_position())

            if abs(moveOffset[0]) > abs(length_from_tile) or abs(moveOffset[1]) > abs(length_from_tile):

                if not self.tile_is_behind(position_of_tile):
                    self.sprite.move(length_from_tile_vector)
                    self.distance_travelled += abs(length_from_tile_vector[0]) + abs(length_from_tile_vector[1])
                    self.set_direction(map, map_size)
                    moveOffset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

                    if moveOffset[0] != 0:
                        if moveOffset[0] > 0:
                            moveOffset[0] -= length_from_tile
                        else:
                            moveOffset[0] += length_from_tile
                    elif moveOffset[1] != 0:
                        if moveOffset[1] > 0:
                            moveOffset[1] -= length_from_tile
                        else:
                            moveOffset[1] += length_from_tile

        else:
            self.set_direction(map, map_size)
            moveOffset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

        moveOffset = [moveOffset[0], moveOffset[1] ]
        self.sprite.move(moveOffset)
        self.distance_travelled += abs(moveOffset[0]) + abs(moveOffset[1])
        # self.sprite.rotate(20)

    def set_direction(self, map, map_size):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        x = int(self.sprite.get_position()[0] / size_of_tile[0])
        y = int(self.sprite.get_position()[1] / size_of_tile[1])

        if x - 1 < 0 or x + 1 > map_size[0] or y - 1 < 0 or y + 1 > map_size[1]:
            return True

        if map[y + 1][x] == '3' and self.previous_move != Enemy.Direction.UP:  # down
            self.next_move = Enemy.Direction.DOWN
            self.previous_move = Enemy.Direction.DOWN
            return True

        if map[y - 1][x] == '3' and self.previous_move != Enemy.Direction.DOWN:  # up
            self.next_move = Enemy.Direction.UP
            self.previous_move = Enemy.Direction.UP
            return True

        if map[y][x + 1] == '3' and self.previous_move != Enemy.Direction.LEFT:  # right
            self.next_move = Enemy.Direction.RIGHT
            self.previous_move = Enemy.Direction.RIGHT
            return True

        if map[y][x - 1] == '3' and self.previous_move != Enemy.Direction.RIGHT:  # left
            self.next_move = Enemy.Direction.LEFT
            self.previous_move = Enemy.Direction.LEFT
            return True

    def is_on_center_tile(self, x, y, map_size):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        if x - 1 < 0 or x + 1 > map_size[0] or y - 1 < 0 or y + 1 > map_size[1]:
            return True

        return not (x * size_of_tile[0] + size_of_tile[0] / 2 != self.sprite.get_position()[0] or y * size_of_tile[1] +
                    size_of_tile[1] / 2 != self.sprite.get_position()[1])

    def arrived_to_finish(self, finish):
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        sprite_index_x = int(self.sprite.get_position()[0] / size_of_tile[0])
        sprite_index_y = int(self.sprite.get_position()[1] / size_of_tile[1])

        finish_index_x = int(finish[0] / size_of_tile[0])
        finish_index_y = int(finish[1] / size_of_tile[1])

        return sprite_index_x == finish_index_x and sprite_index_y == finish_index_y

    def tile_is_behind(self, position_of_tile):
        if position_of_tile[1] > self.sprite.get_position()[1] and self.next_move == Enemy.Direction.UP:
            return True
        if position_of_tile[1] < self.sprite.get_position()[1] and self.next_move == Enemy.Direction.DOWN:
            return True
        if position_of_tile[0] > self.sprite.get_position()[0] and self.next_move == Enemy.Direction.LEFT:
            return True
        if position_of_tile[0] < self.sprite.get_position()[0] and self.next_move == Enemy.Direction.RIGHT:
            return True
        return False

    def health_bar(self, window):
        position = self.sprite.get_global_bounds()

        x = position[0]
        y = position[1] - 15

        sprite_size = self.get_sprite().size[0]

        health_bar_width = int((self.health / self.max_health) * sprite_size)

        pygame.draw.rect(window, (255, 0, 0), (x, y, sprite_size, 10))
        pygame.draw.rect(window, (0, 255, 0), (x, y, health_bar_width, 10))

    def draw(self, window):
        self.health_bar(window)
        self.sprite.draw(window)
