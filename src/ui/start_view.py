import pygame
import functools
from ui.button import Button
from ui.input_field import InputField
from ui.text_object import TextObject
from ui.panel import Panel
from game import button_functions
from database import scores

class StartView:
    """This class creates and renders the start view of the UI.

    Attributes:
        mouse_pos (tuple): The current mouse position on the screen
    """

    def __init__(self, font, game) -> None:
        """Creates a new start view. Adds all default UI objects

        Args:
            font (tuple): 2 elements. Element 0: The default font that text is rendered with.
                          Element 1: The path to the font file.
            game (Game): The Game object that controls the UI.
        """

        self.mouse_pos = (0, 0)
        self.__font = font
        self.__buttons = []
        self.__input_fields = []
        self.__game = game
        self.__messages = []
        self.__leaderboard_objects = []
        self.__add_input_fields()
        self.__add_buttons()
        self.__add_leaderboards()

    def update(self, screen):
        """Updates and renders all UI objects.

        Args:
            screen (Surface): The canvas that all UI objects are rendered into.
        """
    
        self.__update_buttons()
        self.render(screen)

    def render(self, screen):
        """Renders all UI objects into the screen.

        Args:
            screen (Surface): The canvas that all UI objects are rendered into.
        """

        screen.fill((255, 255, 255))
        self.__render_buttons(screen)
        self.__render_input_fields(screen)
        self.__render_messages(screen)
        self.__render_leaderboards(screen)
        pygame.display.flip()

    def click(self, mouse_button):
        """Clicks any Button or InputField that is mouse hovered.

        Args:
            mouse_button (int): The mouse button that was clicked.
        """

        for button in self.__buttons:
            if button.hovered:
                button.click(mouse_button)

        for input_field in self.__input_fields:
            input_field.selected = False

            if input_field.is_hovered(self.mouse_pos):
                input_field.selected = True

    def __add_buttons(self):
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

    def __add_input_fields(self):
        font = self.__game.window.get_font_with_new_size(18)

        input = InputField(400, 275, 80, 50, font, "Width")
        self.__input_fields.append(input)

        input = InputField(490, 275, 80, 50, font, "Height")
        self.__input_fields.append(input)

        input = InputField(580, 275, 130, 50, font, "Mine percentage")
        self.__input_fields.append(input)

    def __add_leaderboards(self):
        easy = scores.get_sorted_scores_for_board(1, 10)
        medium = scores.get_sorted_scores_for_board(2, 10)
        hard = scores.get_sorted_scores_for_board(3, 10)
        leaderboards = [easy, medium, hard]

        font = self.__game.create_font_with_new_size(15)

        for i in range(3):
            self.__add_leaderboard_top((200 + i * 300, 400), font, i)
            for j in range(len(leaderboards[i])):
                score = leaderboards[i][j]
                time = f"{score[3]:.2f}"
                text = f"{j + 1:>2}. {score[1]:<13}{time:>6}{score[4]:>25}"
                pos = (200 + i * 300, 400 + j * 20 - 90)
                text_obj = TextObject(text, pos, font, container=(pos[0], pos[1], 300, 300))
                self.__leaderboard_objects.append(text_obj)

    def __add_leaderboard_top(self, pos, font, i):
        self.__leaderboard_objects.append(Panel(pos[0], pos[1], 300, 300, (253, 253, 253)))
        self.__leaderboard_objects.append(Panel(pos[0], pos[1], 300, 40, (240, 240, 240)))
        self.__leaderboard_objects.append(TextObject("Name", (pos[0] + 15, pos[1] + 20), font))
        self.__leaderboard_objects.append(TextObject("Time", (pos[0] + 100, pos[1] + 20), font))
        self.__leaderboard_objects.append(TextObject("Creation date", (pos[0] + 180, pos[1] + 20), font))

        if i == 0:
            difficulty = "Easy"
        elif i == 1:
            difficulty = "Medium"
        else:
            difficulty = "Hard"

        text = TextObject(f"{difficulty} leaderboard", (pos[0] + 95, pos[1] - 20), font)
        self.__leaderboard_objects.append(text)

    def __update_buttons(self):
        for button in self.__buttons:
            button.update_hovered(self.mouse_pos)

    def __render_buttons(self, screen):
        for button in self.__buttons:
            button.render(screen)

    def __render_input_fields(self, screen):
        for current in self.__input_fields:
            current.render(screen)

    def keydown(self, key):
        """Adds a character to any selected input fields.

        Args:
            key (str): The key to add.
        """

        for input_field in self.__input_fields:
            if input_field.selected:
                input_field.add_char(key)

    def __render_messages(self, screen):
        for message in self.__messages:
            message.render(screen)

    def __render_leaderboards(self, screen):
        for obj in self.__leaderboard_objects:
            obj.render(screen)

    def add_message(self, message):
        """Add a text object.

        Args:
            message (TextObject): The text object that is added.
        """

        self.__messages.append(message)

    def add_error_message(self, text, pos):
        """Creates and adds a red error text.

        Args:
            text (str): The string that is displayed.
            pos (tuple): The position on screen that the text gets rendered into.
        """

        self.add_message(TextObject(text, pos, self.__font[0], (255, 0, 0)))

    def delete_messages(self):
        """Deletes all messages.
        """

        self.__messages.clear()