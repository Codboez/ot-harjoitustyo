import sqlite3

def __create_table_scores():
    sql = "CREATE TABLE Scores(id INTEGER PRIMARY KEY, "
    sql += "player VARCHAR(255), board_id INTEGER, time FLOAT, creation_date DATETIME);"
    execute_sql_command(sql, [])

def create_connection():
    database = sqlite3.connect("scores.db")
    database.isolation_level = None
    return database

def __create_table_boards():
    sql = "CREATE TABLE Boards(id INTEGER PRIMARY KEY, width INTEGER,"
    sql += " height INTEGER, mine_chance INTEGER);"
    execute_sql_command(sql, [])

def set_up():
    open("scores.db", "x").close()

    __create_table_scores()
    __create_table_boards()
    add_default_boards()

def add_board(width: int, height: int, mine_chance: int):
    if (not isinstance(width, int) or not isinstance(height, int)
            or not isinstance(mine_chance, int)):
        return

    sql = "INSERT INTO Boards(width, height, mine_chance) VALUES(?, ?, ?);"
    execute_sql_command(sql, [width, height, mine_chance])

def add_default_boards():
    add_board(10, 10, 15)
    add_board(15, 15, 20)
    add_board(30, 20, 25)

def get_all_boards() -> list:
    return execute_sql_select_command("SELECT * FROM Boards;", [])

def get_all_scores() -> list:
    return execute_sql_select_command("SELECT * FROM Scores;", [])

def add_score(player: str, board_id: int, time: float):
    sql = "INSERT INTO Scores(player, board_id, time, creation_date) "
    sql += "VALUES(?, ?, ?, datetime('now', 'localtime'));"
    return execute_sql_command(sql, [player, board_id, time])

def delete_score(score_id: int):
    return execute_sql_command("DELETE FROM Scores WHERE id=?;", [score_id])

def get_board_id(width: int, height: int, mine_chance: int) -> int:
    sql = "SELECT id FROM Boards WHERE width=? AND height=? AND mine_chance=?;"
    board_id = execute_sql_select_command(sql, [width, height, mine_chance])

    if len(board_id) == 0:
        add_board(width, height, mine_chance)
        return get_board_id(width, height, mine_chance)

    return board_id[0][0]

def get_sorted_scores_for_board(board_id: int, limit: int) -> list:
    sql = "SELECT * FROM Scores WHERE board_id=? ORDER BY time LIMIT ?;"
    return execute_sql_select_command(sql, [board_id, limit])

def execute_sql_command(sql: str, args: list):
    try:
        database = create_connection()
        database.execute(sql, args)
    finally:
        database.close()

def execute_sql_select_command(sql: str, args: list) -> list:
    try:
        database = create_connection()
        return database.execute(sql, args).fetchall()
    finally:
        database.close()

if __name__ == "__main__":
    print(get_all_boards())
    print(get_all_scores())
