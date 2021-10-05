import ppb
from ppb.events import ButtonPressed, ButtonReleased, MouseMotion, Update
from ppb_vector import Vector
from destiny import Destiny


class Player(ppb.Sprite):
    position = ppb.Vector(0, -7)
    direction = ppb.Vector(0, 0)
    speed  = 4
    target = position

    def on_update(self, update_event: Update, signal):
        self.position += self.direction * self.speed * update_event.time_delta

        for d in update_event.scene.get(kind=Destiny):
            if (d.position - self.position).length <= d.size:
                update_event.scene.remove(d)
                break

        if self.target - self.position != Vector(0, 0): #  Prevent division by zero
            self.direction = (self.target - self.position).normalize()
            return

        self.speed = 0

    def on_button_pressed(self, button_event: ButtonPressed, signal):
        self.target = button_event.position
        self.speed = 4

    def on_button_released(self, button_event: ButtonReleased, signal):
        button_event.scene.add(Destiny(button_event.position))
        self.target = button_event.position
        self.speed = 4

    def on_mouse_motion(self, mouse_event: MouseMotion, signal):
        if mouse_event.buttons:
            self.target = mouse_event.position
            self.speed = 4
