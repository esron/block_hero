import ppb
from ppb.events import KeyPressed, SceneStarted, StartScene
from game_scene import GameScene
from title_sprite import TitleSprite


class TitleScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(TitleSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        signal(StartScene(GameScene()))
