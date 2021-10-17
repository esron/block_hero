import ppb
from ppb.events import KeyPressed, SceneStarted, StartScene
from player import Player
from score import Score
from spawner import Spawner
from target import Target
from title_sprite import TitleSprite


class TitleScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(TitleSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        game_scene = ppb.Scene()
        game_scene.add(Player())
        game_scene.add(Spawner())
        game_scene.add(Score())

        # Add 5 initial targets
        for x in range(-4, 5, 2):
            game_scene.add(Target(position=ppb.Vector(x, 3)))
        signal(StartScene(game_scene))
