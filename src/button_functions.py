def open_cell(board, pos):
    board.open_cell(pos)

def switch_flagged(cell, board):
    cell.flagged = not cell.flagged

    if cell.flagged:
        board.mines_non_flagged -= 1
        cell.button.text = "F"
    else:
        board.mines_non_flagged += 1
        cell.button.text = ""

def create_board(width: int, height: int, mine_chance: int, game):
    game.create_board(width, height, mine_chance)
    game.change_state(0)
