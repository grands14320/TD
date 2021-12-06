import time

import Enemy0
import Enemy1
import GUI
from Utility import Tools


class Level:

    def __init__(self):
        self.current_wave = 0
        self.money = 0
        self.hp = 100
        self.waves = Tools.get_single_wave()
        self.wave = self.get_wave()
        self.time_start_lvl = 0
        self.enemies_type = [Enemy0.Enemy0((125, 625)), Enemy1.Enemy1((125, 625))]
        self.gui = GUI.GUI()

    def get_tile(self, point):
        return self.tiles[point - 1].get_surface()

    def get_map(self, current_level):
        map_list = []
        level = "Levels/" + "Level_" + str(current_level) + "/map"
        with open(level, 'r') as file:
            for line in file.readlines():
                line = line.strip('\n')
                map_list.append(line.split("  "))
        return map_list

    def update(self, window):
        i = 0
        while i < len(self.enemies):
            self.enemies[i].health_bar(window)
            if self.enemies[i].get_health() <= 0:
                self.money += self.enemies[i].get_gold_dropped()
                self.enemies.pop(i)
                if len(self.enemies) == 0:  # narazie jesli brak enemy,pozniej jezeli user wcisnie guzik czy cos
                    self.wave = self.get_wave()
                continue
            if self.enemies[i].arrived_to_finish(self.enemy_finish_position):
                self.hp -= 10
                self.enemies.pop(i)
                if len(self.enemies) == 0:  # narazie jesli brak enemy,pozniej jezeli user wcisnie guzik czy cos
                    self.wave = self.get_wave()
                continue
            self.enemies[i].move(self.map, self.map_size)
            i += 1
        self.update_wave()
        self.draw_map(window)

        self.gui.update(self.towers)
        self.gui.draw(window, self.hp, self.money, self.current_wave)

        for enemy in self.enemies:
            enemy.draw(window)

        for tower in self.towers:
            tower.update(self.enemies)
            tower.draw(window)

        if self.hp <= 0:
            self.game_over()

    def game_over(self):
        pass

    def draw_map(self, window):
        for i in range(len(self.map)):
            for j in range(len(self.map[i])):
                window.blit(self.get_tile(int(self.map[i][j])), (j * self.size_of_tile[0], i * self.size_of_tile[1]))

    def get_wave(self):
        self.time_start_lvl = time.perf_counter()
        for wave, enemies in self.waves:
            self.current_wave = wave
            return enemies

    def update_wave(self):
        i = 0
        while i < len(self.wave.items()):
            spawn_time = list(self.wave.items())[i][0]
            enemy_type = list(self.wave.items())[i][1]
            if (round(time.perf_counter(), 5) - round(self.time_start_lvl, 5)) < float(spawn_time):
                break
            self.enemies.append(self.enemies_type[int(enemy_type)].clone())
            del self.wave[spawn_time]
