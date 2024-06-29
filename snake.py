import pygame
# from main import App

class Snake:
    def __init__(self, game ):
        self.direction: str = "RIGHT"
        self.__change_to: str | None = None
        self.pos = [100, 64]
        self.game = game
        self.alive = True
        self.updateing = True
        self.sprites = [
            pygame.image.load("images/snake-head.png").convert_alpha(),
            pygame.image.load("images/snake-bp-1.png").convert_alpha(),
            pygame.image.load("images/snake-bp-2.png").convert_alpha(),
            pygame.image.load("images/snake-bp-angle.png").convert_alpha(),
            pygame.image.load('images/snake-tail-angle-2.png').convert_alpha(),
            pygame.image.load('images/snake-tail-angle.png').convert_alpha(),
            pygame.image.load("images/snake-tail.png").convert_alpha(),
        ]
        self.body: list[list[int]] = [
            [128, 64, "RIGHT"], # Tête
            [112, 64, "RIGHT"], # Cou
            [69, 64, "RIGHT"], # Corps
            [80, 64, "RIGHT"] # Queue
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
        # sprite2 = self.sprites[1]
        sprite3 = self.sprites[-1]
        
        if self.body[0][2] == "UP":
            sprite = pygame.transform.rotate(self.sprites[0], angle=90)
        elif self.body[0][2] == "LEFT":
            sprite = pygame.transform.rotate(self.sprites[0], angle=180)
        elif self.body[0][2] == "DOWN":
            sprite = pygame.transform.rotate(self.sprites[0], angle=270)
        
        if self.body[-1][2] == "UP":
            sprite3 = pygame.transform.rotate(self.sprites[-1], angle=90)
        elif self.body[-1][2] == "LEFT":
            sprite3 = pygame.transform.rotate(self.sprites[-1], angle=180)
        elif self.body[-1][2] == "DOWN":
            sprite3 = pygame.transform.rotate(self.sprites[-1], angle=270)
            
            
        window.blit(sprite, (self.body[0][0], self.body[0][1]))
        # window.blit(sprite2, (self.body[1][0], self.body[1][1]))
        
        for i in range(1, len(self.body) - 1):
            pos = (self.body[i][0], self.body[i][1])
            direc = self.body[i][2]
            spritedny = self.sprites[2]
            
            if self.body[i - 1][2] != self.body[i][2]:
                spritedny = self.sprites[3]
                if self.body[i - 1][2] == "DOWN" and self.body[i][2] == "RIGHT":
                    spritedny = pygame.transform.rotate(spritedny, angle=270)
                elif self.body[i - 1][2] == "DOWN" and self.body[i][2] == "LEFT":
                    spritedny = pygame.transform.rotate(spritedny, angle=0)
                elif self.body[i - 1][2] == "UP" and self.body[i][2] == "RIGHT":
                    spritedny = pygame.transform.rotate(spritedny, angle=180)
                elif self.body[i - 1][2] == "UP" and self.body[i][2] == "LEFT":
                    spritedny = pygame.transform.rotate(spritedny, angle=90)
                    
                elif self.body[i - 1][2] == "RIGHT" and self.body[i][2] == "UP":
                    spritedny = pygame.transform.rotate(spritedny, angle=0)
                elif self.body[i - 1][2] == "RIGHT" and self.body[i][2] == "DOWN":
                    spritedny = pygame.transform.rotate(spritedny, angle=90)
                    
                elif self.body[i - 1][2] == "LEFT" and self.body[i][2] == "UP":
                    spritedny = pygame.transform.rotate(spritedny, angle=270)
                elif self.body[i - 1][2] == "LEFT" and self.body[i][2] == "DOWN":
                    spritedny = pygame.transform.rotate(spritedny, angle=180)
            else:
                if direc == "UP":
                    spritedny = pygame.transform.rotate(spritedny, angle=90)
                elif direc == "LEFT":
                    spritedny = pygame.transform.rotate(spritedny, angle=180)
                elif direc == "DOWN":
                    spritedny = pygame.transform.rotate(spritedny, angle=270)
                
            window.blit(spritedny, tuple(pos))
            # pygame.draw.rect(window, pygame.color.Color(0, 255, 0), pygame.Rect(pos[0], pos[1], 16, 16))
        
        
        ## TAIL PART
        if self.body[-1][2] != self.body[-2][2]:
            sprite3 = self.sprites[-2]
            if self.body[-1][2] == "RIGHT" and self.body[-2][2] == "DOWN":
                sprite3 = pygame.transform.rotate(sprite3, angle=270)
            elif self.body[-1][2] == "RIGHT" and self.body[-2][2] == "UP":
                sprite3 = pygame.transform.rotate(self.sprites[-3], angle=270)
                
            elif self.body[-1][2] == "LEFT" and self.body[-2][2] == "DOWN":
                sprite3 = pygame.transform.rotate(self.sprites[-3], angle=90)
            elif self.body[-1][2] == "LEFT" and self.body[-2][2] == "UP":
                sprite3 = pygame.transform.rotate(sprite3, angle=90)
                
            elif self.body[-1][2] == "UP" and self.body[-2][2] == "RIGHT":
                sprite3 = pygame.transform.rotate(sprite3, angle=0)
            elif self.body[-1][2] == "UP" and self.body[-2][2] == "LEFT":
                sprite3 = pygame.transform.rotate(self.sprites[-3], angle=0)
                
            elif self.body[-1][2] == "DOWN" and self.body[-2][2] == "RIGHT":
                sprite3 = pygame.transform.rotate(self.sprites[-3], angle=180)
            elif self.body[-1][2] == "DOWN" and self.body[-2][2] == "LEFT":
                sprite3 = pygame.transform.rotate(sprite3, angle=180)
                
        
        window.blit(sprite3, (self.body[-1][0], self.body[-1][1]))
            

    def update(self, window: "pygame.surface.Surface"):
        """Updates the snake each frame

        Args:
            window (pygame.surface.Surface): _description_
        """
        if not self.alive or not self.updateing:
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
        self.body.insert(0, [self.pos[0], self.pos[1], self.direction])
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
                
            if event.key == pygame.K_SPACE:
                self.updateing = not self.updateing
                
            if self.__change_to == 'UP' and self.direction != 'DOWN':
                self.direction = 'UP'
            if self.__change_to == 'DOWN' and self.direction != 'UP':
                self.direction = 'DOWN'
            if self.__change_to == 'LEFT' and self.direction != 'RIGHT':
                self.direction = 'LEFT'
            if self.__change_to == 'RIGHT' and self.direction != 'LEFT':
                self.direction = 'RIGHT'


