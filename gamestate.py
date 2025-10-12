class Gamestate():
    def __init__(self):
        self.location = "spawn"

    def move_player(self, target):
        self.location = target