import pygame


class EventControl(object):
    def __init__(self, registered_events):
        self.event_map = registered_events
        self.load_events()

    def load_events(self):
        pygame.event.set_allowed(None)
        for event in self.event_map:
            pygame.event.set_allowed(event)

    def poll_event(self):
        event = pygame.event.poll()
        if event.type in self.event_map:
            self.event_map[event.type](event)
