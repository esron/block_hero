import ppb
from ppb.events import KeyPressed, StartScene

from player import Player
from score import Score
from spawner import Spawner
from target import Target

class TitleSprite(ppb.Sprite):
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

        # Add 5 initial targets
        for x in range(-4, 5, 2):
            main_scene.add(Target(position=ppb.Vector(x, 3)))
        signal(StartScene(main_scene))
