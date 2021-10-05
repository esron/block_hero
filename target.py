import ppb
from ppb.events import Update
from projectile import Projectile


class Target(ppb.Sprite):

    def on_update(self, update_event: Update, signal):
        for p in update_event.scene.get(kind=Projectile):
            if (p.position - self.position).length <= self.size:
                update_event.scene.remove(self)
                update_event.scene.remove(p)
                break
