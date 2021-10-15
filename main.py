import ppb
from title_screen import TitleScreen

start_scene = ppb.Scene()
start_scene.background_color = (0, 0, 0)
start_scene.add(TitleScreen())

ppb.GameEngine(first_scene=start_scene).run()
