import pygame as p
from . import GameVariable as gv


class DrawGameState:

    '''Responsible for all the graphics within a current game state.
    '''

    def __init__(self, screen, gs) -> None:
        '''Initialize the screen properties and game state for children class

        Args:
          screen: Current display screen surface.
          gs: Current game state.
        '''

        self.screen = screen
        self.gs = gs


class Drawboard(DrawGameState):

    '''Draw the squares on the board
    '''

    def __init__(self, screen, gs) -> None:
        '''
        Initializes the Rectangular board with the parent class.

        Args:
          screen: Current display screen surface.
          gs: Current game state.
        '''

        super().__init__(screen, gs)
        self.colors = [p.Color("gray"), p.Color("green"),
                       p.Color("red"), p.Color("brown"),
                       p.Color("blue"), p.Color("black")]
        self.draw_Rect()

    def draw_Rect(self):
        '''
        Create a gray rectangular first and grid along border as per the loop
        '''

        p.draw.rect(self.screen, self.colors[0],
                    (gv.RECT_X, gv.RECT_Y, gv.RECT_WIDTH, gv.RECT_HEIGHT))

        for r in range(gv.DIMENSIONS):
            for c in range(gv.DIMENSIONS):
                rect_obj = p.Rect(gv.RECT_X+c*gv.SQ_SIZE, gv.RECT_Y +
                                  r*gv.SQ_SIZE, gv.SQ_SIZE, gv.SQ_SIZE)
                if self.gs.board[r][c] == "src":
                    p.draw.rect(self.screen, self.colors[1], rect_obj)
                elif self.gs.board[r][c] == "dest":
                    p.draw.rect(self.screen, self.colors[2], rect_obj)
                elif self.gs.board[r][c] == "wall":
                    p.draw.rect(self.screen, self.colors[3], rect_obj)
                elif self.gs.board[r][c] == "vs":
                    p.draw.rect(self.screen, self.colors[4], rect_obj)
                elif self.gs.board[r][c] == "xx":
                    p.draw.rect(self.screen, self.colors[5], rect_obj)

                p.draw.rect(self.screen, p.Color("black"), rect_obj, 1)
