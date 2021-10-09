import ppb
from ppb.events import Update


class Projectile(ppb.Sprite):
    size = 0.25
    speed = 6

    def on_update(self, update_event: Update, signal):
        if self.direction:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
