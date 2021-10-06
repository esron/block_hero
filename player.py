import ppb
from ppb.events import ButtonPressed, ButtonReleased, MouseMotion, Update
from ppb_vector import Vector
from destiny import Destiny


class Player(ppb.Sprite):
    position = ppb.Vector(0, -7)
    direction = ppb.Vector(0, 0)
    speed  = 0
    target = Vector(0 ,0)

    def on_update(self, update_event: Update, signal):
        self.position += self.direction * self.speed * update_event.time_delta

        if (self.target - self.position).length > 0.0001: #  Prevent division by zero
            self.direction = (self.target - self.position).normalize()
        else:
            self.speed = 0

        for d in update_event.scene.get(kind=Destiny):
            if (d.position - self.position).length + 0.4 < d.size:
                update_event.scene.remove(d)
                self.speed = 0
                break

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
