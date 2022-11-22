from random import Random
from cell import Cell

class Board:
    def __init__(self, width: int, height: int, mine_chance: int) -> None:
        self.__width = width
        self.__height = height
        self.__mine_chance = mine_chance
        self.__has_generated = False
        self.__board = []

    def open_cell(self, x: int, y: int) -> bool:
        if self.is_out_of_bounds(x, y):
            return False

        if not self.__has_generated:
            self.generate((x, y))

        cell = self.__board[y][x]
        cell.hidden = False

        if cell.content == 0:
            self.open_around_cell(x, y)

    def is_out_of_bounds(self, x: int, y: int) -> bool:
        return x >= 0 and x < len(self.__board[0]) and y >= 0 and y < len(self.__board)

    def generate_mines(self, start_pos: tuple):
        if self.__has_generated:
            return

        for y in range(len(self.__height)):
            row = []
            for x in range(len(self.__width)):
                if x in range(start_pos[0] - 1, start_pos[0] + 1) and y in range(start_pos[1] - 1, start_pos[1] + 1):
                    continue

                if Random.randint(0, 100) <= self.__mine_chance:
                    row.append(Cell(content=-1))
                else:
                    row.append(Cell(content=0))

            self.__board.append(row)

    def generate_numbers(self):
        if self.__has_generated:
            return

        for y in range(len(self.__board)):
            for x in range(len(self.__board[y])):
                if self.__board[y][x].content == -1:
                    continue

                self.__board[y][x].content = self.count_mines_around_cell(x, y)

    def count_mines_around_cell(self, x: int, y: int) -> int:
        amount = 0
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if j == x and i == y:
                    continue

                if self.__board[i][j].content == -1:
                    amount += 1

        return amount

    def generate(self, start_pos: tuple):
        self.generate_mines(start_pos)
        self.generate_numbers()

    def open_around_cell(self, x: int, y: int):
        for i in range(y - 1, y + 2):
            for j in range(x - 1, x + 2):
                if j == x and i == y:
                    continue

                if self.is_out_of_bounds(j, i):
                    continue

                if self.__board[y][x].hidden:
                    self.open_cell(j, i)