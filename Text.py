import pygame

pygame.init()


class Text:

    def __init__(self, string = "", position = (0, 0), color=(0, 0, 0), font_size=25):
        self.text = str(string)
        self.color = color
        self.position = position
        self.font_size = font_size
        self.my_font = pygame.font.SysFont('Arial', self.font_size)

    def set_string(self, string):
        self.text = str(string)
        return self

    def set_position(self, position):
        self.position = position
        return self

    def draw(self, window):
        window.blit(self.my_font.render(self.text, 0, self.color), self.position)

