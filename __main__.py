# import sys
import pygame, pygame.event
from pygame.locals import * # type: ignore
from snake import Snake
from fruit import Apple
from button import Button
from screens import MainScreen, DeathScreen

WINDOW_WIDTH = 400
WINDOW_HEIGHT = 400
FPS = 15

class App:
    width: int
    height: int
    def __init__(self, fps: int = 60):
        pygame.init()
        self.__running = True
        self.width, self.height = WINDOW_WIDTH, WINDOW_HEIGHT
        self.size: tuple[int, int] = self.width, self.height
        self.clock: "pygame.time.Clock" = pygame.time.Clock()
        self.__screen: "pygame.surface.Surface" = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        gameIcon: pygame.Surface = pygame.image.load('./images/snake_game-1.png')
        pygame.display.set_caption("Pygame snake game")
        pygame.display.set_icon(gameIcon)
        self.started = False

        
        self.mainScreen = MainScreen(self)

        self.deathScreen = DeathScreen(self)

        # Entités
        self.apple: "Apple" | None = None #Apple(self.__screen)
        self.snake: "Snake" | None = None #Snake(self)

        self.execute(fps)

    def onEvent(self, event: "pygame.event.Event") -> None:
        if event.type == pygame.QUIT:
            self.__running = False
        

    def getScreen(self) -> 'pygame.surface.Surface':
        return self.__screen

    def onLoop(self):
        if self.snake and self.snake.alive:
            self.snake.update(self.__screen)

    def gameOver(self):
        self.apple: "Apple" | None = None #Apple(self.__screen)

    def onRender(self):
        self.__screen.fill("purple")
        if (self.apple and self.snake) and self.snake.alive:
            self.snake.draw(self.__screen)
            self.apple.draw()
            self.snake.drawScore(pygame.color.Color(255, 255, 255), "Arial", 15, self.__screen)
        elif self.started == False and not self.snake:
             self.mainScreen.draw()
        elif self.started and not self.snake.alive:
            self.deathScreen.draw()
            
        pygame.display.update()

    def onCleanup(self):
        pygame.quit()
        exit(0)
        
    def startGame(self):
        self.snake = Snake(self)
        self.apple = Apple(self.__screen)
        self.started = True        
        self.apple.newCoords()

    def execute(self, fps: int):
        while self.__running:
            for event in pygame.event.get():
                self.onEvent(event)
                if self.snake:
                    self.snake.onEvent(event)
                if not self.started and not self.snake:
                    self.mainScreen.onEvent(event)
                if self.snake and not self.snake.alive:
                    self.deathScreen.onEvent(event)
                                    
            self.onLoop()
            self.onRender()
            

            self.clock.tick(fps)
            
        self.onCleanup()

if __name__ == "__main__":
    app = App(FPS)
