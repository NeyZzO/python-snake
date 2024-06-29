import pygame

# class Button:
#     def __init__(self, x: int, y: int, w: int = 100, h: int = 100, action: callable = lambda x: print(x), text: str = "", textSize: int = 10, textFont: str = "", textColor: "pygame.color.Color" = pygame.color.Color(255,255,255), backroundColor: "pygame.color.Color" = pygame.color.Color(0,0,0), sprite: str = None):
#         self.x = x
#         self.y = y
#         self.w = w
#         self.h = h
#         self.action = action
#         self.text = text
#         self.textSize = textSize

class Button:
    def __init__(self, x, y, width, height, text, action, font_size=30, 
                 text_color=(255, 255, 255), bg_color=(100, 100, 100), 
                 sprite=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.sprite = sprite

    def draw(self, surface):
        if self.sprite:
            surface.blit(self.sprite, self.rect)
        else:
            pygame.draw.rect(surface, self.bg_color, self.rect)
            text_surface = self.font.render(self.text, True, self.text_color)
            text_rect = text_surface.get_rect(center=self.rect.center)
            surface.blit(text_surface, text_rect)

    def onEvent(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.rect.collidepoint(event.pos):
                self.action()