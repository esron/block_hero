import ppb
from ppb.events import KeyPressed, StopScene

class GameOverSprite(ppb.Sprite):
    image = ppb.Text(
        f'GAME OVER\n\nPRESS ANY KEY',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=48),
        color=(255, 255, 255)
    )

    def on_key_pressed(self, key_event: KeyPressed, signal):
        signal(StopScene(key_event.scene))
