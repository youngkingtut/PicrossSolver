import pygame
from gameconfig import GameConfig


class Layer(pygame.Surface):
    layers = []
    master_screen = pygame.display.set_mode(GameConfig.SCREEN_SIZE)

    @classmethod
    def update(cls):
        for layer in cls.layers:
            cls.master_screen.blit(layer, layer.position)
        pygame.display.flip()

    @classmethod
    def append_layer(cls, layer):
        cls.layers.append(layer)

    @classmethod
    def remove_layer(cls, layer):
        cls.layers.remove(layer)

    def __init__(self, size, position=(0, 0)):
        super(Layer, self).__init__(size)
        self.position = position
        self.clear()
        Layer.append_layer(self)

    def clear(self):
        self.fill(GameConfig.CLEAN_SCREEN)
