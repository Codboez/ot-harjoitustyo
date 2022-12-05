from ui.text_object import TextObject
from ui.panel import Panel

class Button:
    def __init__(self, x: int, y: int, width: int, height: int, action, font, right_click_action = None,
      text: str = "", color: tuple = (150, 150, 150), hover_color: tuple = (120, 120, 120),
      text_align: str = "center", has_border: bool = False, border_color: tuple = (0, 0, 0)) -> None:
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
        if self.hovered:
            self.hover_background.render(screen)
        else:
            self.background.render(screen)

        self.text.render(screen)
        
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
