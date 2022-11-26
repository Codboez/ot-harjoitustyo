import functools
from ui.button import Button
import button_functions

class Cell:
    def __init__(self, board, pos: tuple, content: int = 0,
     hidden: bool = True, flagged: bool = False) -> None:
        self.__board = board
        self.size = 35
        self.content = content
        self.hidden = hidden
        self.flagged = flagged
        self.pos = self.__calculate_position(pos)
        button_action = functools.partial(button_functions.open_cell, board, pos)
        self.button = Button(self.pos[0], self.pos[1], 35, 35, button_action)

    def __calculate_position(self, indexes):
        return (1280 / 2 - self.__board.width / 2 * self.size + indexes[0] * (self.size + 1),
                    720 / 2 - self.__board.height / 2 * self.size + indexes[1] * (self.size + 1))
