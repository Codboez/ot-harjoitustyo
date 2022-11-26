import pygame
from board import Board

class GameView:
    def __init__(self, board: Board, font):
        self.__board = board
        self.__buttons = []
        self.mouse_pos = (0, 0)
        self.__font = font

    def render(self, screen):
        screen.fill((255, 255, 255))
        self.render_board(screen)
        pygame.display.flip()

    def render_board(self, screen):
        for i, row in enumerate(self.__board.get_board()):
            for j, cell in enumerate(row):
                self.render_cell(screen, cell)

    def render_cell(self, screen, cell):
        if cell.hidden:
            cell.button.render(screen)
        else:
            pygame.draw.rect(screen, (160, 160, 160), pygame.Rect(cell.pos[0], cell.pos[1], cell.size, cell.size))
            text = self.__font.render(f"{cell.content}", True, (0, 0, 0))
            screen.blit(text, (cell.pos[0] + cell.size / 2 - 5, cell.pos[1] + 3))

    def update(self, screen):
        self.update_cell_buttons()
        self.render(screen)

    def update_cell_buttons(self):
        for i, row in enumerate(self.__board.get_board()):
            for j, cell in enumerate(row):
                cell.button.update_hovered(self.mouse_pos)
