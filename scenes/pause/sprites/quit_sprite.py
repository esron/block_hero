import ppb
from ppb_vector import Vector


class QuitSprite(ppb.Sprite):
    position = Vector(0, -7)
    image = ppb.Text(
        'PRESS Q TO QUIT',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
