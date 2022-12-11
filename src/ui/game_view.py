import pygame
import functools
from game.board import Board
from game.cell import Cell
from ui.button import Button

class GameView:
    def __init__(self, board: Board, font, game):
        self.__board = board
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

        for row in self.__board.get_board():
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
        for row in self.__board.get_board():
            for cell in row:
                cell.button.update_hovered(self.mouse_pos)

    def click(self, mouse_button):
        """Click the screen. Clicks any hovered buttons.

        Args:
            mouse_button (int): The clicked mouse button.
        """

        for row in self.__board.get_board():
            for cell in row:
                if cell.button.hovered and not self.__board.game_over:
                    cell.button.click(mouse_button)
                    self.__board.open_cell_recursion_stack_size = 0

        for button in self.__buttons:
            if button.hovered:
                button.click(mouse_button)

    def __calculate_board_size_on_screen(self) -> tuple:
        width = len(self.__board.get_board()[0]) * (Cell.size + 1) - 1
        height = len(self.__board.get_board()) * (Cell.size + 1) - 1
        return (width, height)

    def __render_board_background(self, screen):
        board_size = self.__calculate_board_size_on_screen()
        pygame.draw.rect(screen, (230, 230, 230),
          pygame.Rect(screen.get_width() / 2 - board_size[0] / 2 - 15,
          screen.get_height() / 2 - board_size[1] / 2 - 5, board_size[0] + 30, board_size[1] + 90))

    def __render_board_top(self, screen):
        #pygame.draw.rect(screen, (230, 230, 230), pygame.Rect(cell.pos[0], cell.pos[1], Cell.size(), Cell.size()))
        board_size = self.__calculate_board_size_on_screen()
        text = self.__font[0].render(f"{self.__board.mines_non_flagged}", True, (0, 0, 0))
        screen.blit(text, (screen.get_width() / 2 - board_size[0] / 2 + 30,
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
