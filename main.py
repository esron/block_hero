import ppb
from player import Player
from score import Score
from spawner import Spawner
from target import Target


def setup(scene):
    scene.add(Player())
    scene.add(Spawner())
    scene.add(Score())

    for x in range(-4, 5, 2):
        scene.add(Target(position=ppb.Vector(x, 3)))

ppb.run(setup=setup)
