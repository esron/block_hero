import ppb
from ppb_vector import Vector


class RulesSprite(ppb.Sprite):
    position = Vector(0, 4)
    image = ppb.Text(
        'RULES',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
