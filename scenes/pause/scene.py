from typing import Callable
import ppb
from ppb.events import KeyPressed, Quit, SceneStarted, StopScene
from ppb.keycodes import Q, Escape
from global_sprites.continue_sprite import ContinueSprite
from global_sprites.quit_sprite import QuitSprite
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
        self.add(QuitSprite())
        self.add(ContinueSprite())

    def on_key_pressed(self, key_event: KeyPressed, signal):
        if key_event.key == Escape:
            signal(StopScene(key_event.scene))
        if key_event.key == Q:
            signal(Quit())
