import pygame
import functools
from ui.button import Button
from ui.input_field import InputField
from ui.text_object import TextObject
from game import button_functions

class StartView:
    def __init__(self, font, game) -> None:
        self.mouse_pos = (0, 0)
        self.__font = font
        self.__buttons = []
        self.__input_fields = []
        self.__game = game
        self.__messages = []
        self.add_input_fields()
        self.add_buttons()

    def update(self, screen):
        self.update_buttons()
        self.render(screen)

    def render(self, screen):
        screen.fill((255, 255, 255))
        self.render_buttons(screen)
        self.render_input_fields(screen)
        self.render_messages(screen)
        pygame.display.flip()

    def click(self, mouse_button):
        for button in self.__buttons:
            if button.hovered:
                button.click(mouse_button)

        for input_field in self.__input_fields:
            input_field.selected = False

            if input_field.is_hovered(self.mouse_pos):
                input_field.selected = True

    def add_buttons(self):
        action = functools.partial(button_functions.create_board, 10, 10, 15, self.__game)
        button = Button(400, 200, 150, 50, action, self.__font[0], text="Easy", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

        action = functools.partial(button_functions.create_board, 15, 15, 20, self.__game)
        button = Button(560, 200, 150, 50, action, self.__font[0], text="Medium", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

        action = functools.partial(button_functions.create_board, 30, 20, 25, self.__game)
        button = Button(720, 200, 150, 50, action, self.__font[0], text="Hard", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

        action = functools.partial(button_functions.create_custom_board, self.__input_fields[0].text,
          self.__input_fields[1].text, self.__input_fields[2].text, self.__game)
        button = Button(720, 275, 150, 50, action, self.__font[0], text="Create custom", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

    def add_input_fields(self):
        font = self.__game.window.get_font_with_new_size(18)

        input = InputField(400, 275, 80, 50, font, "Width")
        self.__input_fields.append(input)

        input = InputField(490, 275, 80, 50, font, "Height")
        self.__input_fields.append(input)

        input = InputField(580, 275, 130, 50, font, "Mine percentage")
        self.__input_fields.append(input)

    def update_buttons(self):
        for button in self.__buttons:
            button.update_hovered(self.mouse_pos)

    def render_buttons(self, screen):
        for button in self.__buttons:
            button.render(screen)

    def render_input_fields(self, screen):
        for current in self.__input_fields:
            current.render(screen)

    def keydown(self, key):
        for input_field in self.__input_fields:
            if input_field.selected:
                input_field.add_char(key)

    def render_messages(self, screen):
        for message in self.__messages:
            message.render(screen)

    def add_message(self, message):
        self.__messages.append(message)

    def add_error_message(self, text, pos):
        self.add_message(TextObject(text, pos, self.__font[0], (255, 0, 0)))

    def delete_messages(self):
        self.__messages.clear()