import pygame
from button import Button

class MainScreen:
    def __init__(self, game) -> None:
        self.game: "App" = game
        self.playBtn:"Button" = Button(100, 100, 120, 20, "Jouer", game.startGame)
    
    def draw(self):
        self.game.getScreen().blit(pygame.image.load('./images/main-title.png'), (0, 0))
        self.playBtn.draw(self.game.getScreen())
        
    def onEvent(self, event: 'pygame.event.Event'):
        self.playBtn.onEvent(event)