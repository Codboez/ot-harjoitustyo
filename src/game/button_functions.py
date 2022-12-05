def open_cell(board, pos):
    board.open_cell(pos)

def switch_flagged(cell, board):
    cell.flagged = not cell.flagged

    if cell.flagged:
        board.mines_non_flagged -= 1
        cell.button.text.text = "F"
    else:
        board.mines_non_flagged += 1
        cell.button.text.text = ""

def create_board(width: int, height: int, mine_chance: int, game):
    game.create_board(width, height, mine_chance)
    game.change_state(0)

def create_custom_board(width, height, mine_chance, game):
    try:
        width = int(width.text)
        height = int(height.text)
        mine_chance = int(mine_chance.text)
    except ValueError:
        return

    game.create_board(width, height, mine_chance)
    game.change_state(0)

def open_around_an_open_cell(board, pos):
    for i in range(pos[1] - 1, pos[1] + 2):
        for j in range(pos[0] - 1, pos[0] + 2):
            if board.is_out_of_bounds((j, i)):
                print("Out of bounds")
                continue

            cell = board.get_board()[i][j]

            if cell.content == -1 and not cell.flagged:
                print(f"Cannot open: {j}, {i}")
                return
    print("Opening around cell")
    board.open_around_cell(pos, False)
