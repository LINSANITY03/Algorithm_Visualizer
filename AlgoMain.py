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
                if e.type == p.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        current_pos = e.pos
                        if get_button.src_btn.collidepoint(current_pos):
                            gs.issrc = True
                            get_button.create_src_selector(True)

                        elif get_button.dest_btn.collidepoint(current_pos):
                            gs.isdtn = True
                            get_button.create_dest_selector(True)

                        elif gs.issrc and not gs.source:
                            board_x = (current_pos[0] - RECT_X)//SQ_SIZE
                            board_y = (current_pos[1] - RECT_Y)//SQ_SIZE
                            if 0 <= board_x <= 10 and 0 <= board_y <= 10:
                                gs.board[board_y][board_x] = "src"
                                gs.source = True
                                get_button.create_src_selector(False)

                        elif gs.isdtn and not gs.destination:
                            board_x = (current_pos[0] - RECT_X)//SQ_SIZE
                            board_y = (current_pos[1] - RECT_Y)//SQ_SIZE
                            if 0 <= board_x <= 10 and 0 <= board_y <= 10:
                                gs.board[board_y][board_x] = "dest"
                                gs.destination = True
                                get_button.create_dest_selector(False)

            Drawboard(screen, gs)
            get_button = Button(screen, gs)
            clock.tick(MAX_FPS)
            p.display.flip()


class DrawGameState:

    '''
    Responsible for all the graphics within a current game state.
    '''

    def __init__(self, screen, gs) -> None:
        '''
        Initialize the screen properties and game state for children class
        '''

        self.screen = screen
        self.gs = gs


class Drawboard(DrawGameState):

    '''
    Draw the squares on the board
    '''

    def __init__(self, screen, gs) -> None:
        '''
        Initializes the Rectangular board with the parent class
        '''

        super().__init__(screen, gs)
        self.draw_Rect()

    def draw_Rect(self):
        '''
        Create a gray rectangular first and grid along border as per the loop
        '''

        colors = [p.Color("green"), p.Color("red")]
        p.draw.rect(self.screen, p.Color("gray"),
                    (RECT_X, RECT_Y, RECT_WIDTH, RECT_HEIGHT))
        for r in range(DIMENSIONS):
            for c in range(DIMENSIONS):
                rect_obj = p.Rect(RECT_X+c*SQ_SIZE, RECT_Y +
                                  r*SQ_SIZE, SQ_SIZE, SQ_SIZE)
                p.draw.rect(self.screen, p.Color("black"), rect_obj, 1)
                if self.gs.board[r][c] == "src":
                    p.draw.rect(self.screen, colors[0], rect_obj)
                elif self.gs.board[r][c] == "dest":
                    p.draw.rect(self.screen, colors[1], rect_obj)


class Button(DrawGameState):

    '''
    Responsible for choosing src, destin
    '''

    def __init__(self, screen, gs) -> None:
        '''
        Initialize the required attribute to create the buttons
        '''
        super().__init__(screen, gs)
        p.font.init()
        self.font = p.font.SysFont("Grobold", 15)

        self.src_text = self.font.render("Source", True, p.Color("black"))
        self.dest_text = self.font.render(
            "Destination", True, p.Color("black"))
        self.wall_text = self.font.render(
            "Wall", True, p.Color("black"))

        self.src_btn = self.src_text.get_rect(topleft=(10, 10))
        self.dest_btn = self.dest_text.get_rect(topleft=(10, 40))
        self.wall_btn = self.wall_text.get_rect(topleft=(10, 70))
        self.create_button()

    def create_button(self):
        '''
        Draw the rectangular shape for src and dest button on screen
        '''
        p.draw.rect(self.screen, p.Color("grey"), self.src_btn)
        p.draw.rect(self.screen, p.Color("grey"), self.dest_btn)
        p.draw.rect(self.screen, p.Color("grey"), self.wall_btn)

        self.screen.blit(self.src_text, self.src_btn)
        self.screen.blit(self.dest_text, self.dest_btn)
        self.screen.blit(self.wall_text, self.wall_btn)

    def get_src_btn(self):
        '''
        Returns the src button object
        '''

        return self.src_btn

    def get_dest_btn(self):
        '''
        Returns the destination button object
        '''

        return self.dest_btn

    def create_src_selector(self, toggle):
        '''
        Display the helper text to select the source cell
        '''
        if toggle:
            self.src_sel_text = self.font.render(
                "Select your source", True, p.Color("black"))
            self.src_sel_surf = self.src_sel_text.get_rect(topleft=(10, 20))
            self.screen.blit(self.src_sel_text, self.src_sel_surf)
        else:
            if self.gs.source:
                self.src_sel_text = self.font.render(
                    "Source selected", True, p.Color("black"))
                self.src_sel_surf = self.src_sel_text.get_rect(
                    topleft=(10, 20))
                self.screen.blit(self.src_sel_text, self.src_sel_surf)

    def create_dest_selector(self, toggle):
        '''
        Display the helper text to select the destination cell
        '''
        if toggle:
            self.dest_sel_text = self.font.render(
                "Select your destination", True, p.Color("black"))
            self.dest_sel_surf = self.dest_sel_text.get_rect(topleft=(10, 50))
            self.screen.blit(self.dest_sel_text, self.dest_sel_surf)
        else:
            if self.gs.destination:
                self.dest_sel_text = self.font.render(
                    "Destination selected", True, p.Color("black"))
                self.dest_sel_surf = self.dest_sel_text.get_rect(
                    topleft=(10, 50))
                self.screen.blit(self.dest_sel_text, self.dest_sel_surf)


if __name__ == '__main__':
    MainRun()
