import ppb
from ppb.events import SceneStarted
from title_screen import TitleScreen


class MainScene(ppb.Scene):
    background_color = (0, 0, 0)

    def on_scene_started(self, scene_event: SceneStarted, signal):
        print('Main Scene')
        self.add(TitleScreen())
