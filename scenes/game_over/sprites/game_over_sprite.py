import ppb


class GameOverSprite(ppb.Sprite):
    size = 3
    image = ppb.Text(
        'GAME OVER',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=24*3),  # noqa: W605
        color=(255, 255, 255)
    )
