import ppb
from ppb_vector import Vector


class StartSprite(ppb.Sprite):
    position = Vector(0, -3)
    image = ppb.Text(
        'PRESS SPACE TO START',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )