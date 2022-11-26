import pygame
from ui.game_view import GameView

class UI:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.create_window(screen_width, screen_height)
        self.__current_view = None
        self.__state = -1
        self.mouse_position = (0, 0)
        self.font = pygame.font.SysFont("timesnewroman", 24)

    def create_window(self, width, height):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen = pygame.display.set_mode((width, height))

    def update(self) -> bool:
        if not self.check_events(): return False

        if self.__state == -1:
            return

        self.__current_view.update(self.screen)
        return True

    def check_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEMOTION:
                self.__current_view.mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.__current_view.click(event.button)
        return True

    def change_state(self, state: int, board):
        if state == self.__state:
            return

        if state == 0:
            self.__current_view = GameView(board, self.font)
        elif state == 1:
            pass
        
        self.__state = state
