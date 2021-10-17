import ppb
from ppb_vector import Vector


class RuleTwoSprite(ppb.Sprite):
    position = Vector(0, 2)
    image = ppb.Text(
        '2. You can only shoot if you are still',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
