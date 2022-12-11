import pygame

class Panel:
    """A rectangle that is rendered on a pygame screen.

    Attrributes:
        x (int): X position of the top left point.
        y (int): Y position of the top left point.
        width (int): The width of the panel.
        height (int): The height of the panel.
        color (tuple): The color of the panel.
        has_border (bool): If the panel has a border.
        border_color (tuple): The color of the border.
    """

    def __init__(self, x, y, width, height, color: tuple = (150, 150, 150),
                 has_border: bool = True, border_color: tuple = (0, 0, 0)) -> None:
        """Creates a Panel object.

        Args:
            x (int): X position of the top left point.
            y (int): Y position of the top left point.
            width (int): The width of the panel.
            height (int): The height of the panel.
            color (tuple, optional): The color of the panel. Defaults to (150, 150, 150).
            has_border (bool, optional): If the panel has a border. Defaults to True.
            border_color (tuple, optional): The color of the border. Defaults to (0, 0, 0).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.has_border = has_border
        self.border_color = border_color

    def render(self, screen):
        """Renders the panel on the screen

        Args:
            screen (Surface): The screen the panel is rendered in.
        """

        pygame.draw.rect(screen, self.color, pygame.Rect(self.x, self.y, self.width, self.height))
        
        if self.has_border:
           self.__render_border(screen)

    def __render_border(self, screen):
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y, self.width, 1))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y + self.height, self.width, 1))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x, self.y, 1, self.height))
        pygame.draw.rect(screen, self.border_color, pygame.Rect(self.x + self.width, self.y, 1, self.height))