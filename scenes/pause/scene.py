from typing import Callable
import ppb
from ppb.events import KeyPressed, SceneStarted, StopScene
from scenes.pause.sprites.continue_sprite import ContinueSprite

from scenes.pause.sprites.pause_menu_title_sprite import PauseMenuTitleSprite
from scenes.pause.sprites.score_sprite import ScoreSprite


class PauseScene(ppb.Scene):
    background_color = (75, 75, 75)

    def __init__(self, *, set_up: Callable = None, **props):
        super().__init__(set_up=set_up, **props)
        self.points = props['points']

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(PauseMenuTitleSprite())
        self.add(ScoreSprite(points=self.points))
        self.add(ContinueSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        signal(StopScene(key_event.scene))
