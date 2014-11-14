import sys
import pygame
import time
import Picross

__author__ = "Tristan Storz tristanstorz@gmail.com"
__email__ = "tristanstorz@gmail.com"
__status__ = "Development"
__version__ = "0.1.2"

SCREEN_SIZE = 640, 640
BLACK = 0, 0, 0
MENU_COLOR = 150, 150, 150
MENU_TEXT_COLOR = 0, 0, 0
MENU_TEXT_BACKGROUND = 10, 50, 60
MENU_TEXT_BACKGROUND_ACTIVE = 20, 80, 90
MENU_FONT_SIZE = 36
MENU_START = "START"
MENU_OPTION = "OPTION"
CAPTION = ("Picross: version: " + __version__)
CAPTION_IMAGE = pygame.image.load("Picross.png")

pygame.init()
pygame.display.set_icon(CAPTION_IMAGE)
pygame.display.set_caption(CAPTION)


class Picross_Menu(pygame.Surface):
    """docstring for Picross_Menu"""
    def __init__(self, size):
        super(Picross_Menu, self).__init__(size)
        # TODO font size dependent on the size of the menu's surface
        self.menu_font = pygame.font.SysFont("arial", 36)
        self.center = ((self.get_width() / 2, self.get_height() / 2))
        self.default_state_options = [Menu_Options(self.menu_font, "START"),
                                      Menu_Options(self.menu_font, "OPTIONS")]
        self.menu_default_state()

    def menu_default_state(self):
        self.fill(MENU_COLOR)
        self.state_options = self.default_state_options
        self.draw_menu(self.state_options)

    def draw_menu(self, menu_options):
        for index, option in enumerate(menu_options):
            left_align = self.center[0] - (option.size[0] / 2)
            top_align = self.center[1] - (option.size[1] / 2) + index * option.size[1]
            option.menu_position = (left_align, top_align)
            self.blit(option.surface, option.menu_position)

    def mouse_click(self, position):
        for option in self.default_state_options:
            if option.collidepoint(position):
                option.change_state("ON")
            else:
                option.change_state("OFF")

        self.draw_menu(self.state_options)


class Menu_Options(object):
    def __init__(self, menu_font, text):
        self.font = menu_font
        self.text = self.font.render(text, True, MENU_TEXT_COLOR)
        self.size = self.font.size(text)
        self.surface = pygame.Surface(self.size)
        self.state = "OFF"
        self.menu_position = (0, 0)
        self.surface.fill(MENU_TEXT_BACKGROUND)
        self.surface.blit(self.text, (0, 0))

    def change_state(self, new_state):
        if new_state is "OFF":
            self.state = "OFF"
            self.surface.fill(MENU_TEXT_BACKGROUND)
            self.surface.blit(self.text, (0, 0))
        else:
            self.state = "ON"
            self.surface.fill(MENU_TEXT_BACKGROUND_ACTIVE)
            self.surface.blit(self.text, (0, 0))

    def collidepoint(self, position):
        rectangle = self.surface.get_rect()
        rectangle.move_ip(self.menu_position)
        return rectangle.collidepoint(position)

screen = pygame.display.set_mode(SCREEN_SIZE)
menu = Picross_Menu(screen.get_size())


while True:
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.dict["button"] == 1:
                menu.mouse_click(event.dict["pos"])

    screen.blit(menu, (0, 0))
    pygame.display.flip()
