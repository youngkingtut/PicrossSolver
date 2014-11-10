import sys
import pygame
import time
import Picross

__author__ = "Tristan Storz tristanstorz@gmail.com"
__email__ = "tristanstorz@gmail.com"
__status__ = "Development"
__version__ = "0.1.1"

SCREEN_SIZE = 640, 640
BLACK = 0, 0, 0
MENU_COLOR = 150, 150, 150
MENU_TEXT_COLOR = 0, 0, 0
CAPTION = ("Picross: version: " + __version__)
CAPTION_IMAGE = pygame.image.load("Picross.png")

pygame.init()
pygame.display.set_icon(CAPTION_IMAGE)
pygame.display.set_caption(CAPTION)


class Picross_Menu(pygame.Surface):
    """docstring for Picross_Menu"""
    def __init__(self, size):
        super(Picross_Menu, self).__init__(size)
        self.create_menu()

    def create_menu(self):
        self.fill(MENU_COLOR)
        self.add_menu_options()

    def add_menu_options(self):
        self.menu_font = pygame.font.SysFont("arial", 36)
        menu_width_center = self.get_width() / 2
        menu_height_center = self.get_height() / 2
        text_height = self.menu_font.get_height()
        print text_height

        start = self.menu_font.render("Start", True, MENU_TEXT_COLOR)
        options = self.menu_font.render("Options", True, MENU_TEXT_COLOR)
        self.blit(start, (0, 0))
        self.blit(options, (0, 100))


screen = pygame.display.set_mode(SCREEN_SIZE)
menu = Picross_Menu(screen.get_size())


while True:
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.dict["button"] == 1:
                print "yes ma'm"

    screen.blit(menu, (0, 0))
    pygame.display.flip()
