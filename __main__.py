# import sys
import pygame, pygame.event
from pygame.locals import * # type: ignore
from snake import Snake
from fruit import Apple

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
        pygame.display.set_caption("Pygame snake game")

        # Entités
        self.apple = Apple(self.__screen)
        self.snake = Snake(self)

        self.execute(fps)

    def onEvent(self, event: "pygame.event.Event") -> None:
        if event.type == pygame.QUIT:
            self.__running = False

    def getScreen(self):
        return self.__screen

    def onLoop(self):
        self.snake.update(self.__screen)

    def onRender(self):
        self.__screen.fill("purple")
        self.snake.draw(self.__screen)

        self.apple.draw()
        self.snake.drawScore(pygame.color.Color(255, 255, 255), "Arial", 15, self.__screen)
        pygame.display.update()

    def onCleanup(self):
        pygame.quit()

    def execute(self, fps: int):
        while self.__running:
            for event in pygame.event.get():
                self.onEvent(event)
                self.snake.onEvent(event)

            self.onLoop()
            self.onRender()

            self.clock.tick(fps)
        self.onCleanup()

if __name__ == "__main__":
    app = App(FPS)
