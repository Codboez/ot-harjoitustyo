import sqlite3

def __create_table_scores():
    sql = "CREATE TABLE Scores(id INTEGER PRIMARY KEY, "
    sql += "player VARCHAR(255), board_id INTEGER, time FLOAT, creation_date DATETIME);"
    execute_sql_command(sql, [])

def create_connection(file_path: str = "scores.db"):
    """Creates a connection to the given database file.

    Args:
        file_path (str, optional): The path to the database file. Defaults to "scores.db".

    Returns:
        Connection: The connection to the database.
    """

    database = sqlite3.connect(file_path)
    database.isolation_level = None
    return database

def __create_table_boards():
    sql = "CREATE TABLE Boards(id INTEGER PRIMARY KEY, width INTEGER,"
    sql += " height INTEGER, mine_chance INTEGER);"
    execute_sql_command(sql, [])

def set_up():
    """Creates and sets up a new database file.
    """

    with open("scores.db", "x", encoding="utf-8"):
        pass

    __create_table_scores()
    __create_table_boards()
    add_default_boards()

def add_board(width: int, height: int, mine_chance: int):
    """Adds a new board to the database.

    Args:
        width (int): The width of the board.
        height (int): The height of the board.
        mine_chance (int): The mine chance of the board.
    """

    if (not isinstance(width, int) or not isinstance(height, int)
            or not isinstance(mine_chance, int)):
        return

    sql = "INSERT INTO Boards(width, height, mine_chance) VALUES(?, ?, ?);"
    execute_sql_command(sql, [width, height, mine_chance])

def add_default_boards():
    """Adds the default boards to the database.
    """

    add_board(10, 10, 15)
    add_board(15, 15, 20)
    add_board(30, 20, 25)

def get_all_boards() -> list:
    """Gets all boards from the database.

    Returns:
        list: A list of all boards.
    """

    return execute_sql_select_command("SELECT * FROM Boards;", [])

def get_all_scores() -> list:
    """Gets all scores from the database.

    Returns:
        list: A list of all scores.
    """

    return execute_sql_select_command("SELECT * FROM Scores;", [])

def add_score(player: str, board_id: int, time: float):
    """Adds a score to the database.

    Args:
        player (str): The name of the player.
        board_id (int): The id of the board.
        time (float): The time it took to finish the game.
    """

    sql = "INSERT INTO Scores(player, board_id, time, creation_date) "
    sql += "VALUES(?, ?, ?, datetime('now', 'localtime'));"
    execute_sql_command(sql, [player, board_id, time])

def delete_score(score_id: int):
    """Deletes a score from the database.

    Args:
        score_id (int): The id of the score.
    """

    execute_sql_command("DELETE FROM Scores WHERE id=?;", [score_id])

def get_board_id(width: int, height: int, mine_chance: int) -> int:
    """Gets the id of the board with the given information.
    If a board with the given information does not exist it adds a new board.

    Args:
        width (int): The width of the board.
        height (int): The height of the board.
        mine_chance (int): The mine chance of the board.

    Returns:
        int: The id of the board.
    """

    sql = "SELECT id FROM Boards WHERE width=? AND height=? AND mine_chance=?;"
    board_id = execute_sql_select_command(sql, [width, height, mine_chance])

    if len(board_id) == 0:
        add_board(width, height, mine_chance)
        return get_board_id(width, height, mine_chance)

    return board_id[0][0]

def get_sorted_scores_for_board(board_id: int, limit: int) -> list:
    """Get the scores of the given board sorted by time.

    Args:
        board_id (int): The id of the board.
        limit (int): The maximum amount of scores returned.

    Returns:
        list: A list of scores.
    """

    sql = "SELECT * FROM Scores WHERE board_id=? ORDER BY time LIMIT ?;"
    return execute_sql_select_command(sql, [board_id, limit])

def execute_sql_command(sql: str, args: list):
    """Executes the given sql command with the given arguments.

    Args:
        sql (str): The sql command.
        args (list): The arguments for the sql command.
    """

    try:
        database = create_connection()
        database.execute(sql, args)
    except sqlite3.OperationalError:
        print("The path to the database file is invalid.")
    finally:
        database.close()

def execute_sql_select_command(sql: str, args: list) -> list:
    """Executes the given sql select command with the given arguments.

    Args:
        sql (str): A select command.
        args (list): The arguments for the command.

    Returns:
        list: A list of what the select command returned.
    """

    try:
        database = create_connection()
        return database.execute(sql, args).fetchall()
    except sqlite3.OperationalError:
        print("The path to the database file is invalid.")
        return None
    finally:
        database.close()

if __name__ == "__main__":
    print(get_all_boards())
    print(get_all_scores())
