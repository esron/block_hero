import ppb
from ppb.events import SceneStarted
from scenes.game.sprites.player import Player
from scenes.game.sprites.score import Score
from scenes.game.sprites.spawner import Spawner
from scenes.game.sprites.target import Target

class GameScene(ppb.Scene):

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(Player())
        self.add(Spawner())
        self.add(Score())

        for x in range(-4, 5, 2):
            self.add(Target(position=ppb.Vector(x, 3)))
