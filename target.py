import ppb
from ppb.events import Update
from ppb_vector import Vector
from projectile import Projectile


class Target(ppb.Sprite):
    speed = 2
    direction = Vector(0, 0)

    def on_update(self, update_event: Update, signal):
        for p in update_event.scene.get(kind=Projectile):
            if (p.position - self.position).length <= self.size:
                update_event.scene.remove(self)
                update_event.scene.remove(p)
                break

        self.position += self.direction * self.speed * update_event.time_delta
