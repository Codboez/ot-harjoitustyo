import os
from ui.ui import UI
from game.board import Board
from database.scores import Scores

class Game:
    """Minesweeper game. Controls the board and the UI.

    Attributes:
        window (UI): The User interface of the game.
        font (tuple): The default font and its file path.
        board (Board): The board of the game.
    """

    def __init__(self, screen_width: int = 1280, screen_height: int = 720) -> None:
        """Create a Minesweeper game.

        Args:
            screen_width (int, optional): The width of the window. Defaults to 1280.
            screen_height (int, optional): The height of the window. Defaults to 720.
        """

        self.__running = True
        self.database = Scores("scores.db")
        self.check_database_exists()
        self.window = UI(screen_width, screen_height)
        self.font = self.window.font
        self.board = Board(10, 10, 20, self)
        self.change_state(1)

    def run(self):
        """Run the game loop.
        """

        while self.__running:
            self.__running = self.window.update()

    def change_state(self, state: int):
        """Change the UI scene.

        Args:
            state (int): The scene that will be enabled.
        """

        self.window.change_state(state, self.board, self)

    def create_board(self, width, height, mine_chance):
        """Creates a new board with the given information.

        Args:
            width (int): The width of the new board.
            height (int): The height of the new board.
            mine_chance (int): The mine chance of the new board.
        """

        self.board = Board(width, height, mine_chance, self)

    def create_font_with_new_size(self, size: int):
        """Creates a new font with a different size using the default font.

        Args:
            size (int): The size of the new font.

        Returns:
            Font: The new font.
        """

        return self.window.get_font_with_new_size(size)

    def check_database_exists(self):
        """Creates a new database file if one does not already exist.
        """

        if not os.path.exists(self.database.file_path):
            self.database.set_up()
