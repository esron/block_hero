import ppb
from ppb.events import Update

class Score(ppb.Sprite):
    position = ppb.Vector(-10, 8)
    points = 0
    image = ppb.Text(
        f'SCORE  {points}',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),
        color=(255, 255, 255)
    )

    def on_update(self, update_event: Update, signal):
        self.image = ppb.Text(
            f'SCORE  {self.points}',
            font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),
            color=(255, 255, 255)
        )
