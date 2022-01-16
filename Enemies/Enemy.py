import time
from typing import List

import pygame

import Game
from utils import Sprite
from effects.BulletEffect import BulletEffect
from enums.UnitVectors import UnitVectors
from utils.Utility import Tools


class Enemy:
    distance_travelled: int = 0
    sprite: Sprite.Sprite = None
    base_health: int
    health: int
    base_speed: int
    speed: float
    next_move: UnitVectors
    previous_move: UnitVectors
    gold_dropped: int
    is_rotating: bool
    effects: set[BulletEffect] = set()

    def __init__(self, sprite: Sprite.Sprite):
        self.sprite = sprite

    def __del__(self):
        print("Enemy down")

    def get_distance_travelled(self) -> float:
        return self.distance_travelled

    def get_sprite(self) -> Sprite.Sprite:
        return self.sprite

    def get_health(self) -> int:
        return self.health

    def get_gold_dropped(self) -> int:
        return self.gold_dropped

    def move(self, game_map: List[List[int]], map_size: (int, int)) -> None:
        """
        Moves the enemy object on a gamemap. Enemy can move only on previously defined path.
        """
        self.apply_effects()

        size_of_tile: (int, int) = Game.Game.levels[Game.Game.current_level].size_of_tile

        x: int = int(self.sprite.get_position()[0] / size_of_tile[0])
        y: int = int(self.sprite.get_position()[1] / size_of_tile[1])

        move_offset: list[int] = [self.next_move[0] * self.speed,
                                  self.next_move[1] * self.speed]

        if not self.is_on_center_tile(x, y, map_size):

            position_of_tile = (x * size_of_tile[0] + size_of_tile[0] / 2,
                                y * size_of_tile[1] + size_of_tile[1] / 2)

            length_from_tile_vector = [(position_of_tile[0] - self.sprite.get_position()[0]),
                                       (position_of_tile[1] - self.sprite.get_position()[1])]

            length_from_tile = Tools.get_length_point_to_point(position_of_tile, self.sprite.get_position())

            if abs(move_offset[0]) > abs(length_from_tile) or abs(move_offset[1]) > abs(length_from_tile):

                if not self.tile_is_behind(position_of_tile):
                    self.sprite.move(length_from_tile_vector)
                    self.distance_travelled += abs(length_from_tile_vector[0]) + abs(length_from_tile_vector[1])
                    self.set_direction(game_map, map_size)
                    move_offset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

                    if move_offset[0] != 0:
                        if move_offset[0] > 0:
                            move_offset[0] -= length_from_tile
                        else:
                            move_offset[0] += length_from_tile
                    elif move_offset[1] != 0:
                        if move_offset[1] > 0:
                            move_offset[1] -= length_from_tile
                        else:
                            move_offset[1] += length_from_tile

        else:
            self.set_direction(game_map, map_size)
            move_offset = [self.next_move[0] * self.speed, self.next_move[1] * self.speed]

        move_offset = [move_offset[0], move_offset[1]]
        self.sprite.move(move_offset)
        self.distance_travelled += abs(move_offset[0]) + abs(move_offset[1])
        if self.is_rotating:
            self.sprite.rotate(2)

    def apply_effects(self) -> None:
        """
        Applies bullet effect
        """
        expired_effects: set[BulletEffect] = set()
        for effect in self.effects:
            effect.apply_effect(self)
            time_elapsed: float = (round(time.perf_counter(), 5) - round(effect.applied_at, 5))

            if time_elapsed >= effect.duration:
                effect.on_effect_expired(self)
                expired_effects.add(effect)

        for expired_effect in expired_effects:
            self.effects.discard(expired_effect)

    def set_direction(self, game_map: List[List[int]], map_size: (int, int)) -> None:
        """
        Sets the direction of enemy.
        """
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        x = int(self.sprite.get_position()[0] / size_of_tile[0])
        y = int(self.sprite.get_position()[1] / size_of_tile[1])

        if x - 1 < 0 or x + 1 > map_size[0] or y - 1 < 0 or y + 1 > map_size[1]:
            return

        if game_map[y + 1][x] == '3' and self.previous_move != UnitVectors.UP:  # down
            self.next_move = UnitVectors.DOWN
            self.previous_move = UnitVectors.DOWN
            return

        if game_map[y - 1][x] == '3' and self.previous_move != UnitVectors.DOWN:  # up
            self.next_move = UnitVectors.UP
            self.previous_move = UnitVectors.UP
            return

        if game_map[y][x + 1] == '3' and self.previous_move != UnitVectors.LEFT:  # right
            self.next_move = UnitVectors.RIGHT
            self.previous_move = UnitVectors.RIGHT
            return

        if game_map[y][x - 1] == '3' and self.previous_move != UnitVectors.RIGHT:  # left
            self.next_move = UnitVectors.LEFT
            self.previous_move = UnitVectors.LEFT
            return

    def is_on_center_tile(self, x, y, map_size):
        """
        Check whether enemy is on tile center
        """
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        if x - 1 < 0 or x + 1 > map_size[0] or y - 1 < 0 or y + 1 > map_size[1]:
            return True

        return not (x * size_of_tile[0] + size_of_tile[0] / 2 != self.sprite.get_position()[0] or y * size_of_tile[1] +
                    size_of_tile[1] / 2 != self.sprite.get_position()[1])

    def arrived_to_finish(self, finish):
        """
        Check whether enemy arrived to map's end
        """
        size_of_tile = Game.Game.levels[Game.Game.current_level].size_of_tile

        sprite_index_x = int(self.sprite.get_position()[0] / size_of_tile[0])
        sprite_index_y = int(self.sprite.get_position()[1] / size_of_tile[1])

        finish_index_x = int(finish[0] / size_of_tile[0])
        finish_index_y = int(finish[1] / size_of_tile[1])

        return sprite_index_x == finish_index_x and sprite_index_y == finish_index_y

    def tile_is_behind(self, position_of_tile):
        """
        check whether given tile is behind enemy
        """
        if position_of_tile[1] > self.sprite.get_position()[1] and self.next_move == UnitVectors.UP:
            return True
        if position_of_tile[1] < self.sprite.get_position()[1] and self.next_move == UnitVectors.DOWN:
            return True
        if position_of_tile[0] > self.sprite.get_position()[0] and self.next_move == UnitVectors.LEFT:
            return True
        if position_of_tile[0] < self.sprite.get_position()[0] and self.next_move == UnitVectors.RIGHT:
            return True
        return False

    def health_bar(self, window):
        """
        draws enemy's health bar
        """
        position = self.sprite.get_global_bounds()

        x = position[0]
        y = position[1] - 15

        sprite_size = self.get_sprite().size[0]

        health_bar_width = int((self.health / self.base_health) * sprite_size)

        pygame.draw.rect(window, (255, 0, 0), (x, y, sprite_size, 10))
        pygame.draw.rect(window, (0, 255, 0), (x, y, health_bar_width, 10))

    def draw(self, window):
        self.health_bar(window)
        self.sprite.draw(window)
