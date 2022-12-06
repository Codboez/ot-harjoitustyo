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
    game.window.current_view.delete_messages()
    has_invalid_inputs = has_invalid_inputs_for_custom_board_creation(width, height, mine_chance)

    if has_invalid_inputs[0]:
        game.window.current_view.add_error_message(has_invalid_inputs[1], (500, 350))
        return

    game.create_board(int(width.text), int(height.text), int(mine_chance.text))
    game.change_state(0)

def has_invalid_inputs_for_custom_board_creation(width, height, mine_chance) -> tuple:
    try:
        width = int(width.text)
        height = int(height.text)
        mine_chance = int(mine_chance.text)
    except ValueError:
        return (True, "All values must be integer")

    if width < 1 or width > 60:
        return (True, "Width must be between 1 and 60")

    if height < 1 or height > 30:
        return (True, "Height must be between 1 and 30")

    if mine_chance < 0 or mine_chance > 100:
        return (True, "Mine percentage must be between 0 and 100")

    return (False, "")

def open_around_an_open_cell(board, pos):
    for i in range(pos[1] - 1, pos[1] + 2):
        for j in range(pos[0] - 1, pos[0] + 2):
            if board.is_out_of_bounds((j, i)):
                continue

            cell = board.get_board()[i][j]

            if cell.content == -1 and not cell.flagged:
                return

    board.open_around_cell(pos, False)
