import functools
from ui.button import Button
import button_functions

class Cell:
    size = 35

    def __init__(self, board, pos: tuple, font, content: int = 0,
     hidden: bool = True, flagged: bool = False) -> None:
        self.__board = board
        self.content = content
        self.hidden = hidden
        self.flagged = flagged
        self.pos = self.__calculate_position(pos)
        button_action = functools.partial(button_functions.open_cell, board, pos)
        button_right_click_action = functools.partial(button_functions.switch_flagged, self, board)
        self.button = Button(self.pos[0], self.pos[1], Cell.size, Cell.size,
          button_action, font, button_right_click_action)

    def __calculate_position(self, indexes):
        board_center = (1280 / 2, 720 / 2 + 70)
        all_cells_width = self.__board.width * Cell.size
        all_cells_height = self.__board.height * Cell.size
        location_in_board = (indexes[0] * (Cell.size + 1), indexes[1] * (Cell.size + 1))
        gaps_between_cells_size = (self.__board.width - 1, self.__board.height - 1)

        return (board_center[0] - all_cells_width / 2 + location_in_board[0] -
         gaps_between_cells_size[0] / 2, board_center[1] - all_cells_height / 2 +
         location_in_board[1] - gaps_between_cells_size[1] / 2)
