import pygame

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, action, font, right_click_action = None,
     text: str = "", color: tuple = (150, 150, 150), hover_color: tuple = (120, 120, 120),
       text_align: str = "center", has_border: bool = False, border_color: tuple = (0, 0, 0)) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.right_click_action = right_click_action
        self.text = text
        self.hovered = False
        self.font = font
        self.text_align = text_align
        self.has_border = has_border
        self.border_color = border_color

    def render(self, screen):
        if self.hovered:
            pygame.draw.rect(screen, self.hover_color, pygame.Rect(self.x, self.y, self.width, self.height))
        else:
            pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

        self.__render_text(screen)

        if self.has_border:
            self.__render_border(screen)
        
    def is_hovered(self, mouse_pos: tuple) -> bool:
        return (mouse_pos[0] < self.x + self.width and mouse_pos[0] > self.x
         and mouse_pos[1] < self.y + self.height and mouse_pos[1] > self.y)

    def click(self, mouse_button):
        if mouse_button == 1:
            self.action()
        elif mouse_button == 3:
            if self.right_click_action == None: return
            self.right_click_action()

    def update_hovered(self, mouse_pos: tuple):
        self.hovered = self.is_hovered(mouse_pos)

    def __render_border(self, screen):
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y, self.width, 1))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y + self.height, self.width, 1))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y, 1, self.height))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x + self.width, self.y, 1, self.height))

    def __render_text(self, screen):
        text = self.font.render(self.text, True, (0, 0, 0))
        screen.blit(text, (self.x + self.width / 2 - text.get_width() / 2, self.y + self.height / 2 - text.get_height() / 2))