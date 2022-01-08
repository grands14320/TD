import unittest

import pygame

import Level0
from Enemies.Enemy0 import Enemy0
from Game import Game
from Towers.Tower0 import Tower0
from utils import Utility
from utils.Utility import Tools


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        pygame.init()
        config = Tools.get_config()
        HEIGHT = int(config['window']['HEIGHT'])
        WIDTH = int(config['window']['WIDTH'])
        pygame.display.set_mode((WIDTH, HEIGHT))

    def test_map_is_present(self):
        self.assertIsNotNone(Level0.Level0.get_map('0'))

    def test_map_blocks(self):
        gmae_map = Level0.Level0.get_map('0')
        all_blocks_are_correct = True
        for i in gmae_map:
            for j in i:
                if j != '1' and j != '2' and j != '3':
                    all_blocks_are_correct = False
        self.assertEqual(all_blocks_are_correct, True)

    def test_get_config(self):
        config = Utility.Tools.get_config()
        fps = int(config['window']['fps'])
        self.assertEqual(fps, 30)

    def test_bullet_creation(self):
        tower: Tower0 = Tower0((125, 125))
        target: Enemy0 = Enemy0((50, 50))
        tower.shoot_to_target(target)
        self.assertTrue(len(tower.bullets) == 1)

    def test_enemy_is_in_range_should_be_true(self):
        tower: Tower0 = Tower0((125, 125))
        target: Enemy0 = Enemy0((50, 50))
        in_range = tower.is_in_range(target)
        self.assertTrue(in_range)

    def test_enemy_is_in_range_should_be_false(self):
        tower: Tower0 = Tower0((200, 200))
        target: Enemy0 = Enemy0((50, 50))
        in_range = tower.is_in_range(target)
        self.assertFalse(in_range)

    def test_get_length_point_to_point(self):
        A = (1, 1)
        B = (1, 2)
        self.assertEqual(Utility.Tools.get_length_point_to_point(A, B), 1.0)

    def test_enemy_at_the_finish_recognised(self):
        finish_point = (200, 200)
        enemy = Enemy0((200, 200))

        Game.current_level = 0
        Game.levels = [Level0.Level0()]

        arrived_to_finish = enemy.arrived_to_finish(finish_point)
        self.assertTrue(arrived_to_finish, True)

    def test_target_bullet_collision(self):
        tower: Tower0 = Tower0((125, 125))
        target: Enemy0 = Enemy0((124, 124))
        tower.shoot_to_target(target)

        is_hit = tower.enemy_hit(tower.bullets[0], [target])
        self.assertTrue(is_hit)

    def test_tower_creation_on_tile_where_tower_is_already_built(self):
        level: Level0.Level0 = Level0.Level0()
        level.towers = [Tower0((225, 225))]
        is_tile_available = level.is_tile_available_for_structure(4, 4)
        self.assertFalse(is_tile_available)

    def test_tower_creation_on_tile(self):
        level: Level0.Level0 = Level0.Level0()
        level.towers = [Tower0((500, 500))]
        is_tile_available = level.is_tile_available_for_structure(4, 4)
        self.assertTrue(is_tile_available)

    def test_tower_creation_on_enemy_path(self):
        # 0, 3 is an enemy path tile.
        level: Level0.Level0 = Level0.Level0()
        is_tile_available = level.is_tile_available_for_structure(3, 0)
        self.assertFalse(is_tile_available)


if __name__ == '__main__':
    unittest.main()
