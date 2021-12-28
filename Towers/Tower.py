import time
from typing import List

import pygame

from Enemies import Enemy
from Bullet import Bullet
from utils.Sprite import Sprite
from utils.Utility import Tools


class Tower:

    sprite: Sprite
    circle_range: pygame.Surface

    damage: int
    texture: str
    shot_range: int
    cooldown: float
    position: (int, int)
    kills: int
    is_rotatable: bool
    bullet_speed: int
    bullets: List[Bullet]
    last_shot_time: float
    price: int

    def __init__(self):
        self.bullets = []
        self.active = False

    def get_damage(self):
        return self.damage

    def get_cooldown(self):
        return self.cooldown

    def get_range(self):
        return self.shot_range

    def get_kills(self):
        return self.kills

    def get_price(self):
        return self.price

    def get_sprite(self):
        return self.sprite

    def update(self, enemies):

        enemy_found = False
        target: Enemy.Enemy | None = None
        distance: int = 0

        for enemy in enemies:
            if self.is_in_range(enemy) and enemy.get_distance_travelled() > distance:
                target = enemy
                distance = enemy.get_distance_travelled()
                enemy_found = True

        if enemy_found and time.perf_counter() - self.last_shot_time > self.cooldown:
            self.last_shot_time = time.perf_counter()
            self.shoot_to_target(target)

        if enemy_found and self.is_rotatable:
            self.sprite.rotate_to_point(target.get_sprite().get_position())

        i = 0
        while i < len(self.bullets):
            bullet_position = self.bullets[i].get_sprite().get_position()
            if self.enemy_hit(self.bullets[i], enemies):
                self.bullets.pop(i)
                continue
            if Tools.get_length_point_to_point(bullet_position, self.sprite.get_position()) > self.shot_range:
                self.bullets.pop(i)
                continue
            self.bullets[i].update()
            i += 1

    def is_in_range(self, enemy):

        bounds = enemy.get_sprite().get_global_bounds()

        # left up corner
        if Tools.get_length_point_to_point((bounds[0], bounds[1]), self.position) <= self.shot_range:
            return True
        # right up
        if Tools.get_length_point_to_point((bounds[0] + bounds[2], bounds[1]), self.position) <= self.shot_range:
            return True
        # right down
        if Tools.get_length_point_to_point((bounds[0] + bounds[2], bounds[1] + bounds[3]), self.position) <= self.shot_range:
            return True
        # left down
        if Tools.get_length_point_to_point((bounds[0], bounds[1] + bounds[3]), self.position) <= self.shot_range:
            return True
        return False

    def shoot_to_target(self, target) -> None:
        vector: (float, float) = self.create_target_vector(target)
        bullet: Bullet = Bullet(Sprite((10, 10), self.sprite.get_position()), vector, self.bullet_speed)
        self.bullets.append(bullet)

    def create_target_vector(self, target: Enemy) -> (float, float):
        tower_position = self.sprite.get_position()
        enemy_position = target.get_sprite().get_position()
        vector = (enemy_position[0] - tower_position[0], enemy_position[1] - tower_position[1])
        vector_length = Tools.get_length_point_to_point(tower_position, enemy_position)
        vector = (vector[0] / vector_length, vector[1] / vector_length)
        return vector

    def enemy_hit(self, bullet, enemies):
        i = 0
        while i < len(enemies):
            if enemies[i].get_sprite().intersect(bullet.get_sprite().get_global_bounds()):
                enemies[i].health -= self.damage
                enemies[i].effects = set(bullet.effects)
                if enemies[i].health <= 0:
                    self.kills += 1
                return True
            i += 1
        return False

    def draw(self, window):
        if self.active:
            window.blit(self.circle_range,
                        (self.sprite.get_position()[0] - self.shot_range, self.sprite.get_position()[1] - self.shot_range))
        self.sprite.draw(window)

        for bullet in self.bullets:
            bullet.draw(window)
