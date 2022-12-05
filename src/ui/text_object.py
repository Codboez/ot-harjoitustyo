class TextObject:
    def __init__(self, text: str, position: tuple, font, color: tuple = (0, 0, 0),
      container: tuple = None, text_align: str = "center") -> None:
        self.text = text
        self.color = color
        self.container = container
        self.text_align = text_align
        self.font = font
        self.position = position
        self.text_image = None

    def render(self, screen):
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