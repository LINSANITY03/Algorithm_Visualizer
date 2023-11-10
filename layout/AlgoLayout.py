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

        self.color = p.Color("white")
        self.font = p.font.Font("assets/font.ttf", 25)
        self.image = p.image.load("assets/algo_btn_surf.png")

        self.src_text = self.font.render("Source", True, self.color)
        self.dest_text = self.font.render(
            "Destination", True, self.color)
        self.wall_text = self.font.render(
            "Wall", True, self.color)
        self.start_text = self.font.render(
            "Start", True, self.color)

        self.src_rect = self.src_text.get_rect(topleft=(30, 30))
        self.dest_rect = self.dest_text.get_rect(topleft=(30, 90))
        self.wall_rect = self.wall_text.get_rect(topleft=(30, 150))
        self.start_rect = self.start_text.get_rect(topleft=(30, 210))
        self.create_button()

    def center_image_to_text(self, rect):
        '''
        Center the image to the given object position
        '''
        return self.image.get_rect(center=rect.center)

    def create_button(self):
        '''
        Draw the rectangular shape for src, dest, walls and start button on screen
        '''

        self.screen.blit(
            self.image, self.center_image_to_text(self.src_rect))
        self.screen.blit(
            self.image, self.center_image_to_text(self.dest_rect))
        self.screen.blit(
            self.image, self.center_image_to_text(self.wall_rect))
        self.screen.blit(
            self.image, self.center_image_to_text(self.start_rect))

        self.screen.blit(self.src_text, self.src_rect)
        self.screen.blit(self.dest_text, self.dest_rect)
        self.screen.blit(self.wall_text, self.wall_rect)
        self.screen.blit(self.start_text, self.start_rect)

    def get_src_btn(self):
        '''
        Returns the src button object
        '''

        return self.src_rect

    def get_dest_btn(self):
        '''
        Returns the destination button object
        '''

        return self.dest_rect

    def get_start_btn(self):
        '''
        Returns the start button object
        '''

        return self.start_rect

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
