import os
import time
from typing import List

import pygame

from Enemies import Enemy, Enemy0, Enemy1
from gui import Gui
from utils import Sprite
from Towers import Tower
from DetailsStateService import DetailsStateService
from Enemies.Enemy2 import Enemy2
from Enemies.Enemy3 import Enemy3
from EventsStateService import EventStateService
from TowersStateService import TowersStateService
from PlayerProgressStateService import PlayerProgressStateService
from utils.Utility import Tools
from enums.CurrentScreen import CurrentScreen


class Level:

    is_over: bool = False
    map: List[List[str]]
    map_size: (int, int)
    tiles: [Sprite.Sprite]
    enemies_not_fetched_yet: bool = True
    enemy_start_position: (int, int)
    enemy_finish_position: (int, int)

    enemies: List[Enemy.Enemy] = []
    towers: List[Tower.Tower] = []

    size_of_tile = None
    wave: (str, {str, str})
    time_start_lvl: float = None
    enemies_type = []
    gui: Gui

    details_state_service = DetailsStateService()
    towers_state_service: TowersStateService = TowersStateService()
    event_state_service: EventStateService = EventStateService()
    player_progress_state_service: PlayerProgressStateService = PlayerProgressStateService()

    def __init__(self, game_map: List[List[str]], tiles: [Sprite.Sprite]):
        self.map = game_map
        self.tiles = tiles
        self.enemies_type = [Enemy0.Enemy0((125, 625)), Enemy1.Enemy1((125, 625)), Enemy2((125, 625)), Enemy3((125, 625))]
        self.gui = Gui.Gui()
        self.waves = Tools.get_single_wave()

    def get_tile(self, point) -> pygame.Surface:
        return self.tiles[point - 1].get_surface()

    @staticmethod
    def get_map(current_level) -> List[List[str]]:
        map_list: List[List[str]] = []
        level = "Levels/" + "Level_" + str(current_level) + "/map"
        try:
            with open(level, 'r') as file:
                for line in file.readlines():
                    line = line.strip('\n')
                    map_list.append(line.split("  "))
        except FileNotFoundError:
            print("Map not found")
        return map_list

    def update(self, window) -> None:
        # get wave if there are no enemies.
        if self.enemies_not_fetched_yet:
            self.enemies_not_fetched_yet = False
            self.wave = self.get_wave()

        if self.wave is None:
            self.on_game_over_success()

        self.draw_map(window)

        self.gui.update(self.towers)
        self.gui.draw(window)

        if self.player_progress_state_service.get_is_wave_ongoing():
            if self.time_start_lvl is None:
                self.time_start_lvl = time.perf_counter()

            # push enemies to list from wave.
            self.update_wave()

            for enemy in self.enemies:
                if enemy.get_health() <= 0:
                    self.player_progress_state_service.add_money(enemy.get_gold_dropped())
                    self.enemies.remove(enemy)
                    continue
                if enemy.arrived_to_finish(self.enemy_finish_position):
                    self.player_progress_state_service.subtract_health(10)
                    self.enemies.remove(enemy)
                    continue
                enemy.move(self.map, self.map_size)
                enemy.draw(window)

            # stop the wave if there are no spawned enemies left and there are no enemies left to spawn.
            if len(self.enemies) == 0 and not self.wave:
                print('Wave: [' + self.player_progress_state_service.get_current_wave_name() + '] finished')
                self.player_progress_state_service.set_is_wave_ongoing(False)
                self.enemies_not_fetched_yet = True
                self.player_progress_state_service.set_current_wave_name('Idle')
                self.time_start_lvl = None

        for tower in self.towers:
            tower.update(self.enemies)
            tower.draw(window)

        self.check_click_events()

        if self.player_progress_state_service.get_hp() <= 0:
            self.on_game_over_defeat()

    def on_game_over_defeat(self):
        self.player_progress_state_service.set_current_screen(CurrentScreen.GAME_OVER)
        self.is_over = True

    def on_game_over_success(self):
        self.player_progress_state_service.set_current_screen(CurrentScreen.WIN)
        self.is_over = True

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
                        self.player_progress_state_service.subtract_money(new_tower.get_price())

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
