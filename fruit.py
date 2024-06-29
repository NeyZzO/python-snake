import random
import pygame

class Apple:
    def __init__(self, window: "pygame.surface.Surface") -> None:
        self.window = window
        self.x = 16 * 3
        self.sprite = pygame.image.load('./images/apple.png')
        self.y = 16 * 3
        self.color = pygame.color.Color(255, 0, 0)

    def newCoords(self):
        self.x = random.randrange(1, self.window.get_width() // 16) * 16
        self.y = random.randrange(1, self.window.get_height() // 16) * 16

    def draw(self):
        self.window.blit(self.sprite, (self.x, self.y))
        # pygame.draw.rect(self.window, self.color, pygame.Rect(self.x, self.y, 16, 16))