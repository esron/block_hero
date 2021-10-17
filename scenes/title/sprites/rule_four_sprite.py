import ppb
from ppb_vector import Vector


class RuleFourSprite(ppb.Sprite):
    position = Vector(0, 0)
    image = ppb.Text(
        '4. Press Escape to pause',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
