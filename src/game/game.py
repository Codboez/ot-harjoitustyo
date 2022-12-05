from ui.ui import UI
from game.board import Board

class Game:
    def __init__(self) -> None:
        self.__running = True
        self.window = UI(1280, 720)
        self.font = self.window.font
        self.board = Board(10, 10, 20, self.font[0], self)
        self.change_state(1)

    def run(self):
        while self.__running:
            self.__running = self.window.update()

    def change_state(self, state: int):
        self.window.change_state(state, self.board, self)

    def create_board(self, width, height, mine_chance):
        self.board = Board(width, height, mine_chance, self.font[0], self)

    def create_font_with_new_size(self, size: int):
        return self.window.get_font_with_new_size(size)