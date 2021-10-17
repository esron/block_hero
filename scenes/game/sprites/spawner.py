import ppb
from ppb.events import Update
from ppb_vector import Vector
from scenes.game.sprites.player import Player
from scenes.game.sprites.target import Target

class Spawner(ppb.Sprite):
    size = 3
    position = Vector(0, 8)
    max_enemies = 4
    spawn_timer = 0
    spawn_seconds = 2

    def on_update(self, update_event: Update, signal):
        self.spawn_timer += update_event.time_delta

        current_enemies = len(tuple(update_event.scene.get(kind=Target)))

        if current_enemies < self.max_enemies and self.spawn_timer > self.spawn_seconds:

            update_event.scene.add(Target(position=self.position))
            self.spawn_timer = 0

        if current_enemies != 0:
            for p in update_event.scene.get(kind=Player):
                for t in update_event.scene.get(kind=Target):
                    t.direction = (p.position - t.position).normalize()
                break
