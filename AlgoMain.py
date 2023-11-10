"""
This is our main driver file.
It will be responsible for handling user input and displaying the current AlgoState object.
"""

import pygame as p
import AlgoEngine
from core.Game_core import GameCoreState as gcs
from core.Game_core import GameVariable as gv
from layout.AlgoLayout import Button
from core.algorithms.a_star import AStar


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
        screen = p.display.set_mode((gv.SCREEN_WIDTH, gv.SCREEN_HEIGHT))
        clock = p.time.Clock()
        screen.fill(p.Color("dark green"))
        gs = AlgoEngine.GameState()
        loadImages()
        running = True
        while running:
            for e in p.event.get():
                if e.type == p.QUIT:
                    running = False
                if e.type == p.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        current_pos = e.pos

                        board_x = (current_pos[0] - gv.RECT_X)//gv.SQ_SIZE
                        board_y = (current_pos[1] - gv.RECT_Y)//gv.SQ_SIZE
                        if get_button.src_btn.collidepoint(current_pos) and not gs.issrc:
                            gs.issrc = True
                            gs.iswall = False
                            gs.isdtn = False
                            get_button.create_src_selector(True)

                        elif get_button.dest_btn.collidepoint(current_pos) and not gs.isdtn:
                            gs.isdtn = True
                            gs.issrc = False
                            gs.iswall = False
                            get_button.create_dest_selector(True)

                        elif get_button.wall_btn.collidepoint(current_pos):
                            if gs.iswall:
                                gs.iswall = False
                            else:
                                gs.iswall = True
                            gs.isdtn = False
                            gs.issrc = False

                        elif get_button.start_btn.collidepoint(current_pos):

                            if not gs.source and not gs.destination:
                                print("Please src and destination first")

                            elif gs.isrunning:
                                print("algorithm already running please wait...")
                            else:
                                gs.isrunning = True
                                path = AStar(
                                    gs.source, gs.destination, gs).search()
                                gs.isrunning = False
                                if path:
                                    for each in path:
                                        gs.board[each[0]][each[1]] = "xx"
                                else:
                                    print("no path")

                        elif gs.issrc and not gs.source:
                            if 0 <= board_x < gv.DIMENSIONS and 0 <= board_y < gv.DIMENSIONS:
                                gs.board[board_y][board_x] = "src"
                                gs.source = (board_y, board_x)
                                get_button.create_src_selector(False)

                        elif gs.isdtn and not gs.destination:
                            if 0 <= board_x < gv.DIMENSIONS and 0 <= board_y < gv.DIMENSIONS:
                                gs.board[board_y][board_x] = "dest"
                                gs.isdtn = True
                                gs.destination = (board_y, board_x)
                                get_button.create_dest_selector(False)

                        elif gs.iswall:
                            if 0 <= board_x < gv.DIMENSIONS and 0 <= board_y < gv.DIMENSIONS:
                                if [board_y, board_x] in gs.wall:
                                    gs.wall.remove([board_y, board_x])
                                    gs.board[board_y][board_x] = "--"
                                else:
                                    gs.wall.append([board_y, board_x])
                                    gs.board[board_y][board_x] = "wall"

            gcs.Drawboard(screen, gs)
            get_button = Button(screen, gs)
            clock.tick(gv.MAX_FPS)
            p.display.flip()


if __name__ == '__main__':
    MainRun()
