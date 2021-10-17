import ppb
from ppb_vector import Vector


class HoldSprite(ppb.Sprite):
    position = Vector(0, -2)
    image = ppb.Text(
        'Hold mouse button to follow mouse',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
