"""This game is a minimalist Archero clone using ppb
"""

import ppb
from scenes.title.scene import TitleScene

ppb.GameEngine(first_scene=TitleScene()).run()
