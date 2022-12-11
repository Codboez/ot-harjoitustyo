import string
from ui.text_object import TextObject
from ui.panel import Panel

class InputField:
    def __init__(self, x: int, y: int, width: int, height: int, font, placeholder: str = "",
      text_align: str = "left", has_border: bool = True, border_color: tuple = (0, 0, 0),
      background_color: tuple = (245, 245, 245), text_color: tuple = (0, 0, 0),
      placeholder_color: tuple = (150, 150, 150)) -> None:
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.selected = False
        self.placeholder = TextObject(placeholder, (x, y), font,
                                      placeholder_color, (x, y, width, height), text_align)
        self.text = TextObject("", (x, y), font,
                               text_color, (x, y, width, height), text_align)
        self.background = Panel(x, y, width, height, background_color, has_border, border_color)

    def render(self, screen):
        self.background.render(screen)

        if self.text.text == "" and not self.selected:
            self.placeholder.render(screen)
        else:
            self.text.render(screen)

    def add_char(self, char: str):
        if char == "\b":
            self.text.text = self.text.text[:-1]
        elif char in string.ascii_lowercase or char in string.digits:
            if self.__is_input_too_long():
                return

            self.text.text += char

    def is_hovered(self, mouse_pos: tuple):
        return (mouse_pos[0] > self.x and mouse_pos[0] < self.x + self.width and
          mouse_pos[1] > self.y and mouse_pos[1] < self.y + self.height)

    def __is_input_too_long(self) -> bool:
        return self.text.text_image.get_width() > self.width - 10