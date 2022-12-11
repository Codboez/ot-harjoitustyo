from ui.text_object import TextObject
from ui.panel import Panel

class Button:
    """A button that gets rendered in the UI.

    Attributes:
        x (int): X position of the buttons top left point.
        y (int): Y position of the buttons top left point.
        width (int): The width of the button.
        height (int): The height of the button.
        action (Callable): The left click action.
        right_click_action (Callable): The right click action.
        hovered (bool): If the mouse is hovering over this button.
        background (Panel): A Panel that is rendered as the buttons background.
        hover_background (Panel): A Panel that is rendered as the buttons background when it is hovered.
        text (TextObject): A text object that is rendered on the button.
    """

    def __init__(self, x: int, y: int, width: int, height: int, action, font, right_click_action = None,
      text: str = "", color: tuple = (150, 150, 150), hover_color: tuple = (120, 120, 120),
      text_align: str = "center", has_border: bool = False, border_color: tuple = (0, 0, 0)) -> None:
        """Creates a button.

        Args:
            x (int): X position of the buttons top left point.
            y (int): Y position of the buttons top left point.
            width (int): The width of the button.
            height (int): The height of the button.
            action (Callable): The left click action.
            font (Font): The font used to render the text on the button.
            right_click_action (Callable, optional): The right click action. Defaults to None.
            text (str, optional): The text that will be displayed on the button. Defaults to "".
            color (tuple, optional): The color of the background. Defaults to (150, 150, 150).
            hover_color (tuple, optional): The color of the hover background. Defaults to (120, 120, 120).
            text_align (str, optional): How the text will be aligned. "left", "right" or "center". Defaults to "center".
            has_border (bool, optional): If a border gets rendered. Defaults to False.
            border_color (tuple, optional): The color of the border. Defaults to (0, 0, 0).
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.action = action
        self.right_click_action = right_click_action
        self.hovered = False
        self.background = Panel(x, y, width, height, color, has_border, border_color)
        self.hover_background = Panel(x, y, width, height, hover_color, has_border, border_color)
        self.text = TextObject(text, (x, y), font, container=(x, y, width, height), text_align=text_align)

    def render(self, screen):
        """Renders the button on the screen.

        Args:
            screen (Surface): The screen that the button will be rendered in.
        """

        if self.hovered:
            self.hover_background.render(screen)
        else:
            self.background.render(screen)

        self.text.render(screen)
        
    def is_hovered(self, mouse_pos: tuple) -> bool:
        """Determines if the mouse is hovering this button.

        Args:
            mouse_pos (tuple): The current position of the mouse.

        Returns:
            bool: If the button is hovered.
        """

        return (mouse_pos[0] < self.x + self.width and mouse_pos[0] > self.x
         and mouse_pos[1] < self.y + self.height and mouse_pos[1] > self.y)

    def click(self, mouse_button):
        """Click this button. Uses the left or right click action depending on the mouse button.

        Args:
            mouse_button (int): The mouse button that was clicked.
        """

        if mouse_button == 1:
            self.action()
        elif mouse_button == 3:
            if self.right_click_action == None: return
            self.right_click_action()

    def update_hovered(self, mouse_pos: tuple):
        """Updates if this button is hovered based on the mouse position.

        Args:
            mouse_pos (tuple): The current mouse position.
        """

        self.hovered = self.is_hovered(mouse_pos)
