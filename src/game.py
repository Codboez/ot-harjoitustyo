from ui import UI
from board import Board

class Game:
    def __init__(self) -> None:
        self.__running = True
        self.__window = UI(640, 480)

    def run(self):
        while self.__running:
            self.__running = self.__window.update()