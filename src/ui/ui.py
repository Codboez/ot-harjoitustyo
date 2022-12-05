import pygame
from ui.game_view import GameView
from ui.start_view import StartView

class UI:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.create_window(screen_width, screen_height)
        self.current_view = None
        self.__state = -1
        font_path = pygame.font.match_font("timesnewroman")
        self.font = (pygame.font.Font(font_path, 24), font_path)

    def create_window(self, width, height):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen = pygame.display.set_mode((width, height))

    def update(self) -> bool:
        if not self.check_events(): return False

        if self.__state == -1:
            return

        self.current_view.update(self.screen)
        return True

    def check_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return False
            elif event.type == pygame.MOUSEMOTION:
                self.current_view.mouse_pos = event.pos
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.current_view.click(event.button)
            elif event.type == pygame.KEYDOWN:
                self.current_view.keydown(event.unicode)
        return True

    def change_state(self, state: int, board, game):
        if state == self.__state:
            return

        if state == 0:
            self.current_view = GameView(board, self.font, game)
        elif state == 1:
            self.current_view = StartView(self.font, game)
        
        self.__state = state

    def get_font_with_new_size(self, size: int) -> pygame.font.Font:
        return pygame.font.Font(self.font[1], size)
