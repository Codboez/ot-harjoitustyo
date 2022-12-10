import os
from ui.ui import UI
from game.board import Board
from database import scores

class Game:
    def __init__(self) -> None:
        self.__running = True
        self.check_database_exists()
        self.window = UI(1280, 720)
        self.font = self.window.font
        self.board = Board(10, 10, 20, self)
        self.change_state(1)

    def run(self):
        while self.__running:
            self.__running = self.window.update()

    def change_state(self, state: int):
        self.window.change_state(state, self.board, self)

    def create_board(self, width, height, mine_chance):
        self.board = Board(width, height, mine_chance, self)

    def create_font_with_new_size(self, size: int):
        return self.window.get_font_with_new_size(size)

    def check_database_exists(self):
        if not os.path.exists("database/scores.db"):
            scores.set_up()
