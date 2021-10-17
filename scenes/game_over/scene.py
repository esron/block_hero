import ppb
from ppb.events import KeyPressed, SceneStarted, StopScene

from scenes.game_over.sprites.game_over_sprite import GameOverSprite


class GameOverScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(GameOverSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        signal(StopScene(key_event.scene))
