from core.Game_core.GameCoreState import DrawGameState
import pygame as p


class Button(DrawGameState):

    '''
    Responsible for lifecycle of source, destination, walls and start button.
    '''

    def __init__(self, screen, gs) -> None:
        '''Initialize the required attribute to create the buttons.

        Args:
          screen: Current display screen surface.
        '''
        super().__init__(screen, gs)

        p.font.init()

        self.color = p.Color("white")
        self.font = p.font.Font("assets/font.ttf", 25)
        self.font2 = p.font.Font("assets/font.ttf", 8)

        self.src_image = p.image.load("assets/source_surface.png")
        self.dest_image = p.image.load("assets/dest_surface.png")
        self.wall_image = p.image.load("assets/wall_surface.png")
        self.start_image = p.image.load("assets/start_surface.png")

        self.src_text = self.font.render("Source", True, self.color)
        self.dest_text = self.font.render(
            "Destination", True, self.color)
        self.wall_text = self.font.render(
            "Wall", True, self.color)
        self.start_text = self.font.render(
            "Start", True, self.color)
        self.reset_text = self.font.render(
            "Reset", True, self.color)

        self.src_rect = self.src_text.get_rect(topleft=(30, 30))
        self.dest_rect = self.dest_text.get_rect(topleft=(30, 130))
        self.wall_rect = self.wall_text.get_rect(topleft=(30, 230))
        self.start_rect = self.start_text.get_rect(
            topleft=(30, 430))
        self.reset_rect = self.reset_text.get_rect(
            topleft=(30, 530))
        self.create_button()

    def center_image_to_text(self, image, rect):
        '''
        Center the image to the given object position

        Args:
          image: Object representing the loaded image.
          rect: Rectangular object to be centered on.

        Returns:
          New object with text and image same center position.
        '''
        return image.get_rect(center=rect.center)

    def create_button(self):
        '''
        Draw the rectangular shape for src, dest, walls and start button on screen
        '''

        self.screen.blit(
            self.src_image, self.center_image_to_text(self.src_image, self.src_rect))
        self.screen.blit(
            self.dest_image, self.center_image_to_text(self.dest_image, self.dest_rect))
        self.screen.blit(
            self.wall_image, self.center_image_to_text(self.wall_image, self.wall_rect))
        self.screen.blit(
            self.start_image, self.center_image_to_text(self.start_image, self.start_rect))
        self.screen.blit(
            self.start_image, self.center_image_to_text(self.start_image, self.reset_rect))

        self.screen.blit(self.src_text, self.src_rect)
        self.screen.blit(self.dest_text, self.dest_rect)
        self.screen.blit(self.wall_text, self.wall_rect)
        self.screen.blit(self.start_text, self.start_rect)
        self.screen.blit(self.reset_text, self.reset_rect)

    def text_below_parent(self, parent):
        '''Gives the position below 20px of parent.

        Args:
          parent: Surface you want to set the bottom value.

        Returns:
          Tuple representing position 20px below the parent position.
        '''
        return (parent.bottomleft[0], parent.bottomleft[1]+20)

    def create_src_selector(self, toggle):
        '''Display the helper text to select the source cell.

        Args:
          toggle: Bool value to represent on and off state.
        '''
        if toggle:
            self.src_sel_text = self.font2.render(
                "Select source", True, p.Color("black"))
            self.src_sel_surf = self.src_sel_text.get_rect(
                topleft=self.text_below_parent(self.src_rect))
            self.screen.blit(self.src_sel_text, self.src_sel_surf)

        else:
            if self.gs.source:
                self.src_sel_text = self.font2.render(
                    "Source selected", True, p.Color("black"))
                self.src_sel_surf = self.src_sel_text.get_rect(
                    topleft=self.text_below_parent(self.src_rect))
                self.screen.blit(p.image.load(
                    "assets/source_text_sel.png"), self.src_sel_surf)
                self.screen.blit(self.src_sel_text, self.src_sel_surf)

    def create_dest_selector(self, toggle):
        '''Display the helper text to select the destination cell.

        Args:
          toggle: Bool value to represent on and off state.
        '''

        if toggle:
            self.dest_sel_text = self.font2.render(
                "Select destination", True, p.Color("black"))
            self.dest_sel_surf = self.dest_sel_text.get_rect(
                topleft=self.text_below_parent(self.dest_rect))
            self.screen.blit(self.dest_sel_text, self.dest_sel_surf)
        else:
            if self.gs.destination:
                self.dest_sel_text = self.font2.render(
                    "Destination selected", True, p.Color("black"))
                self.dest_sel_surf = self.dest_sel_text.get_rect(
                    topleft=self.text_below_parent(self.dest_rect))
                self.screen.blit(p.image.load(
                    "assets/dest_text_sel.png"), self.dest_sel_surf)
                self.screen.blit(self.dest_sel_text, self.dest_sel_surf)

    def create_start_selector(self, text=None):
        '''Display the running process.

        Args:
          text: String you want to show when start button is pressed.
        '''

        self.start_sel_text = self.font2.render(
            text, True, p.Color("black"))
        self.start_sel_surf = self.start_sel_text.get_rect(
            topleft=self.text_below_parent(self.start_rect))
        self.screen.blit(p.image.load(
            "assets/start_text_sel.png"), self.start_sel_surf)
        self.screen.blit(self.start_sel_text, self.start_sel_surf)
