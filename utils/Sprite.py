import pygame
import math


class Sprite:

    def __init__(self, size, position=(0, 0)):
        self.sprite = pygame.Surface(size)
        self.sprite.fill((255, 255, 255))
        self.position = position
        self.size = size
        self.rotation = 0
        self.color = (255, 255, 255)
        self.origin = self.sprite.get_rect()
        self.origin.center = self.position
        self.bounds = self.get_global_bounds()
        self.texture = ""

    # must set size before call
    def set_texture(self, path):
        """
        Sets the sprite's texture
        """
        self.texture = pygame.image.load(path)
        self.sprite = self.texture

    def set_transparent_texture(self, texture_path):
        """
        Sets the sprite's transparent texture
        """
        self.texture = pygame.image.load(texture_path).convert()
        self.texture.set_colorkey((0, 0, 0))
        self.sprite = self.texture.convert()

    def get_position(self):
        return self.position

    def set_position(self, new_position):
        self.position = new_position
        self.origin.center = self.position

    def move(self, offset=(0, 0)):
        """
        Moves the sprite
        """
        self.position = tuple(map(lambda x, y: x + y, self.position, offset))
        self.origin.center = self.position

    def set_rotation(self, new_rotation):
        """
        Rotates the sprite
        """
        self.rotation = new_rotation % 360
        self.sprite = pygame.Surface(self.size)
        self.sprite.fill(self.color)
        if self.texture != "":
            self.sprite = self.texture
        self.sprite.set_colorkey((0, 0, 0))
        self.sprite = pygame.transform.rotate(self.sprite, self.rotation)
        self.origin = self.sprite.get_rect()
        self.origin.center = self.position

    def rotate(self, angle=0):
        """
        Rotates the sprite by given angle
        """
        self.rotation += angle
        self.set_rotation(self.rotation)

    def rotate_to_point(self, point):
        """
        Rotates the sprite to certain point
        """
        self.rotation = math.atan2(point[0] - self.position[0], point[1] - self.position[1]) * 180 / 3.14
        self.set_rotation(self.rotation)

    def set_fill_color(self, color):
        """
        Sets the sprite background colour
        """
        self.color = color
        self.sprite.fill(self.color)

    def set_size(self, size):
        self.size = size
        self.sprite = pygame.Surface(size)

    def get_size(self):
        return self.size

    # (position.x left up corner, position.y left up corner, size.x , size.y)
    def get_global_bounds(self):
        self.origin = self.sprite.get_rect()
        self.origin.center = self.position
        return self.origin

    def intersect(self, bounds):
        """
        Detects sprite collision
        """
        # left up corner
        if self.contains((bounds[0], bounds[1])):
            return True
        # right up
        if self.contains((bounds[0] + bounds[2], bounds[1])):
            return True
        # right down
        if self.contains((bounds[0] + bounds[2], bounds[1] + bounds[3])):
            return True
        # left down
        if self.contains((bounds[0], bounds[1] + bounds[3])):
            return True
        return False

    def contains(self, point):
        """
        Checks whether sprite contains given point
        """
        self.bounds = self.get_global_bounds()
        if self.bounds[0] <= point[0] <= self.bounds[0] + self.bounds[2] and \
                self.bounds[1] <= point[1] <= self.bounds[1] + self.bounds[3]:
            return True
        return False

    def get_surface(self):
        return self.sprite

    def draw(self, window):
        window.blit(self.sprite, self.origin)
