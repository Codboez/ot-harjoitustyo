import pygame
from ui.game_view import GameView
from ui.start_view import StartView

class UI:
    """The user interface for Minesweeper.

    Attributes:
        current_view (StartView | GameView): The current view.
        font (tuple): The default font and the path to its file.
    """

    def __init__(self, screen_width: int = 1280, screen_height: int = 720) -> None:
        """Creates a new UI object.

        Args:
            screen_width (int, optional): The width of the screen. Defaults to 1280.
            screen_height (int, optional): The height of the screen. Defaults to 720.
        """

        self.create_window(screen_width, screen_height)
        self.current_view = None
        self.__state = -1
        font_path = pygame.font.match_font("timesnewroman")
        self.font = (pygame.font.Font(font_path, 24), font_path)

    def create_window(self, width, height):
        """Initializes pygame and creates a window.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
        """

        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen = pygame.display.set_mode((width, height))

    def update(self) -> bool:
        """Updates the UI.

        Returns:
            bool: If the UI was updated successfully.
        """

        if not self.check_events(): return False

        if self.__state == -1:
            return False

        self.current_view.update(self.screen)
        return True

    def check_events(self) -> bool:
        """Checks for events.

        Returns:
            bool: If events were checked successfully.
        """

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
        """Changes the scene that gets rendered.

        Args:
            state (int): The state that should be changed to.
            board (Board): The board attached to the game.
            game (_type_): The game that is controlling this UI.
        """

        if state == self.__state:
            return

        if state == 0:
            self.current_view = GameView(board, self.font, game)
        elif state == 1:
            self.current_view = StartView(self.font, game)
        
        self.__state = state

    def get_font_with_new_size(self, size: int) -> pygame.font.Font:
        """Creates a new font with new size using the default font.

        Args:
            size (int): The size of the new font.

        Returns:
            Font: The new font.
        """

        return pygame.font.Font(self.font[1], size)
