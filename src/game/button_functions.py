def open_cell(board, pos):
    """Calls the board to open the cell at the given position.

    Args:
        board (Board): The board that the cell is attached to.
        pos (tuple): The position in the board that is opened.
    """

    board.open_cell(pos)

def switch_flagged(cell, board):
    """Alternates the given cell between flagged and not flagged.

    Args:
        cell (Cell): The cell whose flagged is flipped.
        board (Board): The board that the cell is attached to.
    """

    cell.flagged = not cell.flagged

    if cell.flagged:
        board.mines_non_flagged -= 1
        cell.button.text.text = "F"
    else:
        board.mines_non_flagged += 1
        cell.button.text.text = ""

def create_board(width: int, height: int, mine_chance: int, game):
    """Calls the game to create a board with the given information.

    Args:
        width (int): The width of the new board.
        height (int): The height of the new board.
        mine_chance (int): The mine chance of the new board.
        game (Game): The game that a new board is being created to.
    """

    game.create_board(width, height, mine_chance)
    game.change_state(0)

def create_custom_board(width, height, mine_chance, game):
    """Creates a board with custom information if inputs are valid.

    Args:
        width (TextObject): The text object that contains the width of the new board.
        height (TextObject): The text object that contains the height of the new board.
        mine_chance (TextObject): The text object that contains the mine chance of the new board.
        game (Game): The game that a new board is being created to.
    """

    game.window.current_view.delete_messages()
    has_invalid_inputs = has_invalid_inputs_for_custom_board_creation(width, height, mine_chance)

    if has_invalid_inputs[0]:
        game.window.current_view.add_error_message(has_invalid_inputs[1], (500, 350))
        return

    game.create_board(int(width.text), int(height.text), int(mine_chance.text))
    game.change_state(0)

def has_invalid_inputs_for_custom_board_creation(width, height, mine_chance) -> tuple:
    """Checks if the given inputs are invalid.

    Args:
        width (TextObject): The text object that contains the width of the new board.
        height (TextObject): The text object that contains the height of the new board.
        mine_chance (TextObject): The text object that contains the mine chance of the new board.

    Returns:
        tuple: If the inputs were invalid, The error message.
    """

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
    """Opens around a cell if enough flags are surrounding it.

    Args:
        board (Board): The board should get opened.
        pos (tuple): The position on the board to open around.
    """

    if board.count_flags_around_cell(pos) != board.get_board()[pos[1]][pos[0]].content:
        return

    board.open_around_cell(pos, False)
