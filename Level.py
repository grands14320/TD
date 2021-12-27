import time
from typing import List

import pygame

import Enemy
import Enemy0
import Enemy1
import GUI
import Sprite
import Tower
from DetailsStateService import DetailsStateService
from EventsStateService import EventStateService
from TowersStateService import TowersStateService
from PlayerProgressStateService import PlayerProgressStateService
from Utility import Tools


class Level:
    map: list[list[str]]
    map_size: (int, int)
    tiles: [Sprite.Sprite]
    enemy_start_position: (int, int)
    enemy_finish_position: (int, int)

    enemies: List[Enemy.Enemy] = []
    towers: List[Tower.Tower] = []

    size_of_tile = None
    waves = Tools.get_single_wave()
    wave: (str, {str, str})
    time_start_lvl: float = 0
    enemies_type = []
    gui: GUI

    details_state_service = DetailsStateService()
    towers_state_service: TowersStateService = TowersStateService()
    event_state_service: EventStateService = EventStateService()
    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self, game_map: list[list[str]], tiles: [Sprite.Sprite]):
        self.map = game_map
        self.wave = self.get_wave()
        self.tiles = tiles
        self.enemies_type = [Enemy0.Enemy0((125, 625)), Enemy1.Enemy1((125, 625))]
        self.gui = GUI.GUI()

    def get_tile(self, point) -> pygame.Surface:
        return self.tiles[point - 1].get_surface()

    def get_map(self, current_level) -> list[list[str]]:
        map_list: list[list[str]] = []
        level = "Levels/" + "Level_" + str(current_level) + "/map"
        with open(level, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map_list.append(line.split("  "))
        return map_list

    def update(self, window) -> None:
        i = 0
        while i < len(self.enemies):
            self.enemies[i].health_bar(window)
            if self.enemies[i].get_health() <= 0:
                self.player_progress_state_service.add_money(self.enemies[i].get_gold_dropped())
                self.enemies.pop(i)
                if len(self.enemies) == 0:  # narazie jesli brak enemy,pozniej jezeli user wcisnie guzik czy cos
                    self.wave = self.get_wave()
                continue
            if self.enemies[i].arrived_to_finish(self.enemy_finish_position):
                self.player_progress_state_service.subtract_health(10)
                self.enemies.pop(i)
                if len(self.enemies) == 0:  # narazie jesli brak enemy,pozniej jezeli user wcisnie guzik czy cos
                    self.wave = self.get_wave()
                continue
            self.enemies[i].move(self.map, self.map_size)
            i += 1

        self.update_wave()
        self.draw_map(window)

        self.gui.update(self.towers)
        self.gui.draw(window)

        for enemy in self.enemies:
            enemy.draw(window)

        for tower in self.towers:
            tower.update(self.enemies)
            tower.draw(window)

        self.check_click_events()

        if self.player_progress_state_service.get_hp() <= 0:
            self.game_over()

    def game_over(self):
        pass

    def check_click_events(self):
        if self.towers_state_service.get_clicked_structure() is not None:
            for event in self.event_state_service.get_events():
                # check left mouse button click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    tile_x = int(mouse_x / self.size_of_tile[0])
                    tile_y = int(mouse_y / self.size_of_tile[1])
                    clicked_tower_type: type = self.towers_state_service.get_clicked_structure()

                    # check whether click have been made on map
                    if self.is_tile_available_for_structure(tile_x, tile_y):
                        new_tower: Tower = clicked_tower_type((tile_x * self.size_of_tile[0] + 25,
                                                              tile_y * self.size_of_tile[1] + 25))
                        self.towers.append(new_tower)

                        self.towers_state_service.set_clicked_structure(None)
                # check right mouse button click
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
                    self.towers_state_service.set_clicked_structure(None)

    def is_tile_available_for_structure(self, tile_x, tile_y) -> bool:
        if tile_x > self.map_size[0] or tile_y > self.map_size[1]:
            return False

        tile_x_center = tile_x * self.size_of_tile[0] + 25
        tile_y_center = tile_y * self.size_of_tile[1] + 25
        for tower in self.towers:
            if tower.position[0] == tile_x_center and tower.position[1] == tile_y_center:
                return False

        tile_type = self.map[tile_y][tile_x]
        if tile_type != '3':
            return True

        return False

    def draw_map(self, window) -> None:
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                window.blit(self.get_tile(int(self.map[i][j])), (j * self.size_of_tile[0], i * self.size_of_tile[1]))

    def get_wave(self) -> {str, str}:
        self.time_start_lvl = time.perf_counter()
        for wave, enemies in self.waves:
            self.player_progress_state_service.set_current_wave_name(wave)
            return enemies

    def update_wave(self) -> None:
        i = 0
        while i < len(self.wave.items()):
            spawn_time = list(self.wave.items())[i][0]
            enemy_type = list(self.wave.items())[i][1]
            if (round(time.perf_counter(), 5) - round(self.time_start_lvl, 5)) < float(spawn_time):
                break
            self.enemies.append(self.enemies_type[int(enemy_type)].clone())
            del self.wave[spawn_time]
