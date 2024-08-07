import pygame
from button import Button, ActionButton

class MainScreen:
    def __init__(self, game) -> None:
        self.game: "App" = game
        self.playBtn:"Button" = Button(100, 100, 120, 20, "Jouer", game.startGame, sprite= pygame.image.load('./images/play-btn.png'))
    
    def draw(self):
        self.game.getScreen().blit(pygame.image.load('./images/main-title.png'), (0, 0))
        self.playBtn.draw(self.game.getScreen())
        
    def onEvent(self, event: 'pygame.event.Event'):
        self.playBtn.onEvent(event)


class DeathScreen:
    def __init__(self, game):
        self.game = game
        sc: "pygame.Surface" = game.getScreen()
        self.replayBtn: "ActionButton" = ActionButton(x=(sc.get_width() // 2) - 50, y=(sc.get_height()//2) - 20, width=100, height=40, text="Replay", onClick=game.startGame, bg_color=(255,255,255), text_color=(255, 0, 0), hover_bg_color=(200, 200, 200), hover_text_color=(200, 0, 0), font_name="JetBrainsMono Nerd Font", font_size=20)
        self.quitButton: "ActionButton" = ActionButton(x=(sc.get_width() // 2) - 50, y=(sc.get_height()//2) - 20 + 40 + 10, width=100, height=40, text="Quit", onClick=game.startGame, bg_color=(255,255,255), text_color=(255, 0, 0), hover_bg_color=(200, 200, 200), hover_text_color=(200, 0, 0), font_name="JetBrainsMono Nerd Font", font_size=20)

    def draw(self):
        window: "pygame.Surface" = self.game.getScreen()

        # Game Over

        ft: 'pygame.font.Font' = pygame.font.SysFont('JetBrainsMono Nerd Font', size=34, bold=True)
        txt_surface = ft.render("Game Over", True, pygame.color.Color(0, 0, 0))
        txt = txt_surface.get_rect(centerx=window.get_rect().centerx, y= 40)
        self.game.getScreen().blit(txt_surface, txt)

        # Score

        ft: 'pygame.font.Font' = pygame.font.SysFont('JetBrainsMono Nerd Font', size=18)
        txt_surface = ft.render(f"Score: {self.game.snake.score}", True, pygame.color.Color(0, 0, 0))
        txt = txt_surface.get_rect(centerx=window.get_rect().centerx, y= 90)
        self.game.getScreen().blit(txt_surface, txt)

        # Best Score

        txt_surface = ft.render(f"Best Score: UNKNOWN", True, pygame.color.Color(0, 0, 0))
        txt = txt_surface.get_rect(centerx=window.get_rect().centerx, y= 110)
        self.game.getScreen().blit(txt_surface, txt)

        # Buttons

        self.replayBtn.draw(self.game.getScreen())
        self.quitButton.draw(self.game.getScreen())

    def onEvent(self, event: "pygame.event.Event"):
        self.replayBtn.handle_event(event=event)
        self.quitButton.handle_event(event=event)