class Gamestate():
    def __init__(self):
        self.location = "spawn"
        self.triggered_finite_events = [] # Only tracks one time events.

    def move_player(self, target):
        self.location = target

    def track_event(self, trigger):
        self.triggered_events.append(trigger)