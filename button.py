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
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.font = pygame.font.Font(None, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.sprite: "pygame.surface.Surface" = sprite

    def draw(self, surface):
        if self.sprite:
            self.rect.width = self.sprite.get_width()
            self.rect.height = self.sprite.get_height   ()
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


class ActionButton:
    def __init__(self, x, y, width, height, text='', font_name='Arial', font_size=30, 
                 text_color=(0, 0, 0), bg_color=(255, 255, 255), 
                 hover_text_color=(0, 0, 0), hover_bg_color=(200, 200, 200), 
                 outline_color=None, outline_width=0, onClick=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.SysFont(font_name, font_size)
        self.text_color = text_color
        self.bg_color = bg_color
        self.hover_text_color = hover_text_color
        self.hover_bg_color = hover_bg_color
        self.outline_color = outline_color
        self.outline_width = outline_width
        self.onClick = onClick
        self.hovered = False

    def draw(self, screen):
        # Check if the mouse is over the button
        mouse_pos = pygame.mouse.get_pos()
        self.hovered = self.rect.collidepoint(mouse_pos)

        # Draw the button
        if self.hovered:
            bg_color = self.hover_bg_color
            text_color = self.hover_text_color
        else:
            bg_color = self.bg_color
            text_color = self.text_color

        if self.outline_color and self.outline_width > 0:
            pygame.draw.rect(screen, self.outline_color, self.rect, 0)
            inner_rect = self.rect.inflate(-self.outline_width * 2, -self.outline_width * 2)
            pygame.draw.rect(screen, bg_color, inner_rect, 0)
        else:
            pygame.draw.rect(screen, bg_color, self.rect, 0)

        # Draw the text
        text_surf = self.font.render(self.text, True, text_color)
        text_rect = text_surf.get_rect(center=self.rect.center)
        screen.blit(text_surf, text_rect)

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.hovered and self.onClick:
                self.onClick()