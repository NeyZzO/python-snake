import pygame
# from main import App

class Snake:
    def __init__(self, game ):
        self.direction: str = "RIGHT"
        self.pos = [100, 50]
        self.game = game
        self.body: list[list[int]] = [
            [100, 50],
            [90, 50],
            [80, 50],
            [70, 50]
        ]
        self.score = 0
        self.game = game

    def drawScore(self, color: "pygame.Color", font: str, size: int, window: "pygame.surface.Surface"):
        score_font: "pygame.font.Font" = pygame.font.SysFont(font, size)
        score_surface = score_font.render(f"Score: {self.score} | X: {self.pos[0]} Y: {self.pos[1]}", True, color)
        score_rect = score_surface.get_rect()

        window.blit(score_surface, score_rect)

    def draw(self, window: "pygame.surface.Surface"):
        for pos in self.body:
            pygame.draw.rect(window, pygame.color.Color(0, 255, 0), pygame.Rect(pos[0], pos[1], 10, 10))

    def update(self, window: "pygame.surface.Surface"):
        
        WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()

        ## On gère le déplacement du snake
        if self.direction == "RIGHT":
            self.pos[0] += 10
        elif self.direction == "LEFT":
            self.pos[0] -= 10
        elif self.direction == "UP":
            self.pos[1] -= 10
        elif self.direction == "DOWN":
            self.pos[1] += 10


        if self.pos[0] >= WINDOW_WIDTH -     10:
            self.pos[0] = WINDOW_WIDTH - 10
        if self.pos[1] >= WINDOW_HEIGHT:
            self.pos[1] = WINDOW_HEIGHT
        if self.pos[0] <= 0:
            self.pos[0] = 0
        if self.pos[1] <= 0:
            self.pos[1] = 0

        # On update le corps du snake
        self.body.insert(0, list(self.pos))
        if self.pos[0] == self.game.apple.x and self.pos[1] == self.game.apple.y:
            self.game.apple.newCoords()
            self.score += 1
        else:
            self.body.pop()

    def onEvent(self, event: "pygame.event.Event"):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN and (self.direction != "UP" and self.direction != "DOWN"):
                self.direction = "DOWN"
            elif event.key == pygame.K_UP and (self.direction != "UP" and self.direction != "DOWN"):
                self.direction = "UP"
            elif event.key == pygame.K_LEFT and (self.direction != "LEFT" and self.direction != "RIGHT"):
                self.direction = "LEFT"
            elif event.key == pygame.K_RIGHT and (self.direction != "LEFT" and self.direction != "RIGHT"):
                self.direction = "RIGHT"


