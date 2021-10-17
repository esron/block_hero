import ppb
from ppb.events import SceneContinued, SceneStarted, StartScene, StopScene, Update
from scenes.game.sprites.player import Player
from scenes.game.sprites.score import Score
from scenes.game.sprites.spawner import Spawner
from scenes.game.sprites.target import Target
from scenes.game_over.scene import GameOverScene

class GameScene(ppb.Scene):

    def on_scene_started(self, scene_event: SceneStarted, signal):
        self.add(Player())
        self.add(Spawner())
        self.add(Score())

        for x in range(-4, 5, 2):
            self.add(Target(position=ppb.Vector(x, 3)))

    def on_update(self, update_event: Update, signal):
        for p in update_event.scene.get(kind=Player):
            for t in update_event.scene.get(kind=Target):
                if (t.position - p.position).length <= p.size:
                    signal(StartScene(GameOverScene()))
                    break
            break

    # Work around a scene transaction flow from
    # Start Scene -> Game -> Game Over -> Start Scene
    def on_scene_continued(self, scene_event: SceneContinued, signal):
        signal(StopScene(scene_event.scene))
