import pygame

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, action,
     color: tuple = (120, 120, 120), hover_color: tuple = (160, 160, 160)) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.hovered = False

    def render(self, screen):
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        
    def is_hovered(self, mouse_pos: tuple) -> bool:
        return (mouse_pos[0] < self.x + self.width and mouse_pos[0] > self.x
         and mouse_pos[1] < self.y + self.height and mouse_pos[1] > self.y)

    def click(self):
        self.action()

    def update_hovered(self, mouse_pos: tuple):
        self.hovered = self.is_hovered(mouse_pos)