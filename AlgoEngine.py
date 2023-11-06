"""
This class is responsible for storing all the information about the current state of a Algo game. 
It will also be responsible for determining the valid moves as the current state.
It will also keep a move log.
"""


class GameState:
    def __init__(self) -> None:
        # board is a 11x11 2-D array list.
        # "--" represents the empty space.
        self.board = [
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"],
            ["--", "--", "--", "--", "--", "--", "--", "--", "--", "--", "--"]
        ]
        self.movelog = []
        self.wall = []
        self.iswall = False
        self.source = None
        self.issrc = False
        self.destination = None
        self.isdtn = False
