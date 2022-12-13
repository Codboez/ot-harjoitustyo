import random
import functools
import time
from ui.text_object import TextObject
from game.cell import button_functions, Cell

class Board:
    """A minesweeper board.

    Attributes:
        size (tuple): The size of the board.
        mines_non_flagged (int): The amount of mines that have not yet been flagged.
        game_over (bool): Tells if the game has ended yet.
        open_cell_recursion_stack_size (int): The amount of times open_cell has called itself.
        Set this to 0 after every click.
    """

    def __init__(self, width: int, height: int, mine_chance: int, game) -> None:
        """Creates a Board object. Calculates the size of the cells and font used.

        Args:
            width (int): The width of the board.
            height (int): The height of the board.
            mine_chance (int): The percentage chance that mines will spawn with.
            game (Game): The game that this board is attached to.
        """

        self.size = (width, height)
        self.__mine_chance = mine_chance
        self.__has_generated = False
        self.__board = []
        self.mines_non_flagged = 0
        self.__game = game
        self.game_over = False
        self.open_cell_recursion_stack_size = 0
        self.start_time = 0
        self.end_time = 0
        self.calculate_cell_size()
        font = self.__calculate_cell_font_size()
        self.__add_cells(font)

    def open_cell(self, pos: tuple) -> bool:
        """Opens a cell at the given position.

        Args:
            pos (tuple): The position in the board that is being opened.

        Returns:
            bool: If this cell was opened successfully.
        """

        if not self.__has_generated:
            self.generate((pos[0], pos[1]))

        if self.is_out_of_bounds(pos):
            return False

        cell = self.__board[pos[1]][pos[0]]
        self.__update_cell(cell, pos)

        if cell.content == 0:
            if self.__check_for_recursion_stack_overflow():
                return False
            self.open_around_cell((pos[0], pos[1]))
        elif cell.content == -1:
            self.lose()

        if self.check_win() and not self.game_over:
            self.win()

        return True

    def is_out_of_bounds(self, pos: tuple) -> bool:
        """Checks if the given position is out of the bounds of the board.

        Args:
            pos (tuple): The position to check for.

        Returns:
            bool: If it is out of bounds.
        """

        return (pos[0] < 0 or pos[0] >= len(self.__board[0])
                or pos[1] < 0 or pos[1] >= len(self.__board))

    def generate_mines(self, start_pos: tuple):
        """Generates the mines.

        Args:
            start_pos (tuple): The position on the board of the first click.
        """

        if self.__has_generated:
            return

        for i, row in enumerate(self.__board):
            for j, cell in enumerate(row):
                if (j in range(start_pos[0] - 1, start_pos[0] + 2)
                        and i in range(start_pos[1] - 1, start_pos[1] + 2)):
                    continue

                if random.randint(1, 100) <= self.__mine_chance:
                    cell.content = -1
                    self.mines_non_flagged += 1

    def generate_numbers(self):
        """Generates the numbers for all cells
        """

        if self.__has_generated:
            return

        for i, row in enumerate(self.__board):
            for j, cell in enumerate(row):
                if cell.content == -1:
                    continue

                cell.content = self.__count_mines_around_cell((j, i))

    def __count_mines_around_cell(self, pos: tuple) -> int:
        amount = 0
        for i in range(pos[1] - 1, pos[1] + 2):
            for j in range(pos[0] - 1, pos[0] + 2):
                if j == pos[0] and i == pos[1]:
                    continue

                if self.is_out_of_bounds((j, i)):
                    continue

                if self.__board[i][j].content == -1:
                    amount += 1

        return amount

    def count_flags_around_cell(self, pos: tuple) -> int:
        """Counts the flagged cells around the cell at the given position.

        Args:
            pos (tuple): The position in the board the cell is in.

        Returns:
            int: The amount of flags around the cell.
        """

        amount = 0
        for i in range(pos[1] - 1, pos[1] + 2):
            for j in range(pos[0] - 1, pos[0] + 2):
                if j == pos[0] and i == pos[1]:
                    continue

                if self.is_out_of_bounds((j, i)):
                    continue

                if self.__board[i][j].flagged:
                    amount += 1

        return amount

    def generate(self, start_pos: tuple):
        """Generates the board.

        Args:
            start_pos (tuple): The position on the board of the first click.
        """

        self.generate_mines(start_pos)
        self.generate_numbers()
        self.__has_generated = True
        self.start_time = time.time()

    def open_around_cell(self, pos: tuple, open_flagged: bool = True):
        """Opens all cells around the given position.

        Args:
            pos (tuple): The position to open around.
            open_flagged (bool, optional): If it should open flagged cells. Defaults to True.
        """

        for i in range(pos[1] - 1, pos[1] + 2):
            for j in range(pos[0] - 1, pos[0] + 2):
                if j == pos[0] and i == pos[1]:
                    continue

                if self.is_out_of_bounds((j, i)):
                    continue

                if not self.__board[i][j].hidden:
                    continue

                if not open_flagged and self.__board[i][j].flagged:
                    continue

                self.open_cell((j, i))

    def get_board(self) -> list:
        return self.__board

    def __add_cells(self, font):
        for i in range(self.size[1]):
            row = []
            for j in range(self.size[0]):
                row.append(Cell(self, (j, i), font))
            self.__board.append(row)

    def lose(self):
        """The player loses the game. Ends the game
        """

        if self.__game is None:
            return

        self.end_game("You lose", (255, 0, 0))

    def win(self):
        """The player wins the game. Ends the game. Adds a score to database.
        """

        if self.__game is None:
            return

        self.end_game("You win", (0, 255, 0))
        board_id = self.__game.database.get_board_id(self.size[0], self.size[1], self.__mine_chance)
        self.__game.database.add_score("Default", board_id, self.end_time - self.start_time)

    def end_game(self, message: str, color: tuple):
        """Ends the game. Adds a message to the UI.

        Args:
            message (str): The message that gets added to the UI.
            color (tuple): The color that the text gets rendered in.
        """

        self.game_over = True
        font = self.__game.create_font_with_new_size(30)
        text_object = TextObject(message, (600, 50), font, color=color)
        self.__game.window.current_view.add_message(text_object)
        self.end_time = time.time()

    def check_win(self) -> bool:
        """Checks if the player has won the game.

        Returns:
            bool: If the player has won the game.
        """

        for row in self.__board:
            for cell in row:
                if cell.hidden and cell.content != -1:
                    return False

        return True

    def calculate_cell_size(self):
        """Calculates the cell size so that the board can fit on the screen.
        """

        Cell.size = 35

        if self.size[0] * Cell.size > 1100:
            Cell.size = 1100 // self.size[0]

        if self.size[1] * Cell.size > 525:
            Cell.size = 525 // self.size[1]

    def __calculate_cell_font_size(self):
        if self.__game is None:
            return None

        return self.__game.create_font_with_new_size(Cell.size - 10)

    def __update_cell(self, cell, pos):
        if cell.flagged:
            self.mines_non_flagged += 1

        cell.hidden = False
        cell.flagged = False
        cell.button.background.color = (200, 200, 200)
        cell.button.hover_background.color = (200, 200, 200)
        cell.button.text.text = str(cell.content)
        cell.button.right_click_action = None
        cell.button.action = functools.partial(button_functions.open_around_an_open_cell, self, pos)

    def __check_for_recursion_stack_overflow(self) -> bool:
        if self.open_cell_recursion_stack_size <= 450:
            self.open_cell_recursion_stack_size += 1
            return False

        font = self.__game.create_font_with_new_size(20)
        self.__game.window.current_view.add_message(
            TextObject("Could not open any more cells in one click. " +
                       "Game is still fully operational.", (350, 25), font, color=(255, 150, 0)))
        return True
