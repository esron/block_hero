import ppb
from ppb.events import SceneStarted
from player import Player
from score import Score
from spawner import Spawner
from target import Target

class GameScene(ppb.Scene):

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(Player())
        self.add(Spawner())
        self.add(Score())

        for x in range(-4, 5, 2):
            self.add(Target(position=ppb.Vector(x, 3)))
