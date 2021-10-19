import ppb


class ScoreSprite(ppb.Sprite):

    def __init__(self, **props):
        super().__init__(**props)
        self.image = ppb.Text(
            f'SCORE {props["points"]}',
            font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24),  # noqa: W605 E501
            color=(255, 255, 255)
        )
