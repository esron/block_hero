import ppb


class GameOverSprite(ppb.Sprite):
    image = ppb.Text(
        'GAME OVER\n\nPRESS ANY KEY',
        font=ppb.Font('fonts\RobotoMono-Regular.ttf', size=48),  # noqa: W605
        color=(255, 255, 255)
    )
