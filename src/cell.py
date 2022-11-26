class Cell:
    def __init__(self, content: int = 0, hidden: bool = True, flagged: bool = False) -> None:
        self.content = content
        self.hidden = hidden
        self.flagged = flagged
        