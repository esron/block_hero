import ppb
from ppb.events import ButtonPressed, ButtonReleased
from ppb_vector import Vector

class Destiny(ppb.Sprite):
    size = 0.5

    def __init__(self, position: Vector):
        self.position = position

    def on_button_pressed(self, button_event: ButtonPressed, signal):
        button_event.scene.remove(self)


    def on_button_released(self, button_event: ButtonReleased, signal):
        self.position = button_event.position
