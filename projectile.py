import ppb


class Projectile(ppb.Sprite):
    size = 0.25
    direction = ppb.Vector(0, 1)
    speed = 6

    def on_update(self, update_event, signal):
        if self.direction:
            direction = self.direction.normalize()
        else:
            direction = self.direction
        self.position += direction * self.speed * update_event.time_delta
