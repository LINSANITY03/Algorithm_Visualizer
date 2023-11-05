"""
This is our main driver file.
It will be responsible for handling user input and displaying the current AlgoState object.
"""

import pygame as p
import AlgoEngine

SCREEN_WIDTH = 720
SCREEN_HEIGHT = 405
DIMENSIONS = 11  # representing 11x11 board
SQ_SIZE = SCREEN_HEIGHT // DIMENSIONS
MAX_FPS = 30
IMAGES = {}

# Rectangle dimensions
RECT_WIDTH = RECT_HEIGHT = SQ_SIZE * DIMENSIONS

# Calculate the position of the rectangle to center it
RECT_X = (SCREEN_WIDTH - RECT_WIDTH) // 2
RECT_Y = (SCREEN_HEIGHT - RECT_HEIGHT) // 2


def loadImages():
    '''
    Initialize a global dictionary of images. This will be called exactly once in the main.
    '''
    pass


class MainRun:

    '''
    The main driver for our code. This will handle user input and updating the graphics.
    '''

    def __init__(self) -> None:
        p.init()
        p.display.set_caption("Algo Visualizer")
        p.display.set_icon(p.image.load("./assets/logo.png"))
        screen = p.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        clock = p.time.Clock()
        screen.fill(p.Color("dark green"))
        gs = AlgoEngine.GameState()
        loadImages()
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
            Drawboard(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()


class DrawGameState:

    '''
    Responsible for all the graphics within a current game state.
    '''

    def __init__(self, screen, gs) -> None:
        self.screen = screen
        self.gs = gs


class Drawboard(DrawGameState):

    '''
    Draw the squares on the board
    '''

    def __init__(self, screen, gs) -> None:
        super().__init__(screen, gs)

        p.draw.rect(screen, p.Color("gray"),
                    (RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                rect_obj = p.Rect(RECT_X+c*SQ_SIZE, RECT_Y +
                                  r*SQ_SIZE, SQ_SIZE, SQ_SIZE)
                p.draw.rect(screen, p.Color("black"), rect_obj, 1)


if __name__ == '__main__':
    MainRun()
