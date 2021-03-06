import ppb
from ppb.events import ButtonPressed, ButtonReleased, MouseMotion, Update
from scenes.game.sprites.destiny import Destiny
from scenes.game.sprites.projectile import Projectile
from scenes.game.sprites.target import Target


class Player(ppb.Sprite):
    layer = 1
    position = ppb.Vector(0, -7)
    direction = ppb.Vector(0, 0)
    speed = 0
    target = ppb.Vector(0, 0)
    fire_timer = 0.0
    move_speed = 4

    def find_closest_target(self, update_event: Update):
        closest = None
        min_distance = 1000000  # A big number

        for t in update_event.scene.get(kind=Target):
            distance = (t.position - self.position).length
            if distance < min_distance:
                min_distance = distance
                closest = t

        return closest

    def on_update(self, update_event: Update, signal):
        self.fire_timer += update_event.time_delta

        if self.fire_timer > 1 and self.speed == 0:
            self.fire_timer = 0
            closest_target = self.find_closest_target(update_event)

            if closest_target:
                update_event.scene.add(Projectile(
                    position=self.position,
                    direction=(closest_target.position -
                               self.position).normalize()
                ))

        self.position += self.direction * self.speed * update_event.time_delta

        # Prevent division by zero
        if (self.target - self.position).length > 0.0001:
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
        self.speed = self.move_speed

    def on_button_released(self, button_event: ButtonReleased, signal):
        button_event.scene.add(Destiny(button_event.position))
        self.target = button_event.position
        self.speed = self.move_speed

    def on_mouse_motion(self, mouse_event: MouseMotion, signal):
        if mouse_event.buttons:
            self.target = mouse_event.position
            self.speed = self.move_speed
