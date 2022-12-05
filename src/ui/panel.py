import pygame

class Panel:
    def __init__(self, x, y, width, height, color: tuple = (150, 150, 150),
      has_border: bool = True, border_color: tuple = (0, 0, 0)) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.has_border = has_border
        self.border_color = border_color

    def render(self, screen):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        
        if self.has_border:
           self.render_border(screen)

    def render_border(self, screen):
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y, self.width, 1))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y + self.height, self.width, 1))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y, 1, self.height))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x + self.width, self.y, 1, self.height))