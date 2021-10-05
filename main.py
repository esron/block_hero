import ppb

from player import Player
from target import Target


def setup(scene):
    scene.add(Player())

    for x in range(-4, 5, 2):
        scene.add(Target(position=ppb.Vector(x, 3)))

ppb.run(setup=setup)
