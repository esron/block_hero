import ppb
from ppb.events import KeyPressed, Quit, SceneStarted, StopScene
from ppb.keycodes import Q, Space
from global_sprites.continue_sprite import ContinueSprite
from global_sprites.quit_sprite import QuitSprite

from scenes.game_over.sprites.game_over_sprite import GameOverSprite


class GameOverScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(GameOverSprite())
        self.add(ContinueSprite())
        self.add(QuitSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == Space:
            signal(StopScene(key_event.scene))
        if key_event.key == Q:
            signal(Quit())
