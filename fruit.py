import random
import pygame

class Apple:
    def __init__(self, window: "pygame.surface.Surface") -> None:
        self.window = window
        self.x = self.window.get_width() // 2
        self.y = self.window.get_height() // 2
        self.color = pygame.color.Color(255, 0, 0)

    def newCoords(self):
        self.x = random.randrange(1, self.window.get_width() // 10) * 10
        self.y = random.randrange(1, self.window.get_height() // 10) * 10

    def draw(self):
        pygame.draw.rect(self.window, self.color, pygame.Rect(self.x, self.y, 10, 10))