import ppb
from ppb.events import KeyPressed, SceneStarted, StopScene

from scenes.pause.sprites.pause_menu_title_sprite import PauseMenuTitleSprite


class PauseScene(ppb.Scene):
    background_color = (75, 75, 75)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(PauseMenuTitleSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        signal(StopScene(key_event.scene))
