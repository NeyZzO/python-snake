import pygame
# from main import App

class Snake:
    def __init__(self, game ):
        self.direction: str = "RIGHT"
        self.__change_to: str | None = None
        self.pos = [100, 64]
        self.game = game
        self.alive = True
        self.sprites = [
            pygame.image.load("images/snake-head.png").convert_alpha(),
            pygame.image.load("images/snake-bp-1.png").convert_alpha(),
            pygame.image.load("images/snake-bp-2.png").convert_alpha(),
            pygame.image.load("images/snake-tail.png").convert_alpha(),
        ]
        self.body: list[list[int]] = [
            [128, 64, "RIGHT"],
            [112, 64, "RIGHT"],
            [69, 64, "RIGHT"],
            [80, 64, "RIGHT"]
        ]
        self.score = 0
        self.game = game

    def drawScore(self, color: "pygame.Color", font: str, size: int, window: "pygame.surface.Surface"):
        """Draws the score on each frame of the game

        Args:
            color (pygame.Color): Color
            font (str): Font of the text
            size (int): Size of the text
            window (pygame.surface.Surface): The game window
        """
        score_font: "pygame.font.Font" = pygame.font.SysFont(font, size)
        score_surface = score_font.render(f"Score: {self.score} | X: {self.pos[0]} Y: {self.pos[1]}", True, color)
        score_rect = score_surface.get_rect()

        window.blit(score_surface, score_rect)

    def draw(self, window: "pygame.surface.Surface"):
        """Draws the snake each frame

        Args:
            window (pygame.surface.Surface): the game window
        """
        if not self.alive:
            return
        
        sprite = self.sprites[0]
        sprite2 = self.sprites[1]
        sprite3 = self.sprites[-1]
        
        if self.direction == "UP":
            sprite = pygame.transform.rotate(self.sprites[0], angle=90)
            sprite2 = pygame.transform.rotate(self.sprites[1], angle=90)
            sprite3 = pygame.transform.rotate(self.sprites[-1], angle=90)
        elif self.direction == "LEFT":
            sprite = pygame.transform.rotate(self.sprites[0], angle=180)
            sprite2 = pygame.transform.rotate(self.sprites[1], angle=180)
            sprite3 = pygame.transform.rotate(self.sprites[-1], angle=180)
        elif self.direction == "DOWN":
            sprite = pygame.transform.rotate(self.sprites[0], angle=270)
            sprite2 = pygame.transform.rotate(self.sprites[1], angle=270)
            sprite3 = pygame.transform.rotate(self.sprites[-1], angle=270)

        window.blit(sprite, tuple(self.body[0]))
        window.blit(sprite2, tuple(self.body[1][0], self.body[1][1]))
        
        for i in range(2, len(self.body) - 1):
            pos = self.body[i]
            spritedny = self.sprites[2]
            if self.direction == "UP":
                spritedny = pygame.transform.rotate(spritedny, angle=90)
            elif self.direction == "LEFT":
                spritedny = pygame.transform.rotate(spritedny, angle=180)
            elif self.direction == "DOWN":
                spritedny = pygame.transform.rotate(spritedny, angle=270)
                
            window.blit(spritedny, tuple(pos))
            # pygame.draw.rect(window, pygame.color.Color(0, 255, 0), pygame.Rect(pos[0], pos[1], 16, 16))
            
        window.blit(sprite3, tuple(self.body[-1]))
            

    def update(self, window: "pygame.surface.Surface"):
        """Updates the snake each frame

        Args:
            window (pygame.surface.Surface): _description_
        """
        if not self.alive:
            return
        WINDOW_WIDTH, WINDOW_HEIGHT = window.get_size()

        ## On gère le déplacement du snake
        if self.direction == "RIGHT":
            self.pos[0] += 16
        elif self.direction == "LEFT":
            self.pos[0] -= 16
        elif self.direction == "UP":
            self.pos[1] -= 16
        elif self.direction == "DOWN":
            self.pos[1] += 16


        if self.pos[0] >= WINDOW_WIDTH - 16:
            self.pos[0] = WINDOW_WIDTH - 16
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
        """Checks the events for the snake

        Args:
            event (pygame.event.Event): Pygame event
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.__change_to = "DOWN"
            if event.key == pygame.K_UP:
                self.__change_to = "UP"
            if event.key == pygame.K_LEFT:
                self.__change_to = "LEFT"
            if event.key == pygame.K_RIGHT:
                self.__change_to = "RIGHT"
                                
            if self.__change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.__change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.__change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.__change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'


