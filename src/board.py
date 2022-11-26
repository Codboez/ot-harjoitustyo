import random
from cell import Cell

class Board:
    def __init__(self, width: int, height: int, mine_chance: int) -> None:
        self.width = width
        self.height = height
        self.__mine_chance = mine_chance
        self.__has_generated = False
        self.__board = []
        self.open_cell((3, 3))

    def open_cell(self, pos: tuple) -> bool:
        if not self.__has_generated:
            self.generate((pos[0], pos[1]))

        if self.is_out_of_bounds(pos):
            return False

        cell = self.__board[pos[1]][pos[0]]
        cell.hidden = False

        if cell.content == 0:
            self.open_around_cell((pos[0], pos[1]))

        return True

    def is_out_of_bounds(self, pos: tuple) -> bool:
        return (pos[0] < 0 or pos[0] >= len(self.__board[0])
         or pos[1] < 0 or pos[1] >= len(self.__board))

    def generate_mines(self, start_pos: tuple):
        if self.__has_generated:
            return

        for i in range(self.height):
            row = []
            for j in range(self.width):
                if (j in range(start_pos[0] - 1, start_pos[0] + 1)
                 and i in range(start_pos[1] - 1, start_pos[1] + 1)):
                    row.append(Cell(self, (j, i), content=0))
                    continue

                if random.randint(0, 100) <= self.__mine_chance:
                    row.append(Cell(self, (j, i), content=-1))
                else:
                    row.append(Cell(self, (j, i), content=0))

            self.__board.append(row)

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

    def open_around_cell(self, pos: tuple):
        for i in range(pos[1] - 1, pos[1] + 2):
            for j in range(pos[0] - 1, pos[0] + 2):
                if j == pos[0] and i == pos[1]:
                    continue

                if self.is_out_of_bounds((j, i)):
                    continue

                if self.__board[pos[1]][pos[0]].hidden:
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
