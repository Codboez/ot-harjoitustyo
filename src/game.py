from ui.ui import UI
from board import Board

class Game:
    def __init__(self) -> None:
        self.__running = True
        self.__window = UI(1280, 720)
        self.board = Board(10, 10, 20)
        self.change_state(0)

    def run(self):
        while self.__running:
            self.__running = self.__window.update()

    def change_state(self, state: int):
        self.__window.change_state(state, self.board)

    def create_board(self, width, height, mine_chance):
        self.board = Board(width, height, mine_chance)
