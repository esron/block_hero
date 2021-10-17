import ppb
from ppb_vector import Vector


class TitleSprite(ppb.Sprite):
    size = 3
    position = Vector(0, 4)
    image = ppb.Text(
        'BLOCK HERO',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24*3),  # noqa: W605
        color=(255, 255, 255)
    )
