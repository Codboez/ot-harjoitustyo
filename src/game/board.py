import random
import functools
from ui.text_object import TextObject
from game.cell import button_functions, Cell

class Board:
    def __init__(self, width: int, height: int, mine_chance: int, game) -> None:
        self.size = (width, height)
        self.__mine_chance = mine_chance
        self.__has_generated = False
        self.__board = []
        self.mines_non_flagged = 0
        self.__game = game
        self.game_over = False
        self.open_cell_recursion_stack_size = 0
        self.calculate_cell_size()
        font = self.calculate_cell_font_size()
        self.add_cells(font)

    def open_cell(self, pos: tuple) -> bool:
        if not self.__has_generated:
            self.generate((pos[0], pos[1]))

        if self.is_out_of_bounds(pos):
            return False

        cell = self.__board[pos[1]][pos[0]]
        self.update_cell(cell, pos)

        if cell.content == 0:
            if self.check_for_recursion_stack_overflow():
                return False
            self.open_around_cell((pos[0], pos[1]))
        elif cell.content == -1:
            self.lose()

        if self.check_win():
            self.win()

        return True

    def is_out_of_bounds(self, pos: tuple) -> bool:
        return (pos[0] < 0 or pos[0] >= len(self.__board[0])
                or pos[1] < 0 or pos[1] >= len(self.__board))

    def generate_mines(self, start_pos: tuple):
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
        if self.__has_generated:
            return

        for i, row in enumerate(self.__board):
            for j, cell in enumerate(row):
                if cell.content == -1:
                    continue

                cell.content = self.count_mines_around_cell((j, i))

    def count_mines_around_cell(self, pos: tuple) -> int:
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

    def generate(self, start_pos: tuple):
        self.generate_mines(start_pos)
        self.generate_numbers()
        self.__has_generated = True

    def open_around_cell(self, pos: tuple, open_flagged: bool = True):
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

    def get_board(self):
        return self.__board

    def print(self):
        for board_row in self.__board:
            row_print = ""
            for cell in board_row:
                row_print += ("m " if cell.content == -1
                              else str(cell.content) + " ")
            print(row_print)

    def add_cells(self, font):
        for i in range(self.size[1]):
            row = []
            for j in range(self.size[0]):
                row.append(Cell(self, (j, i), font))
            self.__board.append(row)

    def lose(self):
        if self.__game is None:
            return

        self.game_over = True
        font = self.__game.create_font_with_new_size(30)
        text_object = TextObject("You lose", (600, 50), font, color=(255, 0, 0))
        self.__game.window.current_view.add_message(text_object)

    def win(self):
        if self.__game is None:
            return

        self.game_over = True
        font = self.__game.create_font_with_new_size(30)
        text_object = TextObject("You win", (600, 50), font, color=(0, 255, 0))
        self.__game.window.current_view.add_message(text_object)

    def check_win(self) -> bool:
        for row in self.__board:
            for cell in row:
                if cell.hidden and cell.content != -1:
                    return False

        return True

    def calculate_cell_size(self):
        Cell.size = 35

        if self.size[0] * Cell.size > 1100:
            Cell.size = 1100 // self.size[0]

        if self.size[1] * Cell.size > 525:
            Cell.size = 525 // self.size[1]

    def calculate_cell_font_size(self):
        if self.__game is None:
            return None

        return self.__game.create_font_with_new_size(Cell.size - 10)

    def update_cell(self, cell, pos):
        cell.hidden = False
        cell.button.background.color = (200, 200, 200)
        cell.button.hover_background.color = (200, 200, 200)
        cell.button.text.text = str(cell.content)
        cell.button.right_click_action = None
        cell.button.action = functools.partial(button_functions.open_around_an_open_cell, self, pos)

    def check_for_recursion_stack_overflow(self) -> bool:
        if self.open_cell_recursion_stack_size <= 450:
            self.open_cell_recursion_stack_size += 1
            return False

        font = self.__game.create_font_with_new_size(20)
        self.__game.window.current_view.add_message(
            TextObject("Could not open any more cells in one click. " +
                        "Game is still fully operational.", (350, 25), font, color=(255, 150, 0)))
        return True
