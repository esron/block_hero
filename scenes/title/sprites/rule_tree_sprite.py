import ppb
from ppb_vector import Vector


class RuleTreeSprite(ppb.Sprite):
    position = Vector(0, -1)
    image = ppb.Text(
        '3. Click to move',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605
        color=(255, 255, 255)
    )
