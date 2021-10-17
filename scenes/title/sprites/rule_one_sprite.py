import ppb
from ppb_vector import Vector


class RuleOneSprite(ppb.Sprite):
    position = Vector(0, 1)
    image = ppb.Text(
        '1. Don\'t get caught by the targets',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
