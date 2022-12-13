import pygame
import functools
import time
from game.cell import Cell
from ui.button import Button

class GameView:
    def __init__(self, font, game):
        self.__buttons = []
        self.__messages = []
        self.mouse_pos = (0, 0)
        self.__font = font
        self.__game = game
        self.__add_buttons()

    def render(self, screen):
        """Renders the view.

        Args:
            screen (Surface): The screen that everything will be rendered to.
        """

        screen.fill((255, 255, 255))
        self.__render_board(screen)
        self.__render_buttons(screen)
        self.__render_messages(screen)
        pygame.display.flip()

    def __render_board(self, screen):
        self.__render_board_background(screen)
        self.__render_board_top(screen)

        for row in self.__game.board.get_board():
            for cell in row:
                cell.button.render(screen)

    def update(self, screen):
        """Updates and renders the view.

        Args:
            screen (Surface): The screen that everything will be rendered to.
        """

        self.__update_buttons()
        self.render(screen)

    def __update_cell_buttons(self):
        for row in self.__game.board.get_board():
            for cell in row:
                cell.button.update_hovered(self.mouse_pos)

    def click(self, mouse_button):
        """Click the screen. Clicks any hovered buttons.

        Args:
            mouse_button (int): The clicked mouse button.
        """

        for row in self.__game.board.get_board():
            for cell in row:
                if cell.button.hovered and not self.__game.board.game_over:
                    cell.button.click(mouse_button)
                    self.__game.board.open_cell_recursion_stack_size = 0

        for button in self.__buttons:
            if button.hovered:
                button.click(mouse_button)

    def __calculate_board_size_on_screen(self) -> tuple:
        width = len(self.__game.board.get_board()[0]) * (Cell.size + 1) - 1
        height = len(self.__game.board.get_board()) * (Cell.size + 1) - 1
        return (width, height)

    def __render_board_background(self, screen):
        board_size = self.__calculate_board_size_on_screen()
        pygame.draw.rect(screen, (230, 230, 230),
          pygame.Rect(screen.get_width() / 2 - board_size[0] / 2 - 15,
          screen.get_height() / 2 - board_size[1] / 2 - 5, board_size[0] + 30, board_size[1] + 90))

    def __render_board_top(self, screen):
        board_size = self.__calculate_board_size_on_screen()
        text = self.__font[0].render(f"{self.__game.board.mines_non_flagged}", True, (0, 0, 0))
        screen.blit(text, (screen.get_width() / 2 - board_size[0] / 2 + 30,
          screen.get_height() / 2 - board_size[1] / 2 + 20))

        if not self.__game.board.game_over and self.__game.board.start_time != 0:
            time_passed = f"{time.time() - self.__game.board.start_time:.2f}"
        else:
            time_passed = f"{self.__game.board.end_time - self.__game.board.start_time:.2f}"
        text = self.__font[0].render(f"{time_passed:>8}", True, (0, 0, 0))
        screen.blit(text, (screen.get_width() / 2 + board_size[0] / 2 - 80,
          screen.get_height() / 2 - board_size[1] / 2 + 20))

    def __add_buttons(self):
        action = functools.partial(self.__game.change_state, 1)
        button = Button(50, 20, 150, 40, action, self.__font[0], text="Exit to menu",
          color=(200, 200, 200), hover_color=(170, 170, 170), has_border=True)
        self.__buttons.append(button)

    def __update_buttons(self):
        self.__update_cell_buttons()

        for button in self.__buttons:
            button.update_hovered(self.mouse_pos)

    def __render_buttons(self, screen):
        for button in self.__buttons:
            button.render(screen)

    def __render_messages(self, screen):
        for message in self.__messages:
            message.render(screen)

    def add_message(self, message):
        """Adds a message to render.

        Args:
            message (TextObject): A text object that should be rendered.
        """

        self.__messages.append(message)

    def keydown(self, key):
        """Does nothing. The UI calls this method for the current view.
        """

        pass
