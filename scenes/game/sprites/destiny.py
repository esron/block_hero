import ppb
from ppb.events import ButtonPressed
from ppb_vector import Vector

class Destiny(ppb.Sprite):
    size = 0.5

    def __init__(self, position: Vector):
        self.position = position

    def on_button_pressed(self, button_event: ButtonPressed, signal):
        button_event.scene.remove(self)
