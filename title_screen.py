import ppb
from ppb.events import KeyPressed, StartScene

from player import Player
from score import Score
from spawner import Spawner

class TitleScreen(ppb.Sprite):
    image = ppb.Text(
        f'BLOCK HERO\n\nPRESS ANY KEY',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=48),
        color=(255, 255, 255)
    )

    def on_key_pressed(self, key_event: KeyPressed, signal):
        main_scene = ppb.Scene()
        main_scene.add(Player())
        main_scene.add(Spawner())
        main_scene.add(Score())
        signal(StartScene(main_scene))
