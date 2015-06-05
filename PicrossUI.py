import pygame
from gameconfig import GameConfig
from layer import Layer
from control import EventControl


class State(object):
    def __init__(self, state_vars):
        self.state_vars = state_vars

    def run(self):
        return None


class StateHandler(object):
    def __init__(self):
        self.screen = None
        self.current_state = None
        self.state_vars = {}

    def setup(self):
        pygame.init()
        pygame.display.set_caption(GameConfig.CAPTION)
        self.current_state = GameMenu(self.state_vars)

    def run_game(self):
        while self.current_state:
            current_state_object = self.current_state.run()
            if not hasattr(current_state_object, '__call__'):
                self.current_state = current_state_object
            else:
                self.current_state = current_state_object(self.screen, self.state_vars)

    @staticmethod
    def teardown():
        pygame.quit()


class GameMenu(State):
    def __init__(self, *args, **kwargs):
        State.__init__(self, *args, **kwargs)
        self.surface = None
        self.clock = None
        self.controls = None
        self.font = None
        self.exit = False
        self.buttons = None
        self.setup()

    def setup(self):
        self.surface = Layer(GameConfig.SCREEN_SIZE)
        self.surface.fill(GameConfig.MENU_COLOR)
        self.clock = pygame.time.Clock()
        self.controls = EventControl({
            pygame.QUIT: self.quit,
            pygame.MOUSEMOTION: self.mouse_movement_event
        })
        self.font = pygame.font.Font(None, GameConfig.MENU_FONT_SIZE)

        self.buttons = [
            Button("START", self.font, GameConfig.MENU_TEXT_COLOR, (40, 40)),
            Button("OPTIONS", self.font, GameConfig.MENU_TEXT_COLOR, (40, 40)),
            Button("EXIT", self.font, GameConfig.MENU_TEXT_COLOR, (40, 40)),

        ]

    def run(self):
        while not self.exit:
            self.clock.tick(GameConfig.FRAMES_PER_SECOND)
            self.controls.poll_event()
            self.draw_menu()
            Layer.update()

        return None

    def draw_menu(self):
        for button in self.buttons:
            self.surface.blit(button.surface, button.position)

    def mouse_movement_event(self, event):
        for button in self.buttons:
            if button.rect.collidepoint(event.pos):
                print button.text

    def quit(self, event):
        self.exit = True


class Button(object):
    def __init__(self, text, font, color, position):
        self.text = text
        self.font = font
        self.size = self.font.size(text)
        self.surface = self.font.render(text, True, color)
        self.position = position
        self.rect = self.surface.get_rect(left=position[0], top=position[1])
