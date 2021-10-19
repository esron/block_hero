import ppb
from ppb_vector import Vector


class PauseMenuTitleSprite(ppb.Sprite):
    size = 2
    position = Vector(0, 2)
    image = ppb.Text(
        'GAME PAUSED',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24*2),  # noqa: W605
        color=(255, 255, 255)
    )
