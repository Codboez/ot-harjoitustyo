import pygame
import functools
from ui.button import Button
import button_functions

class StartView:
    def __init__(self, font, game) -> None:
        self.mouse_pos = (0, 0)
        self.__font = font
        self.__buttons = []
        self.__game = game
        self.add_buttons()

    def update(self, screen):
        self.update_buttons()
        self.render(screen)

    def render(self, screen):
        screen.fill((255, 255, 255))
        self.render_buttons(screen)
        pygame.display.flip()

    def click(self, mouse_button):
        for button in self.__buttons:
            if button.hovered:
                button.click(mouse_button)

    def add_buttons(self):
        action = functools.partial(button_functions.create_board, 10, 10, 15, self.__game)
        button = Button(400, 200, 150, 50, action, self.__font[0], text="Easy", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

        action = functools.partial(button_functions.create_board, 15, 15, 20, self.__game)
        button = Button(560, 200, 150, 50, action, self.__font[0], text="Medium", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

        action = functools.partial(button_functions.create_board, 40, 30, 30, self.__game)
        button = Button(720, 200, 150, 50, action, self.__font[0], text="Hard", 
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

    def update_buttons(self):
        for button in self.__buttons:
            button.update_hovered(self.mouse_pos)

    def render_buttons(self, screen):
        for button in self.__buttons:
            button.render(screen)