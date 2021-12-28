import pygame


class Text:

    def __init__(self, position=(0, 0), font_size=25, color=(0, 0, 0)):
        self.text = ''
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

    def set_color(self, color: (int, int, int)):
        self.color = color

    def draw(self, window):
        window.blit(self.my_font.render(self.text, True, self.color), self.position)

