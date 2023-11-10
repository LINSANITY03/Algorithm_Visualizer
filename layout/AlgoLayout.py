from core.Game_core.GameCoreState import DrawGameState
import pygame as p


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
        self.font = p.font.Font("assets/font.ttf", 25)

        self.src_text = self.font.render("Source", True, p.Color("black"))
        self.dest_text = self.font.render(
            "Destination", True, p.Color("black"))
        self.wall_text = self.font.render(
            "Wall", True, p.Color("black"))
        self.start_text = self.font.render(
            "Start", True, p.Color("black"))

        self.src_btn = self.src_text.get_rect(topleft=(10, 10))
        self.dest_btn = self.dest_text.get_rect(topleft=(10, 40))
        self.wall_btn = self.wall_text.get_rect(topleft=(10, 70))
        self.start_btn = self.start_text.get_rect(topleft=(10, 100))
        self.create_button()

    def create_button(self):
        '''
        Draw the rectangular shape for src, dest, walls and start button on screen
        '''
        p.draw.rect(self.screen, p.Color("grey"), self.src_btn)
        p.draw.rect(self.screen, p.Color("grey"), self.dest_btn)
        p.draw.rect(self.screen, p.Color("grey"), self.wall_btn)
        p.draw.rect(self.screen, p.Color("grey"), self.start_btn)

        self.screen.blit(self.src_text, self.src_btn)
        self.screen.blit(self.dest_text, self.dest_btn)
        self.screen.blit(self.wall_text, self.wall_btn)
        self.screen.blit(self.start_text, self.start_btn)

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

    def get_start_btn(self):
        '''
        Returns the start button object
        '''

        return self.start_btn

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

    def create_start_selector(self):
        '''
        Display the running process
        '''
        if self.gs.isrunning:
            self.start_sel_text = self.font.render(
                "Searching best path...", True, p.Color("black"))
            self.start_sel_surf = self.start_sel_text.get_rect(
                topleft=(10, 110))
            self.screen.blit(self.start_sel_text, self.start_sel_surf)
        else:
            self.start_sel_text = self.font.render(
                "Done", True, p.Color("black"))
            self.start_sel_surf = self.start_sel_text.get_rect(
                topleft=(10, 110))
            self.screen.blit(self.start_sel_text, self.start_sel_surf)
