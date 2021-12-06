import time

from Bullet import Bullet
from Sprite import Sprite
from Utility import Tools


class Tower:
    def __init__(self):
        self.bullets = []
        self.active = False

    def get_damage(self):
        return self.damage

    def get_cooldown(self):
        return self.cooldown

    def get_range(self):
        return self.range

    def get_kills(self):
        return self.kills

    def get_sprite(self):
        return self.sprite

    def update(self, enemies):

        finded = False
        target = ""
        distance = 0

        for enemy in enemies:
            if self.is_in_range(enemy) and enemy.get_distance_travelled() > distance:
                target = enemy
                distance = enemy.get_distance_travelled()
                finded = True

        if finded and time.perf_counter() - self.time_last_shoot > self.cooldown:
            self.time_last_shoot = time.perf_counter()
            self.shoot_to_target(target)

        if finded and self.rotatable:
            self.sprite.rotate_to_point(target.get_sprite().get_position())

        i = 0
        while i < len(self.bullets):
            bullet_position = self.bullets[i].get_sprite().get_position()
            if self.hitted_enemy(self.bullets[i], enemies):
                self.bullets.pop(i)
                continue
            if Tools.get_length_point_to_point(bullet_position, self.sprite.get_position()) > self.range:
                self.bullets.pop(i)
                continue
            self.bullets[i].update()
            i += 1

    def is_in_range(self, enemy):

        bounds = enemy.get_sprite().get_global_bounds()

        # left up corner
        if Tools.get_length_point_to_point((bounds[0], bounds[1]), self.position) <= self.range:
            return True
        # right up
        if Tools.get_length_point_to_point((bounds[0] + bounds[2], bounds[1]), self.position) <= self.range:
            return True
        # right down
        if Tools.get_length_point_to_point((bounds[0] + bounds[2], bounds[1] + bounds[3]), self.position) <= self.range:
            return True
        # left down
        if Tools.get_length_point_to_point((bounds[0], bounds[1] + bounds[3]), self.position) <= self.range:
            return True
        return False

    def shoot_to_target(self, target):
        tower_position = self.sprite.get_position()
        enemy_position = target.get_sprite().get_position()
        vector = (enemy_position[0] - tower_position[0], enemy_position[1] - tower_position[1])
        vector_length = Tools.get_length_point_to_point(tower_position, enemy_position)
        vector = (vector[0] / vector_length, vector[1] / vector_length)
        self.bullets.append(Bullet(Sprite((10, 10), self.sprite.get_position()), vector, self.bullet_speed))

    def hitted_enemy(self, bullet, enemies):
        i = 0
        while i < len(enemies):
            if enemies[i].get_sprite().intersect(bullet.get_sprite().get_global_bounds()):
                enemies[i].health -= self.damage
                if enemies[i].health <= 0:
                    self.kills += 1
                print("Trafiony")
                return True
            i += 1
        return False

    def draw(self, window):
        if self.active:
            window.blit(self.circle_range,
                        (self.sprite.get_position()[0] - self.range, self.sprite.get_position()[1] - self.range))
        self.sprite.draw(window)

        for bullet in self.bullets:
            bullet.draw(window)
