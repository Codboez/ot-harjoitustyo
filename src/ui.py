import pygame

class UI:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        self.create_window(screen_width, screen_height)
        self.__running = True

    def create_window(self, width, height):
        pygame.init()
        pygame.display.set_caption("Minesweeper")
        self.screen = pygame.display.set_mode((width, height))

    def render(self):
        self.screen.fill((255, 255, 255))
        pygame.display.flip()

    def update(self) -> bool:
        self.check_events()
        self.render()
        return self.__running

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__running = False
