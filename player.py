import ppb
from ppb.buttons import Primary
from ppb.events import ButtonPressed, ButtonReleased, MouseMotion
from ppb_vector import Vector


class Player(ppb.Sprite):
    position = ppb.Vector(0, -7)
    direction = ppb.Vector(0, 0)
    speed  = 4
    target = position

    def on_update(self, update_event, signal):
        self.position += self.direction * self.speed * update_event.time_delta
        if self.target - self.position != Vector(0, 0): #  Prevent division by zero
            self.direction = (self.target - self.position).normalize()
            return

        self.speed = 0

    def on_button_pressed(self, button_event: ButtonPressed, signal):
        self.target = button_event.position
        self.speed = 4

    def on_button_released(self, button_event: ButtonReleased, signal):
        self.target = button_event.position
        self.speed = 4

    def on_mouse_motion(self, mouse_event: MouseMotion, signal):
        if mouse_event.buttons:
            self.target = mouse_event.position
            self.speed = 4
