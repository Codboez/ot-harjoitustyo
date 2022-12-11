class TextObject:
    """A text object that gets rendered on a pygame screen.

    Attributes:
        text (str): The text that gets displayed.
        position (tuple): The position the text object will be rendered in.
        font (Font): The font used to render text.
        color (tuple, optional): The color of the text.
        container (tuple, optional): The container the text will be rendered in.
        text_align (str, optional): How the text will be aligned. "left", "right" or "center".
    """

    def __init__(self, text: str, position: tuple, font, color: tuple = (0, 0, 0),
                 container: tuple = None, text_align: str = "center") -> None:
        """Creates a TextObject.

        Args:
            text (str): The text that gets displayed.
            position (tuple): The position the text object will be rendered in.
            font (Font): The font used to render text.
            color (tuple, optional): The color of the text. Defaults to (0, 0, 0).
            container (tuple, optional): The container the text will be rendered in. Defaults to None.
            text_align (str, optional): How the text will be aligned. "left", "right" or "center". Defaults to "center".
        """
        self.text = text
        self.color = color
        self.container = container
        self.text_align = text_align
        self.font = font
        self.position = position
        self.text_image = None

    def render(self, screen):
        """Renders the text on the screen.

        Args:
            screen (Surface): The screen the text will be rendered in.
        """

        self.text_image = self.font.render(self.text, True, self.color)
        location = (self.position[0], self.position[1])

        if self.container != None:
            y_location = self.container[1] + self.container[3] / 2 - self.text_image.get_height() / 2

            if self.text_align == "center":
                location = (self.container[0] + self.container[2] / 2 - self.text_image.get_width() / 2, y_location)
            elif self.text_align == "left":
                location = (self.container[0] + 5, y_location)
            else:
                location = (self.container[0] + self.container[2] - self.text_image.get_width(), y_location)

        screen.blit(self.text_image, location)